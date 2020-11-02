groups = [
    "vk.com/rambler",
    "vk.com/ramblermail",
    "vk.com/horoscopesrambler",
    "vk.com/championat",
    "vk.com/championat.auto",
    "vk.com/championat_cybersport",
    "vk.com/livejournal",
    "vk.com/afisha",
]

access_token = '914bdeb3aa6078c1ce41630a4fd13c6b1cb1065296452cb88c6d851065b87c043635d68b3ef5e7f25e10e'

group_table_name = 'vk_group'
group_info_table_name = 'vk_group_info'

group_table_fields = ["group_name VARCHAR(256) NOT NULL",
                      "group_id INTEGER PRIMARY KEY"
                      ]

group_info_table_fields = ["id integer PRIMARY KEY",
                           "user_count INTEGER",
                           "group_id INTEGER",
                           "FOREIGN KEY (group_id) REFERENCES vk_group (group_id)"
                           ]