import config

class SequenceFactory():
    """
    Nozzle selection and quality sequence generator
    Written by Daan Treurniet, april 3, 2018
    This class generates the clock, black and color data for printing.

    How to use:
    After instantiating a Sequence_factory object,
    everything is done with the get_sequence function.

    You can choose which nozzles fire with the following arguments:
    nozzles_black = [1,2,3,4,.......,87,88,89,90]
    nozzles_cyan = [1,2,3,4,........27,28,29,30]
    nozzles_magenta = [1,2,3,4,........27,28,29,30]
    nozzles_yellow = [1,2,3,4,........27,28,29,30]

    To choose droplet size, set the size argument to:
    'small', 'medium' or 'large'

    To set quality settings: set the quality argument to:
    'economy', 'jeff', 'all', 'VSD1', 'VSD2' or 'VSD3'

    The function will return a list of 16-bit words, with 6 bits of data.
    The placement of these bits is defined in the config file.
    """



    def __init__(self):
        pass

    def _nozzle_to_pulse_black(self, nozzle):
        if nozzle >= 61: return (30-(nozzle-60))*2+1
        if nozzle <= 30: return (116-nozzle)*2+1
        else: return (73-(nozzle-30))*2+1
    def _nozzle_to_pulse_cyan(self, nozzle): return (116-nozzle)*2+1
    def _nozzle_to_pulse_magenta(self, nozzle): return (73-(nozzle))*2+1
    def _nozzle_to_pulse_yellow(self, nozzle): return (30-(nozzle))*2+1

    def _get_selection_block(self,
                              nozzles_black, nozzles_cyan,
                              nozzles_yellow, nozzles_magenta):
        tmp_data_black = [0]*256
        tmp_data_color = [0]*256
        # Populate black nozzle data
        for nozzle_b in nozzles_black:
            tmp_data_black[self._nozzle_to_pulse_black(nozzle_b)] = 1
            tmp_data_black[self._nozzle_to_pulse_black(nozzle_b)+1] = 1
        # Populate color nozzle data
        for nozzle_c in nozzles_cyan:
            tmp_data_color[self._nozzle_to_pulse_cyan(nozzle_c)] = 1
            tmp_data_color[self._nozzle_to_pulse_cyan(nozzle_c)+1] = 1
        for nozzle_m in nozzles_magenta:
            tmp_data_color[self._nozzle_to_pulse_magenta(nozzle_m)] = 1
            tmp_data_color[self._nozzle_to_pulse_magenta(nozzle_m)+1] = 1
        for nozzle_y in nozzles_yellow:
            tmp_data_color[self._nozzle_to_pulse_yellow(nozzle_y)] = 1
            tmp_data_color[self._nozzle_to_pulse_yellow(nozzle_y)+1] = 1
        return (tmp_data_black, tmp_data_color)

    def _get_quality_sequence(self, quality):
        tmp_data = [0]*64

        if quality == 'economy': i_list = [40,50,52,54,56]
        if quality == 'VSD1': i_list = [24,26,32,36,40,42,48,62]
        if quality == 'VSD2': i_list = [28,32,40,48,50,62]
        if quality == 'VSD3': i_list = [36,40,48,50,62]
        if quality == 'jeff': i_list = [1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,33,34,35,36,37,38,39,40,41,42,43,44,49,50,51,52,53,54,55,56,57,58,59,60]
        if quality == 'all': i_list = list(range(1,63))

        for i in i_list:
            tmp_data[i] = 1
            tmp_data[i+1] = 1
        return tmp_data

    def _tuple_to_word_list(self, lists):
        signal_len = len(lists[0])
        signal = [0x0]*signal_len
        for i in range(signal_len):
            signal[i] |= (lists[0][i] << config.GPIO_NCHG)
            signal[i] |= (lists[1][i] << config.GPIO_CH)
            signal[i] |= (lists[2][i] << config.GPIO_LAT)
            signal[i] |= (lists[3][i] << config.GPIO_CK)
            signal[i] |= (lists[4][i] << config.GPIO_SIBL)
            signal[i] |= (lists[5][i] << config.GPIO_SICL)
        return signal


    def get_sequence2(self, nozzles_black=[], nozzles_yellow=[], nozzles_cyan=[], nozzles_magenta=[], size='medium', quality='VSD2'):
        data_NCHG = [1]
        data_CH = [0]
        data_LAT = [0]
        data_CK = [0]
        data_SIBL = [0]
        data_SICL = [0]

        # First pulse
        data_NCHG.extend([0]*48)
        data_CH.extend([0]*24 + [1]*12 + [0]*12)
        data_LAT.extend([1]*12 + [0]*36)
        data_CK.extend([0]*48)
        data_SIBL.extend([0]*48)
        data_SICL.extend([0]*48)

        # Idle
        data_NCHG.extend([1]*440)
        data_CH.extend([0]*440)
        data_LAT.extend([0]*440)
        data_CK.extend([0]*440)
        data_SIBL.extend([0]*440)
        data_SICL.extend([0]*440)

        #Second pulse
        data_NCHG.extend([0]*48)
        data_CH.extend([0]*24 + [1]*12 + [0]*12)
        data_LAT.extend([0]*48)
        data_CK.extend([0]*48)
        data_SIBL.extend([0]*48)
        data_SICL.extend([0]*48)

        # Idle
        data_NCHG.extend([1]*56)
        data_CH.extend([0]*56)
        data_LAT.extend([0]*56)
        data_CK.extend([0]*56)
        data_SIBL.extend([0]*56)
        data_SICL.extend([0]*56)

        # Data block 1
        for i in range(32):
            data_NCHG.extend([1]*4)
            data_CH.extend([0]*4)
            data_LAT.extend([0]*4)
            data_CK.extend([1]*2)
            if (2*i) in nozzles_black:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([1,1,0])
            else:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([0,0,0])
            data_CK.extend([0]*2)
            if (2*i)+1 in nozzles_black:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([1,1,0])
            else:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([0,0,0])
            data_SICL.extend([0]*4)

        # Idle
        data_NCHG.extend([1]*151)
        data_CH.extend([0]*151)
        data_LAT.extend([0]*151)
        data_CK.extend([0]*151)
        data_SIBL.extend([0]*151)
        data_SICL.extend([0]*151)

        #Third pulse
        data_NCHG.extend([0]*48)
        data_CH.extend([0]*24 + [1]*12 + [0]*12)
        data_LAT.extend([0]*48)
        data_CK.extend([0]*48)
        data_SIBL.extend([0]*48)
        data_SICL.extend([0]*48)

        # Idle
        data_NCHG.extend([1]*56)
        data_CH.extend([0]*56)
        data_LAT.extend([0]*56)
        data_CK.extend([0]*56)
        data_SIBL.extend([0]*56)
        data_SICL.extend([0]*56)

        # Data block 2
        for i in range(32):
            data_NCHG.extend([1]*4)
            data_CH.extend([0]*4)
            data_LAT.extend([0]*4)
            data_CK.extend([1]*2)
            if (2*i) in nozzles_black:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([1,1,0])
            else:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([0,0,0])
            data_CK.extend([0]*2)
            if (2*i)+1 in nozzles_black:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([1,1,0])
            else:
                data_SIBL = data_SIBL[0:-1]
                data_SIBL.extend([0,0,0])
            data_SICL.extend([0]*4)

        # Idle
        data_NCHG.extend([1]*151)
        data_CH.extend([0]*151)
        data_LAT.extend([0]*151)
        data_CK.extend([0]*151)
        data_SIBL.extend([0]*151)
        data_SICL.extend([0]*151)

        #Fourth pulse
        data_NCHG.extend([0]*48)
        data_CH.extend([0]*24 + [1]*12 + [0]*12)
        data_LAT.extend([0]*48)
        data_CK.extend([0]*48)
        data_SIBL.extend([0]*48)
        data_SICL.extend([0]*48)

        # Idle
        data_NCHG.extend([1]*27)
        data_CH.extend([0]*27)
        data_LAT.extend([0]*27)
        data_CK.extend([0]*27)
        data_SIBL.extend([0]*27)
        data_SICL.extend([0]*27)

        # Quality block
        for j in range(16):
            data_NCHG.extend([1]*4)
            data_CH.extend([0]*4)
            data_LAT.extend([0]*4)
            data_CK.extend([1, 1, 0, 0])
            data_SIBL.extend([1]*4)
            data_SICL.extend([1]*4)

        data_NCHG.extend([1]*1)
        data_CH.extend([0]*1)
        data_LAT.extend([0]*1)
        data_CK.extend([0]*1)
        data_SIBL.extend([0]*1)
        data_SICL.extend([0]*1)


        return self._tuple_to_word_list((data_NCHG, data_CH, data_LAT, data_CK, data_SIBL, data_SICL))


    def get_sequence(self,
                     nozzles_black=[], nozzles_yellow=[],
                     nozzles_cyan=[], nozzles_magenta=[],
                     size='medium', quality='VSD2', plot=False):
        nozzles_black = list(nozzles_black)
        nozzles_cyan = list(nozzles_cyan)
        nozzles_magenta = list(nozzles_magenta)
        nozzles_yellow = list(nozzles_yellow)

        data_clock = [0,0]
        data_black = [0]
        data_color = [0]
        data_ch = [0]

        # PHASE 1: first selection of nozzles
        # Init clock and empty data lines
        for i in range(64):
            data_clock.extend([0,1,1,0])
        if size == 'large' or size == 'medium':
            tmp_data = self._get_selection_block(nozzles_black, nozzles_cyan, nozzles_yellow, nozzles_magenta)
            data_black.extend(tmp_data[0])
            data_color.extend(tmp_data[1])
        else:
            data_clock.append(0)
            data_black.extend([0]*256)
            data_color.extend([0]*256)

        # PHASE 2: insert waiting period
        for i in range(230):
            data_clock.append(0)
            data_black.append(0)
            data_color.append(0)

        # PHASE 3: second selection of nozzles
        for i in range(64):
            data_clock.extend([0,1,1,0])
        if size == 'large' or size == 'small':
            tmp_data = self._get_selection_block(nozzles_black, nozzles_cyan, nozzles_yellow, nozzles_magenta)
            data_black.extend(tmp_data[0])
            data_color.extend(tmp_data[1])
        else:
            data_black.extend([0]*256)
            data_color.extend([0]*256)

        # PHASE 4: insert waiting period
        for i in range(230):
            data_clock.append(0)
            data_black.append(0)
            data_color.append(0)

        # Phase 5: quality selection pulses
        for i in range(16):
            data_clock.extend([0,1,1,0])
        tmp_data = self._get_quality_sequence(quality)
        data_black.extend(tmp_data)
        data_color.extend(tmp_data)

        # Phase 6: append zeroes for good measure
        data_clock.append(0)
        data_black.append(0)
        data_black.append(0)
        data_color.append(0)
        data_color.append(0)

        data_nchg = [0]*len(data_clock)
        data_ch = [0]*len(data_clock)
        data_lat = [0]*len(data_clock)


        if plot == True:
            self.fig, axarr = plt.subplots(3, 1, sharex=True)
            axarr[0].plot(range(len(data_clock)), data_clock, drawstyle='steps-pre')
            axarr[1].plot(range(len(data_black)), data_black, drawstyle='steps-pre')
            axarr[2].plot(range(len(data_color)), data_color, drawstyle='steps-pre')
            plt.show()

        return self._tuple_to_word_list((data_nchg, data_ch, data_lat, data_clock, data_black, data_color))
