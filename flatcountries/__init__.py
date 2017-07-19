__author__ = 'Daniel Kuruc'
__date__ = '2017/07/19'
__email__ = 'dnk@dnk.net.pl'
__license__ = 'MIT'
__version__ = '0.0.1'

AFRICA = (
    'AO',
    'BF',
    'BI',
    'BJ',
    'BW',
    'CD',
    'CF',
    'CG',
    'CI',
    'CM',
    'CV',
    'DJ',
    'DZ',
    'EG',
    'EH',
    'ER',
    'ET',
    'GA',
    'GH',
    'GM',
    'GN',
    'GQ',
    'GW',
    'KE',
    'KM',
    'LR',
    'LS',
    'LY',
    'MA',
    'MG',
    'ML',
    'MR',
    'MU',
    'MW',
    'MZ',
    'NA',
    'NE',
    'NG',
    'RE',
    'RW',
    'SC',
    'SD',
    'SH',
    'SL',
    'SN',
    'SO',
    'SS',
    'ST',
    'SZ',
    'TD',
    'TG',
    'TN',
    'TZ',
    'UG',
    'YT',
    'ZA',
    'ZM',
    'ZW',
)

ANTARCTICA = (
    'AQ',
    'BV',
    'GS',
    'HM',
    'TF',
)

ASIA = (
    'AE',
    'AF',
    'AM',
    'AZ',
    'BD',
    'BH',
    'BN',
    'BT',
    'CC',
    'CN',
    'CX',
    'GE',
    'HK',
    'ID',
    'IL',
    'IN',
    'IO',
    'IQ',
    'IR',
    'JO',
    'JP',
    'KG',
    'KH',
    'KP',
    'KR',
    'KW',
    'KZ',
    'LA',
    'LB',
    'LK',
    'MM',
    'MN',
    'MO',
    'MV',
    'MY',
    'NP',
    'OM',
    'PH',
    'PK',
    'PS',
    'QA',
    'SA',
    'SG',
    'SY',
    'TH',
    'TJ',
    'TM',
    'TR',
    'TW',
    'UZ',
    'VN',
    'YE',
)

EUROPE = (
    'AD',
    'AL',
    'AT',
    'AX',
    'BA',
    'BE',
    'BG',
    'BY',
    'CH',
    'CY',
    'CZ',
    'DE',
    'DK',
    'EE',
    'ES',
    'FI',
    'FO',
    'FR',
    'GB',
    'GG',
    'GI',
    'GR',
    'HR',
    'HU',
    'IE',
    'IM',
    'IS',
    'IT',
    'JE',
    'LI',
    'LT',
    'LU',
    'LV',
    'MC',
    'MD',
    'ME',
    'MK',
    'MT',
    'NL',
    'NO',
    'PL',
    'PT',
    'RO',
    'RS',
    'RU',
    'SE',
    'SI',
    'SJ',
    'SK',
    'SM',
    'UA',
    'VA',
    'XK',
)

EUROPEAN_UNION = (
    'AT',
    'BE',
    'BG',
    'CY',
    'CZ',
    'DK',
    'EE',
    'FI',
    'FR',
    'DE',
    'GR',
    'HU',
    'HR',
    'IE',
    'IT',
    'LV',
    'LT',
    'LU',
    'MT',
    'NL',
    'PL',
    'PT',
    'RO',
    'SK',
    'SI',
    'ES',
    'SE',
    'GB',
)

NORTH_AMERICA = (
    'AG',
    'AI',
    'AW',
    'BB',
    'BL',
    'BM',
    'BQ',
    'BS',
    'BZ',
    'CA',
    'CR',
    'CU',
    'CW',
    'DM',
    'DO',
    'GD',
    'GL',
    'GP',
    'GT',
    'HN',
    'HT',
    'JM',
    'KN',
    'KY',
    'LC',
    'MF',
    'MQ',
    'MS',
    'MX',
    'NI',
    'PA',
    'PM',
    'PR',
    'SV',
    'SX',
    'TC',
    'TT',
    'US',
    'VC',
    'VG',
    'VI',
)

OCEANIA = (
    'AS',
    'AU',
    'CK',
    'FJ',
    'FM',
    'GU',
    'KI',
    'MH',
    'MP',
    'NC',
    'NF',
    'NR',
    'NU',
    'NZ',
    'PF',
    'PG',
    'PN',
    'PW',
    'SB',
    'TK',
    'TL',
    'TO',
    'TV',
    'UM',
    'VU',
    'WF',
    'WS',
)

SOUTH_AMERICA = (
    'AR',
    'BO',
    'BR',
    'CL',
    'CO',
    'EC',
    'FK',
    'GF',
    'GY',
    'PE',
    'PY',
    'SR',
    'UY',
    'VE',

)

NON_EU = (
    AFRICA +
    ANTARCTICA +
    ASIA +
    NORTH_AMERICA +
    OCEANIA +
    SOUTH_AMERICA
)

AMERICAS = (
    NORTH_AMERICA +
    SOUTH_AMERICA
)

COUNTRIES = (
    AFRICA +
    ANTARCTICA +
    ASIA +
    EUROPE +
    NORTH_AMERICA +
    OCEANIA +
    SOUTH_AMERICA
)


def is_africa(country_code):
    return country_code in AFRICA


def is_antarctica(country_code):
    return country_code in ANTARCTICA


def is_asia(country_code):
    return country_code in ASIA


def is_europe(country_code):
    return country_code in EUROPE


def is_european_union(country_code):
    return country_code in EUROPEAN_UNION


def is_north_america(country_code):
    return country_code in NORTH_AMERICA


def is_not_europe(country_code):
    return country_code in NON_EU


def is_oceania(country_code):
    return country_code in OCEANIA


def is_south_america(country_code):
    return country_code in SOUTH_AMERICA
