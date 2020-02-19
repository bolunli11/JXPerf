#BEGIN_LEGAL
#
#Copyright (c) 2019 Intel Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  
#END_LEGAL
import genutil

def read_file(fn):
    lines = open(fn,'r').readlines()
    lines = map(genutil.no_comments, lines)
    lines = list(filter(genutil.blank_line, lines))
    d = {} # isa-set to list of cpuid records
    for line in lines:
        wrds = line.split(':')
        isa_set = wrds[0].strip()
        cpuid_bits = wrds[1].upper().split()
        if isa_set in d:
            msg = "Duplicate cpuid definition for isa set. isa-set={} old={} new={}"
            genutil.die(msg.format(isa_set, d[isa_set], cpuid_bits))
        d[isa_set] = cpuid_bits
    return d