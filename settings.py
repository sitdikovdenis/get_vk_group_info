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

access_token = '1c4238671ef9101e609c01b48a4f9d2b8420ace05b4ce1182b6e3a4a1d9a2d74e7a7c3f980d94a06c9d41'

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
