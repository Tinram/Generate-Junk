#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Junk data generator using multiprocessing and avoiding GIL. """


import multiprocessing as mp
import random
import string


class GenerateJunk(object):

    """
        Generate ASCII strings using multiprocessing across CPU threads.

        Python Version     3.6.9
        Author             Martin Latter, 13/12/2019
        Author             Sebastian Raschka (multiprocessing pattern)
        Version            0.03
    """


    # output queue
    output = mp.Queue()

    junk = ''
    list_output = []
    junk_len = 8192 # string length per thread
    cores = mp.cpu_count()
    random.seed()


    def __init__(self):

        """ Initialise and execute methods. """

        self.list_output = self.generate()


    def rnd_string(self, length, output):

        """ Create ASCII string """

        self.junk = ''.join(
            random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(length)
        )

        self.output.put(self.junk)


    def generate(self):

        """
            Generate processes creating random strings.
        """

        # setup list of processes to run
        processes = [mp.Process(target=self.rnd_string, args=(self.junk_len, self.output)) for x in range(self.cores)]

        for psi in processes:
            psi.start()

        for psi in processes:
            psi.join()

        # get process results from the output queue
        results = [self.output.get() for psi in processes]

        return results


    def emit(self):

        """
            Public emitter.
        """

        return self.list_output

# end class


def main():

    """ run """

    GenerateJunk().emit()


if __name__ == '__main__':

    main()
