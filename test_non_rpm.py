"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Description: Test non-rpm executable files in the system.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	In this test all the files in the system will listed. If execuable
#   file is belong to any rpm then it is valid file otherwise it is
#	not a valid file and test will be exited.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Author: Amol Kahat <akahat@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2016 Red Hat, Inc. All rights reserved.
#
#   This copyrighted material is made available to anyone wishing
#   to use, modify, copy, or redistribute it subject to the terms
#   and conditions of the GNU General Public License version 2.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE. See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free
#   Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#   Boston, MA 02110-1301, USA.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import os
import unittest

from .testutils import system


class Test_rpm_executable(unittest.TestCase):
    """
    This class include the tests checking valid rpm files.
    """

    def test_list_files_and_test(self):
        """
        This function is listing all the files in the system and
        test it belong to any rpm or not.
        """
        def is_executable(file_path):
            return os.path.isfile(file_path) and os.access(file_path, os.X_OK)

        exe_file = []
        out, err, retcode = system("rpm -qal")
        files = out.decode("utf-8").split("\n")
        [exe_file.append(i) for i in files if is_executable(i)]
        exceptions = ['rpmostree-postprocess-treecompose-post.sh']

        for i in exe_file:
            if i not in present:
                output, error, rcode = system('rpm -qf {}'.format(i))
                self.assertEqual(rcode, 0)

if __name__ == '__main__':
    unittest. main()
