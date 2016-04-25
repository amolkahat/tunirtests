"""
   This document is used to test
   Non RPM files in the system.
"""

import os
import unittest

from .testutils import system

class TestRPMExecutable(unittest.TestCase):
    """
    This class include test cases for testing non rpm file.
    """

    def test_check_binarys(self):
        """
        This program test the executable files which belongs to rpm package.
        """
        present = ['rpmostree-postprocess-treecompose-post.sh']
        out, err, retcode = system("echo $PATH")
        path = out.decode('utf-8').split(':')
        for singlepath in path:
            for root, dirs, files in os.walk(singlepath):
                if files:
                    for i in files:
                        if i not in present:
                            rpm = 'rpm -qf ' + os.path.join(singlepath, i)
                            output, error, rcode = system(rpm)
                            self.assertEqual(rcode, 0)

if __name__ == '__main__':
    unittest.main()
