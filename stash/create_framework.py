

all_tags = ['ADD',
            # 'ALN',
            'AST',
            # 'BRK',
            # 'BRL',
            # 'CEL',
            # 'COL',
            'DEL',
            # 'DTA',
            'DTE',
            # 'END',
            'ENG',
            'HDR',
            'HL1',
            'HL4',
            'ITM',
            'LST',
            'MET',
            # 'MTA',
            # 'NED',
            'NPR',
            'NTE',
            'ORG',
            # 'PRA',
            'PRT',
            'REF',
            'RID',
            # 'ROW',
            'RTL',
            'SCN',
            'SCP',
            # 'SEC',
            'SPT',
            'SRF',
            'STL',
            # 'STS',
            # 'STY',
            'SUB',
            'TAB',
            'TAI',
            # 'TDA',
            'TST',
            'TTL',
            'TXT',
            'URL',
            # 'WBK'
            ]


def write_css_to_file(tag_list:list=all_tags, output_path:str='./stash/output_css.txt') -> None:
    with open(output_path, 'w') as file:
        for tag in tag_list:
            file.write(f'.display_{tag} {{\n\n}}\n\n')

write_css_to_file()