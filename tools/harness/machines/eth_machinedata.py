##########################################################################
# Copyright (c) 2009, 2016, ETH Zurich.
# All rights reserved.
#
# This file is distributed under the terms in the attached LICENSE file.
# If you do not find this file, copies can be found by writing to:
# ETH Zurich D-INFK, Universitaetstr 6, CH-8092 Zurich. Attn: Systems Group.
##########################################################################

machines = dict({
    'nos4'   : {'ncores'      : 4,
                'machine_name' : 'nos4',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 2,
                'perfcount_type': 'amd0f',
                'tickrate'    : 2800},
    'nos5'   : {'ncores'      : 4,
                'machine_name' : 'nos5',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 2,
                'perfcount_type': 'amd0f',
                'tickrate'    : 2800},
    'nos6'   : {'ncores'      : 4,
                'machine_name' : 'nos6',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 2,
                'perfcount_type': 'amd0f',
                'tickrate'    : 2800},

    'sbrinz1': {'ncores'      : 16,
                'machine_name' : 'sbrinz1',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 4,
                'perfcount_type': 'amd10',
                'tickrate'    : 2500,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                },
    'sbrinz2': {'ncores'      : 16,
                'machine_name' : 'sbrinz2',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 4,
                'perfcount_type': 'amd10',
                'tickrate'    : 2500,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                },

    'gruyere': {'ncores'      : 32,
                'machine_name' : 'gruyere',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 4,
                'perfcount_type': 'amd10',
                'tickrate'    : 2000,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                },

    'ziger1':  {'ncores'      : 24,
                'machine_name' : 'ziger1',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 6,
                'perfcount_type': 'amd10',
                'tickrate'    : 2400.367},
    'ziger2':  {'ncores'      : 24,
                'machine_name' : 'ziger2',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 6,
                'perfcount_type': 'amd10',
                'tickrate'    : 2400.367},

    'tomme1':  {'ncores'      : 16,
                'machine_name' : 'tomme1',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 8,
                'perfcount_type': 'intel',
                'tickrate'    : 2270,
                'boot_timeout': 360,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                'kernel_args' : ['serial=0x2f8']},
    'tomme2':  {'ncores'      : 16,
                'machine_name' : 'tomme2',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 8,
                'perfcount_type': 'intel',
                'tickrate'    : 2270,
                'boot_timeout': 360,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                'kernel_args' : ['serial=0x2f8']},

    'vacherin':{'ncores'      : 4,
                'machine_name' : 'vacherin',
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket': 4,
                'perfcount_type': 'intel',
                'tickrate'    : 3400,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                },

    'appenzeller': {'ncores'      : 48,
                    'machine_name' : 'appenzeller',
                    'bootarch' : 'x86_64',
                    'buildarchs' : ['x86_64'],
                    'cores_per_socket': 12,
                    'perfcount_type': 'amd10',
                    'tickrate'    : 2200,
                    'boot_timeout': 360,
                    'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                    },

    'gottardo': {'ncores'      : 32,
                 'machine_name' : 'gottardo',
                 'bootarch' : 'x86_64',
                 'buildarchs' : ['x86_64'],
                 'cores_per_socket': 16,
                 'perfcount_type': 'intel',
                 'tickrate'    : 1870,
                 'boot_timeout': 360},

    'babybel1': {'ncores'          : 20,
                'machine_name'    : 'babybel1',
                'bootarch'        : 'x86_64',
                'buildarchs'      : ['x86_64', 'k1om'],
                'cores_per_socket': 10,
                'perfcount_type'  : 'intel',
                'tickrate'        : 2500,
                'boot_timeout'    : 360,
                'xphi_ncores'     : 57,
                'xphi_ncards'     : 2,
                'xphi_tickrate'   : 1140,
                'xphi_ram_gb'     : 6,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                'eth0'            : (4, 0, 0),
                },

    'babybel2': {'ncores'          : 20,
                'machine_name'    : 'babybel2',
                'bootarch'        : 'x86_64',
                'buildarchs'      : ['x86_64', 'k1om'],
                'cores_per_socket': 10,
                'perfcount_type'  : 'intel',
                'tickrate'        : 2500,
                'boot_timeout'    : 360,
                'xphi_ncores'     : 57,
                'xphi_ncards'     : 2,
                'xphi_tickrate'   : 1140,
                'xphi_ram_gb'     : 6,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                'eth0'            : (4, 0, 0),
                },

    'babybel3': {'ncores'          : 20,
                'machine_name'    : 'babybel3',
                'bootarch'        : 'x86_64',
                'buildarchs'      : ['x86_64', 'k1om'],
                'cores_per_socket': 10,
                'perfcount_type'  : 'intel',
                'tickrate'        : 2500,
                'boot_timeout'    : 360,
                'xphi_ncores'     : 57,
                'xphi_ncards'     : 2,
                'xphi_tickrate'   : 1140,
                'xphi_ram_gb'     : 6,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                'eth0'            : (4, 0, 0),
                },

    'babybel4': {'ncores'          : 20,
                'machine_name'    : 'babybel4',
                'bootarch'        : 'x86_64',
                'buildarchs'      : ['x86_64', 'k1om'],
                'cores_per_socket': 10,
                'perfcount_type'  : 'intel',
                'tickrate'        : 2500,
                'boot_timeout'    : 360,
                'xphi_ncores'     : 57,
                'xphi_ncards'     : 2,
                'xphi_tickrate'   : 1140,
                'xphi_ram_gb'     : 6,
                'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                'eth0'            : (4, 0, 0),
                },

   'tilsiter1': {'ncores'          : 2,
                 'machine_name'    : 'tilsiter1',
                 'bootarch'        : 'x86_64',
                 'buildarchs'      : ['x86_64'],
                 'cores_per_socket': 2,
                 'perfcount_type'  : 'intel',
                 'tickrate'        : 2500,
                 'boot_timeout'    : 120,
                 'pci_args'        : [ "skb_bridge_program=bridge_bios" ],
                 },

    'nos4-32'   : {'ncores'      : 4,
                   'machine_name' : 'nos4',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 2,
                   'perfcount_type': 'amd0f',
                   'tickrate'    : 2800},
    'nos5-32'   : {'ncores'      : 4,
                   'machine_name' : 'nos5',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 2,
                   'perfcount_type': 'amd0f',
                   'tickrate'    : 2800},
    'nos6-32'   : {'ncores'      : 4,
                   'machine_name' : 'nos6',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 2,
                   'perfcount_type': 'amd0f',
                   'tickrate'    : 2800},

    'sbrinz1-32': {'ncores'      : 16,
                   'machine_name' : 'sbrinz1',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 4,
                   'perfcount_type': 'amd10',
                   'tickrate'    : 2500},
    'sbrinz2-32': {'ncores'      : 16,
                   'machine_name' : 'sbrinz2',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 4,
                   'perfcount_type': 'amd10',
                   'tickrate'    : 2500},

    'gruyere-32': {'ncores'      : 32,
                   'machine_name' : 'gruyere',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 4,
                   'perfcount_type': 'amd10',
                   'tickrate'    : 2000},

    'ziger1-32':  {'ncores'      : 24,
                   'machine_name' : 'ziger1',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 6,
                   'perfcount_type': 'amd10',
                   'tickrate'    : 2400.367},
    'ziger2-32':  {'ncores'      : 24,
                   'machine_name' : 'ziger2',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 6,
                   'perfcount_type': 'amd10',
                   'tickrate'    : 2400.367},

    'tomme1-32':  {'ncores'      : 16,
                   'machine_name' : 'tomme1',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 8,
                   'perfcount_type': 'intel',
                   'tickrate'    : 2270,
                   'boot_timeout': 360,
                   'kernel_args' : ['serial=0x2f8']},
    'tomme2-32':  {'ncores'      : 16,
                   'machine_name' : 'tomme2',
                   'bootarch' : 'x86_32',
                   'buildarchs' : ['x86_64', 'x86_32'],
                   'cores_per_socket': 8,
                   'perfcount_type': 'intel',
                   'tickrate'    : 2270,
                   'boot_timeout': 360,
                   'kernel_args' : ['serial=0x2f8']},

    'appenzeller-32': {'ncores'      : 48,
                       'machine_name' : 'appenzeller',
                       'bootarch' : 'x86_32',
                       'buildarchs' : ['x86_64', 'x86_32'],
                       'cores_per_socket': 12,
                       'perfcount_type': 'amd10',
                       'tickrate'    : 2200,
                       'boot_timeout': 360},

    'gottardo-32': {'ncores'      : 32,
                    'machine_name' : 'gottardo',
                    'bootarch' : 'x86_32',
                    'buildarchs' : ['x86_64', 'x86_32'],
                    'cores_per_socket': 16,
                    'perfcount_type': 'intel',
                    'tickrate'    : 1870,
                    'boot_timeout': 360},

    'vacherin-32': {'ncores'      : 4,
                'machine_name' : 'vacherin',
                'bootarch' : 'x86_32',
                'buildarchs' : ['x86_64', 'x86_32'],
                'cores_per_socket': 4,
                'perfcount_type': 'intel',
                'tickrate'    : 3400},

    'babybel1-32': {'ncores'          : 20,
                'machine_name'    : 'babybel1',
                'bootarch'        : 'x86_32',
                'buildarchs'      : ['x86_64', 'x86_32'],
                'cores_per_socket': 10,
                'perfcount_type'  : 'intel',
                'tickrate'        : 2500,
                'boot_timeout'    : 360},

    'babybel2-32': {'ncores'          : 20,
                'machine_name'    : 'babybel2',
                'bootarch'        : 'x86_32',
                'buildarchs'      : ['x86_64', 'x86_32'],
                'cores_per_socket': 10,
                'perfcount_type'  : 'intel',
                'tickrate'        : 2500,
                'boot_timeout'    : 360},

    'babybel3-32': {'ncores'          : 20,
                   'machine_name'    : 'babybel3',
                   'bootarch'        : 'x86_32',
                   'buildarchs'      : ['x86_64', 'x86_32'],
                   'cores_per_socket': 10,
                   'perfcount_type'  : 'intel',
                   'tickrate'        : 2500,
                   'boot_timeout'    : 360},
    'babybel4-32': {'ncores'          : 20,
                   'machine_name'    : 'babybel4',
                   'bootarch'        : 'x86_32',
                   'buildarchs'      : ['x86_64', 'x86_32'],
                   'cores_per_socket': 10,
                   'perfcount_type'  : 'intel',
                   'tickrate'        : 2500,
                   'boot_timeout'    : 360},
    'xeon_phi_1': {'ncores'          : 64,
                   'nphi'            : 2,
                   'host_ncores'     : 20,
                   'machine_name'    : 'babybel1',
                   'bootarch'        : 'x86_64',
                   'buildarchs'      : ['k1om', 'x86_64'],
                   'cores_per_socket': 10,
                   'perfcount_type'  : 'intel',
                   'tickrate'        : 1140,
                   'host_tickrate'   : 2500,
                   'boot_timeout'    : 360},
    'xeon_phi_2': {'ncores'          : 64,
                   'nphi'            : 2,
                   'host_ncores'     : 20,
                   'machine_name'    : 'babybel2',
                   'bootarch'        : 'x86_64',
                   'buildarchs'      : ['k1om', 'x86_64'],
                   'cores_per_socket': 10,
                   'perfcount_type'  : 'intel',
                   'tickrate'        : 1140,
                   'host_tickrate'   : 2500,
                   'boot_timeout'    : 360},
    'xeon_phi_3': {'ncores'          : 64,
                   'nphi'            : 2,
                   'host_ncores'     : 20,
                   'machine_name'    : 'babybel3',
                   'bootarch'        : 'x86_64',
                   'buildarchs'      : ['k1om', 'x86_64'],
                   'cores_per_socket': 10,
                   'perfcount_type'  : 'intel',
                   'tickrate'        : 1140,
                   'host_tickrate'   : 2500,
                   'boot_timeout'    : 360},
    'xeon_phi_4': {'ncores'          : 64,
                   'nphi'            : 2,
                   'host_ncores'     : 20,
                   'machine_name'    : 'babybel4',
                   'bootarch'        : 'x86_64',
                   'buildarchs'      : ['k1om', 'x86_64'],
                   'cores_per_socket': 10,
                   'perfcount_type'  : 'intel',
                   'tickrate'        : 1140,
                   'host_tickrate'   : 2500,
                   'boot_timeout'    : 360},

    'danablu1': {'ncores'      : 8,
                 'machine_name' : 'danablu1',
                 'bootarch' : 'armv8',
                 'buildarchs' : ['armv8'],
                 'cores_per_socket': 8,
                 'perfcount_type': 'arm',
                 'tickrate'    : 2400,
                 'boot_timeout': 360,
                 'platform': 'apm88xxxx',
                 'serial_binary': 'serial_kernel',
                 'boot_driver' : 'boot_armv8_generic'},

    'gorgonzola1': {'ncores'      : 48,
                    'machine_name' : 'gorgonzola1',
                    'bootarch' : 'armv8',
                    'buildarchs' : ['armv8'],
                    'cores_per_socket': 48,
                    'perfcount_type': 'arm',
                    'tickrate'    : 1950,
                    'boot_timeout': 360,
                    'platform': 'cn88xx',
                    'serial_binary': 'serial_kernel',
                    'boot_driver' : 'boot_armv8_generic'},
    'gorgonzola2': {'ncores'      : 48,
                    'machine_name' : 'gorgonzola1',
                    'bootarch' : 'armv8',
                    'buildarchs' : ['armv8'],
                    'cores_per_socket': 48,
                    'perfcount_type': 'arm',
                    'tickrate'    : 1950,
                    'boot_timeout': 360,
                    'platform': 'cn88xx',
                    'serial_binary': 'serial_kernel',
                    'boot_driver' : 'boot_armv8_generic'},
    'roquefort':    {'ncores'      : 96,
                     'machine_name' : 'roquefort',
                     'bootarch' : 'armv8',
                     'buildarchs' : ['armv8'],
                     'cores_per_socket': 48,
                     'perfcount_type': 'arm',
                     'tickrate'    : 1950,
                     'boot_timeout': 360,
                     'platform': 'cn88xx',
                     'serial_binary': 'serial_kernel',
                     'boot_driver' : 'boot_armv8_generic'},


    # SK: For Python 2.7
    # }.items() + {
    #     'brie%s' % b: {
    #         'ncores' : 4,
    #         'machine_name' : ('brie%s' % b),
    #         'bootarch' : 'x86_64',
    #         'buildarchs' : ['x86_64', 'x86_32'],
    #         'cores_per_socket' : 2,
    #         'tickrate' : 2193,
    #         'boot_timeout' : 360,
    #         } for b in range(1, 17) if b != 11 }.items()

    # SK: For Python 2.6, which is what the current toolchain is ATM
    }.items() +
        dict(('brie%s' % b, {
                'ncores' : 4,
                'machine_name' : ('brie%s' % b),
                'bootarch' : 'x86_64',
                'buildarchs' : ['x86_64'],
                'cores_per_socket' : 2,
                'tickrate' : 2193,
                'perfcount_type': 'amd0f',
                'boot_timeout' : 360,
                }) for b in range(1, 17) if b != 11
        ).items() +
        dict(('brie%s-32' % b, {
                'ncores' : 4,
                'machine_name' : ('brie%s' % b),
                'bootarch' : 'x86_32',
                'buildarchs' : ['x86_64', 'x86_32'],
                'cores_per_socket' : 2,
                'tickrate' : 2193,
                'perfcount_type': 'amd0f',
                'boot_timeout' : 360,
                }) for b in range(1, 17) if b != 11
        ).items()
)

pandaboards = dict({
    'panda1':     {'ncores'          : 2,
                   'nphi'            : 0,
                   'host_ncores'     : 20,
                   'machine_name'    : 'panda1',
                   'bootarch'        : 'armv7',
                   'platform'        : 'omap44xx',
                   'buildarchs'      : ['armv7'],
                   'cores_per_socket': 2,
                   'perfcount_type'  : 'arm',
                   'tickrate'        : 1000, # XXX ?
                   'host_tickrate'   : 2500,
                   'boot_timeout'    : 360},
    'panda2':     {'ncores'          : 2,
                   'nphi'            : 0,
                   'host_ncores'     : 20,
                   'machine_name'    : 'panda2',
                   'bootarch'        : 'armv7',
                   'platform'        : 'omap44xx',
                   'buildarchs'      : ['armv7'],
                   'cores_per_socket': 2,
                   'perfcount_type'  : 'arm',
                   'tickrate'        : 1000, # XXX ?
                   'host_tickrate'   : 2500,
                   'boot_timeout'    : 360},
    'panda3':     {'ncores'          : 2,
                   'nphi'            : 0,
                   'host_ncores'     : 20,
                   'machine_name'    : 'panda3',
                   'bootarch'        : 'armv7',
                   'platform'        : 'omap44xx',
                   'buildarchs'      : ['armv7'],
                   'cores_per_socket': 2,
                   'perfcount_type'  : 'arm',
                   'tickrate'        : 1000, # XXX ?
                   'host_tickrate'   : 2500,
                   'boot_timeout'    : 360},
})
