groups = [
    "vk.com/rambler",
    "vk.com/ramblermail",
    "vk.com/horoscopesrambler",
    "vk.com/championat",
    "vk.com/championat.auto",
    "vk.com/championat_cybersport",
    "vk.com/livejournal",
    "vk.com/afisha"
]

access_token = '72b65cbd1ea90b97cc8c0b37ca6470b9019c0f8957d9918401301ac9d0b6013daa8bdfccbb9e120208d9a'

group_table_name = 'vk_group'
# group_info_table_name = 'vk_group_info'

group_table_fields = ["group_name VARCHAR(256) NOT NULL",
                      "group_id INTEGER PRIMARY KEY",
                      "user_count INTEGER"
                      ]

# group_info_table_fields = ["id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL",
#                            "user_count INTEGER",
#                            "group_id INTEGER UNIQUE",
#                            "FOREIGN KEY (group_id) REFERENCES vk_group (group_id)"
#                            ]
