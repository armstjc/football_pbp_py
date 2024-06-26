"""
- Creation Date: 08/16/2023 07:28 PM EST
- Last Updated: 06/04/2024 01:15 PM EDT
- Author: Joseph Armstrong (armstrongjoseph08@gmail.com)
- File Name: ./core/database/create_sdv_pbp_db.py
- Purpose: Creates a database that can be used for this application.
"""
###############################################################################

import logging
from os import makedirs
from os.path import expanduser
from sqlite3 import connect as sqlite_connect

# import zoneinfo


class SqliteSampleFiles:
    """
    Houses the base SQL scripts for this application
    to use for building out SQLite3 databases.
    """

    def iso_nations() -> str:
        """
        Returns a SQLite3 script that creates a table to hold ISO country data.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a table to hold ISO country data.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS iso_nations(
            "nation_name"                 TEXT NOT NULL
            ,"nation_iso_alpha_2"         TEXT NOT NULL
            ,"nation_iso_alpha_3"         TEXT NOT NULL PRIMARY KEY
            ,"nation_iso_numeric"         INTEGER  NOT NULL
            ,"iso_3166_2"                 TEXT NOT NULL
            ,"region"                     TEXT
            ,"subregion"                  TEXT
            ,"intermediate_region"        TEXT
            ,"region_code"                INTEGER
            ,"subregion_code"             INTEGER
            ,"intermediate_region_code"   INTEGER
        );

        INSERT INTO iso_nations(
            nation_name,
            nation_iso_alpha_2,
            nation_iso_alpha_3,
            nation_iso_numeric,
            iso_3166_2,
            region,
            subregion,
            intermediate_region,
            region_code,
            subregion_code,
            intermediate_region_code)
        VALUES
            ('Afghanistan','AF','AFG',004,'ISO 3166-2:AF',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Åland Islands','AX','ALA',248,'ISO 3166-2:AX',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Albania','AL','ALB',008,'ISO 3166-2:AL',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Algeria','DZ','DZA',012,'ISO 3166-2:DZ',
                'Africa','Northern Africa',NULL,002,015,NULL)
            ,('American Samoa','AS','ASM',016,'ISO 3166-2:AS',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('Andorra','AD','AND',020,'ISO 3166-2:AD',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Angola','AO','AGO',024,'ISO 3166-2:AO',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Anguilla','AI','AIA',660,'ISO 3166-2:AI',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Antarctica','AQ','ATA',010,'ISO 3166-2:AQ',
                NULL,NULL,NULL,NULL,NULL,NULL)
            ,('Antigua and Barbuda','AG','ATG',028,'ISO 3166-2:AG',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Argentina','AR','ARG',032,'ISO 3166-2:AR',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Armenia','AM','ARM',051,'ISO 3166-2:AM',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Aruba','AW','ABW',533,'ISO 3166-2:AW',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Australia','AU','AUS',036,'ISO 3166-2:AU',
                'Oceania','Australia and New Zealand',NULL,009,053,NULL)
            ,('Austria','AT','AUT',040,'ISO 3166-2:AT',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('Azerbaijan','AZ','AZE',031,'ISO 3166-2:AZ',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Bahamas','BS','BHS',044,'ISO 3166-2:BS',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Bahrain','BH','BHR',048,'ISO 3166-2:BH',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Bangladesh','BD','BGD',050,'ISO 3166-2:BD',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Barbados','BB','BRB',052,'ISO 3166-2:BB',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Belarus','BY','BLR',112,'ISO 3166-2:BY',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Belgium','BE','BEL',056,'ISO 3166-2:BE',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('Belize','BZ','BLZ',084,'ISO 3166-2:BZ',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Benin','BJ','BEN',204,'ISO 3166-2:BJ',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Bermuda','BM','BMU',060,'ISO 3166-2:BM',
                'Americas','Northern America',NULL,019,021,NULL)
            ,('Bhutan','BT','BTN',064,'ISO 3166-2:BT',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Bolivia (Plurinational State of)',
                'BO','BOL',068,'ISO 3166-2:BO',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Bonaire, Sint Eustatius and Saba',
                'BQ','BES',535,'ISO 3166-2:BQ',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Bosnia and Herzegovina','BA','BIH',070,'ISO 3166-2:BA',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Botswana','BW','BWA',072,'ISO 3166-2:BW',
                'Africa','Sub-Saharan Africa','Southern Africa',002,202,018)
            ,('Bouvet Island','BV','BVT',074,'ISO 3166-2:BV',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Brazil','BR','BRA',076,'ISO 3166-2:BR',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('British Indian Ocean Territory','IO','IOT',086,'ISO 3166-2:IO',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Brunei Darussalam','BN','BRN',096,'ISO 3166-2:BN',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Bulgaria','BG','BGR',100,'ISO 3166-2:BG',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Burkina Faso','BF','BFA',854,'ISO 3166-2:BF',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Burundi','BI','BDI',108,'ISO 3166-2:BI',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Cabo Verde','CV','CPV',132,'ISO 3166-2:CV',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Cambodia','KH','KHM',116,'ISO 3166-2:KH',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Cameroon','CM','CMR',120,'ISO 3166-2:CM',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Canada','CA','CAN',124,'ISO 3166-2:CA',
                'Americas','Northern America',NULL,019,021,NULL)
            ,('Cayman Islands','KY','CYM',136,'ISO 3166-2:KY',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Central African Republic','CF','CAF',140,'ISO 3166-2:CF',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Chad','TD','TCD',148,'ISO 3166-2:TD',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Chile','CL','CHL',152,'ISO 3166-2:CL',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('China','CN','CHN',156,'ISO 3166-2:CN',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Christmas Island','CX','CXR',162,'ISO 3166-2:CX',
                'Oceania','Australia and New Zealand',NULL,009,053,NULL)
            ,('Cocos (Keeling) Islands','CC','CCK',166,'ISO 3166-2:CC',
                'Oceania','Australia and New Zealand',NULL,009,053,NULL)
            ,('Colombia','CO','COL',170,'ISO 3166-2:CO',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Comoros','KM','COM',174,'ISO 3166-2:KM',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Congo','CG','COG',178,'ISO 3166-2:CG',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Congo, Democratic Republic of the',
                'CD','COD',180,'ISO 3166-2:CD',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Cook Islands','CK','COK',184,'ISO 3166-2:CK',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('Costa Rica','CR','CRI',188,'ISO 3166-2:CR',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Côte d''Ivoire','CI','CIV',384,'ISO 3166-2:CI',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Croatia','HR','HRV',191,'ISO 3166-2:HR',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Cuba','CU','CUB',192,'ISO 3166-2:CU',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Curaçao','CW','CUW',531,'ISO 3166-2:CW',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Cyprus','CY','CYP',196,'ISO 3166-2:CY',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Czechia','CZ','CZE',203,'ISO 3166-2:CZ',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Denmark','DK','DNK',208,'ISO 3166-2:DK',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Djibouti','DJ','DJI',262,'ISO 3166-2:DJ',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Dominica','DM','DMA',212,'ISO 3166-2:DM',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Dominican Republic','DO','DOM',214,'ISO 3166-2:DO',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Ecuador','EC','ECU',218,'ISO 3166-2:EC',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Egypt','EG','EGY',818,'ISO 3166-2:EG',
                'Africa','Northern Africa',NULL,002,015,NULL)
            ,('El Salvador','SV','SLV',222,'ISO 3166-2:SV',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Equatorial Guinea','GQ','GNQ',226,'ISO 3166-2:GQ',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Eritrea','ER','ERI',232,'ISO 3166-2:ER',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Estonia','EE','EST',233,'ISO 3166-2:EE',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Eswatini','SZ','SWZ',748,'ISO 3166-2:SZ',
                'Africa','Sub-Saharan Africa','Southern Africa',002,202,018)
            ,('Ethiopia','ET','ETH',231,'ISO 3166-2:ET',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Falkland Islands (Malvinas)','FK','FLK',238,'ISO 3166-2:FK',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Faroe Islands','FO','FRO',234,'ISO 3166-2:FO',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Fiji','FJ','FJI',242,'ISO 3166-2:FJ',
                'Oceania','Melanesia',NULL,009,054,NULL)
            ,('Finland','FI','FIN',246,'ISO 3166-2:FI',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('France','FR','FRA',250,'ISO 3166-2:FR',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('French Guiana','GF','GUF',254,'ISO 3166-2:GF',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('French Polynesia','PF','PYF',258,'ISO 3166-2:PF',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('French Southern Territories','TF','ATF',260,'ISO 3166-2:TF',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Gabon','GA','GAB',266,'ISO 3166-2:GA',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Gambia','GM','GMB',270,'ISO 3166-2:GM',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Georgia','GE','GEO',268,'ISO 3166-2:GE',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Germany','DE','DEU',276,'ISO 3166-2:DE',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('Ghana','GH','GHA',288,'ISO 3166-2:GH',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Gibraltar','GI','GIB',292,'ISO 3166-2:GI',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Greece','GR','GRC',300,'ISO 3166-2:GR',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Greenland','GL','GRL',304,'ISO 3166-2:GL',
                'Americas','Northern America',NULL,019,021,NULL)
            ,('Grenada','GD','GRD',308,'ISO 3166-2:GD',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Guadeloupe','GP','GLP',312,'ISO 3166-2:GP',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Guam','GU','GUM',316,'ISO 3166-2:GU',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Guatemala','GT','GTM',320,'ISO 3166-2:GT',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Guernsey','GG','GGY',831,'ISO 3166-2:GG',
                'Europe','Northern Europe','Channel Islands',150,154,830)
            ,('Guinea','GN','GIN',324,'ISO 3166-2:GN',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Guinea-Bissau','GW','GNB',624,'ISO 3166-2:GW',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Guyana','GY','GUY',328,'ISO 3166-2:GY',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Haiti','HT','HTI',332,'ISO 3166-2:HT',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Heard Island and McDonald Islands',
                'HM','HMD',334,'ISO 3166-2:HM',
                'Oceania','Australia and New Zealand',NULL,009,053,NULL)
            ,('Holy See','VA','VAT',336,'ISO 3166-2:VA',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Honduras','HN','HND',340,'ISO 3166-2:HN',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Hong Kong','HK','HKG',344,'ISO 3166-2:HK',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Hungary','HU','HUN',348,'ISO 3166-2:HU',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Iceland','IS','ISL',352,'ISO 3166-2:IS',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('India','IN','IND',356,'ISO 3166-2:IN',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Indonesia','ID','IDN',360,'ISO 3166-2:ID',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Iran (Islamic Republic of)','IR','IRN',364,'ISO 3166-2:IR',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Iraq','IQ','IRQ',368,'ISO 3166-2:IQ',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Ireland','IE','IRL',372,'ISO 3166-2:IE',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Isle of Man','IM','IMN',833,'ISO 3166-2:IM',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Israel','IL','ISR',376,'ISO 3166-2:IL',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Italy','IT','ITA',380,'ISO 3166-2:IT',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Jamaica','JM','JAM',388,'ISO 3166-2:JM',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Japan','JP','JPN',392,'ISO 3166-2:JP',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Jersey','JE','JEY',832,'ISO 3166-2:JE',
                'Europe','Northern Europe','Channel Islands',150,154,830)
            ,('Jordan','JO','JOR',400,'ISO 3166-2:JO',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Kazakhstan','KZ','KAZ',398,'ISO 3166-2:KZ',
                'Asia','Central Asia',NULL,142,143,NULL)
            ,('Kenya','KE','KEN',404,'ISO 3166-2:KE',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Kiribati','KI','KIR',296,'ISO 3166-2:KI',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Korea (Democratic People''s Republic of)',
                'KP','PRK',408,'ISO 3166-2:KP',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Korea, Republic of','KR','KOR',410,'ISO 3166-2:KR',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Kuwait','KW','KWT',414,'ISO 3166-2:KW',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Kyrgyzstan','KG','KGZ',417,'ISO 3166-2:KG',
                'Asia','Central Asia',NULL,142,143,NULL)
            ,('Lao People''s Democratic Republic',
                'LA','LAO',418,'ISO 3166-2:LA',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Latvia','LV','LVA',428,'ISO 3166-2:LV',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Lebanon','LB','LBN',422,'ISO 3166-2:LB',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Lesotho','LS','LSO',426,'ISO 3166-2:LS',
                'Africa','Sub-Saharan Africa','Southern Africa',002,202,018)
            ,('Liberia','LR','LBR',430,'ISO 3166-2:LR',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Libya','LY','LBY',434,'ISO 3166-2:LY',
                'Africa','Northern Africa',NULL,002,015,NULL)
            ,('Liechtenstein','LI','LIE',438,'ISO 3166-2:LI',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('Lithuania','LT','LTU',440,'ISO 3166-2:LT',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Luxembourg','LU','LUX',442,'ISO 3166-2:LU',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('Macao','MO','MAC',446,'ISO 3166-2:MO',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Madagascar','MG','MDG',450,'ISO 3166-2:MG',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Malawi','MW','MWI',454,'ISO 3166-2:MW',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Malaysia','MY','MYS',458,'ISO 3166-2:MY',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Maldives','MV','MDV',462,'ISO 3166-2:MV',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Mali','ML','MLI',466,'ISO 3166-2:ML',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Malta','MT','MLT',470,'ISO 3166-2:MT',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Marshall Islands','MH','MHL',584,'ISO 3166-2:MH',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Martinique','MQ','MTQ',474,'ISO 3166-2:MQ',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Mauritania','MR','MRT',478,'ISO 3166-2:MR',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Mauritius','MU','MUS',480,'ISO 3166-2:MU',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Mayotte','YT','MYT',175,'ISO 3166-2:YT',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Mexico','MX','MEX',484,'ISO 3166-2:MX',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Micronesia (Federated States of)',
                'FM','FSM',583,'ISO 3166-2:FM',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Moldova, Republic of',
                'MD','MDA',498,'ISO 3166-2:MD',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Monaco','MC','MCO',492,'ISO 3166-2:MC',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('Mongolia','MN','MNG',496,'ISO 3166-2:MN',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Montenegro','ME','MNE',499,'ISO 3166-2:ME',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Montserrat','MS','MSR',500,'ISO 3166-2:MS',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Morocco','MA','MAR',504,'ISO 3166-2:MA',
                'Africa','Northern Africa',NULL,002,015,NULL)
            ,('Mozambique','MZ','MOZ',508,'ISO 3166-2:MZ',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Myanmar','MM','MMR',104,'ISO 3166-2:MM',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Namibia','NA','NAM',516,'ISO 3166-2:NA',
                'Africa','Sub-Saharan Africa','Southern Africa',002,202,018)
            ,('Nauru','NR','NRU',520,'ISO 3166-2:NR',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Nepal','NP','NPL',524,'ISO 3166-2:NP',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Netherlands','NL','NLD',528,'ISO 3166-2:NL',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('New Caledonia','NC','NCL',540,'ISO 3166-2:NC',
                'Oceania','Melanesia',NULL,009,054,NULL)
            ,('New Zealand','NZ','NZL',554,'ISO 3166-2:NZ',
                'Oceania','Australia and New Zealand',NULL,009,053,NULL)
            ,('Nicaragua','NI','NIC',558,'ISO 3166-2:NI',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Niger','NE','NER',562,'ISO 3166-2:NE',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Nigeria','NG','NGA',566,'ISO 3166-2:NG',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Niue','NU','NIU',570,'ISO 3166-2:NU',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('Norfolk Island','NF','NFK',574,'ISO 3166-2:NF',
                'Oceania','Australia and New Zealand',NULL,009,053,NULL)
            ,('North Macedonia','MK','MKD',807,'ISO 3166-2:MK',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Northern Mariana Islands','MP','MNP',580,'ISO 3166-2:MP',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Norway','NO','NOR',578,'ISO 3166-2:NO',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Oman','OM','OMN',512,'ISO 3166-2:OM',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Pakistan','PK','PAK',586,'ISO 3166-2:PK',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Palau','PW','PLW',585,'ISO 3166-2:PW',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Palestine, State of','PS','PSE',275,'ISO 3166-2:PS',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Panama','PA','PAN',591,'ISO 3166-2:PA',
                'Americas','Latin America and the Caribbean',
                'Central America',019,419,013)
            ,('Papua New Guinea','PG','PNG',598,'ISO 3166-2:PG',
                'Oceania','Melanesia',NULL,009,054,NULL)
            ,('Paraguay','PY','PRY',600,'ISO 3166-2:PY',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Peru','PE','PER',604,'ISO 3166-2:PE',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Philippines','PH','PHL',608,'ISO 3166-2:PH',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Pitcairn','PN','PCN',612,'ISO 3166-2:PN',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('Poland','PL','POL',616,'ISO 3166-2:PL',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Portugal','PT','PRT',620,'ISO 3166-2:PT',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Puerto Rico','PR','PRI',630,'ISO 3166-2:PR',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Qatar','QA','QAT',634,'ISO 3166-2:QA',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Réunion','RE','REU',638,'ISO 3166-2:RE',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Romania','RO','ROU',642,'ISO 3166-2:RO',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Russian Federation','RU','RUS',643,'ISO 3166-2:RU',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Rwanda','RW','RWA',646,'ISO 3166-2:RW',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Saint Barthélemy','BL','BLM',652,'ISO 3166-2:BL',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Saint Helena, Ascension and Tristan da Cunha',
                'SH','SHN',654,'ISO 3166-2:SH',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Saint Kitts and Nevis','KN','KNA',659,'ISO 3166-2:KN',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Saint Lucia','LC','LCA',662,'ISO 3166-2:LC',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Saint Martin (French part)','MF','MAF',663,'ISO 3166-2:MF',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Saint Pierre and Miquelon','PM','SPM',666,'ISO 3166-2:PM',
                'Americas','Northern America',NULL,019,021,NULL)
            ,('Saint Vincent and the Grenadines',
                'VC','VCT',670,'ISO 3166-2:VC',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Samoa','WS','WSM',882,'ISO 3166-2:WS',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('San Marino','SM','SMR',674,'ISO 3166-2:SM',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Sao Tome and Principe','ST','STP',678,'ISO 3166-2:ST',
                'Africa','Sub-Saharan Africa','Middle Africa',002,202,017)
            ,('Saudi Arabia','SA','SAU',682,'ISO 3166-2:SA',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Senegal','SN','SEN',686,'ISO 3166-2:SN',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Serbia','RS','SRB',688,'ISO 3166-2:RS',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Seychelles','SC','SYC',690,'ISO 3166-2:SC',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Sierra Leone','SL','SLE',694,'ISO 3166-2:SL',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Singapore','SG','SGP',702,'ISO 3166-2:SG',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Sint Maarten (Dutch part)','SX','SXM',534,'ISO 3166-2:SX',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Slovakia','SK','SVK',703,'ISO 3166-2:SK',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('Slovenia','SI','SVN',705,'ISO 3166-2:SI',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Solomon Islands','SB','SLB',090,'ISO 3166-2:SB',
                'Oceania','Melanesia',NULL,009,054,NULL)
            ,('Somalia','SO','SOM',706,'ISO 3166-2:SO',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('South Africa','ZA','ZAF',710,'ISO 3166-2:ZA',
                'Africa','Sub-Saharan Africa','Southern Africa',002,202,018)
            ,('South Georgia and the South Sandwich Islands',
                'GS','SGS',239,'ISO 3166-2:GS',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('South Sudan','SS','SSD',728,'ISO 3166-2:SS',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Spain','ES','ESP',724,'ISO 3166-2:ES',
                'Europe','Southern Europe',NULL,150,039,NULL)
            ,('Sri Lanka','LK','LKA',144,'ISO 3166-2:LK',
                'Asia','Southern Asia',NULL,142,034,NULL)
            ,('Sudan','SD','SDN',729,'ISO 3166-2:SD',
                'Africa','Northern Africa',NULL,002,015,NULL)
            ,('Suriname','SR','SUR',740,'ISO 3166-2:SR',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Svalbard and Jan Mayen','SJ','SJM',744,'ISO 3166-2:SJ',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Sweden','SE','SWE',752,'ISO 3166-2:SE',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('Switzerland','CH','CHE',756,'ISO 3166-2:CH',
                'Europe','Western Europe',NULL,150,155,NULL)
            ,('Syrian Arab Republic','SY','SYR',760,'ISO 3166-2:SY',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Taiwan, Province of China','TW','TWN',158,'ISO 3166-2:TW',
                'Asia','Eastern Asia',NULL,142,030,NULL)
            ,('Tajikistan','TJ','TJK',762,'ISO 3166-2:TJ',
                'Asia','Central Asia',NULL,142,143,NULL)
            ,('Tanzania, United Republic of','TZ','TZA',834,'ISO 3166-2:TZ',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Thailand','TH','THA',764,'ISO 3166-2:TH',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Timor-Leste','TL','TLS',626,'ISO 3166-2:TL',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Togo','TG','TGO',768,'ISO 3166-2:TG',
                'Africa','Sub-Saharan Africa','Western Africa',002,202,011)
            ,('Tokelau','TK','TKL',772,'ISO 3166-2:TK',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('Tonga','TO','TON',776,'ISO 3166-2:TO',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('Trinidad and Tobago','TT','TTO',780,'ISO 3166-2:TT',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Tunisia','TN','TUN',788,'ISO 3166-2:TN',
                'Africa','Northern Africa',NULL,002,015,NULL)
            ,('Turkey','TR','TUR',792,'ISO 3166-2:TR',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('Turkmenistan','TM','TKM',795,'ISO 3166-2:TM',
                'Asia','Central Asia',NULL,142,143,NULL)
            ,('Turks and Caicos Islands','TC','TCA',796,'ISO 3166-2:TC',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Tuvalu','TV','TUV',798,'ISO 3166-2:TV',
                'Oceania','Polynesia',NULL,009,061,NULL)
            ,('Uganda','UG','UGA',800,'ISO 3166-2:UG',
                'Africa','Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Ukraine','UA','UKR',804,'ISO 3166-2:UA',
                'Europe','Eastern Europe',NULL,150,151,NULL)
            ,('United Arab Emirates','AE','ARE',784,'ISO 3166-2:AE',
                'Asia','Western Asia',NULL,142,145,NULL)
            ,('United Kingdom of Great Britain and Northern Ireland',
                'GB','GBR',826,'ISO 3166-2:GB',
                'Europe','Northern Europe',NULL,150,154,NULL)
            ,('United States of America','US','USA',840,'ISO 3166-2:US',
                'Americas','Northern America',NULL,019,021,NULL)
            ,('United States Minor Outlying Islands',
                'UM','UMI',581,'ISO 3166-2:UM',
                'Oceania','Micronesia',NULL,009,057,NULL)
            ,('Uruguay','UY','URY',858,'ISO 3166-2:UY',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Uzbekistan','UZ','UZB',860,'ISO 3166-2:UZ',
                'Asia','Central Asia',NULL,142,143,NULL)
            ,('Vanuatu','VU','VUT',548,'ISO 3166-2:VU',
                'Oceania','Melanesia',NULL,009,054,NULL)
            ,('Venezuela (Bolivarian Republic of)',
                'VE','VEN',862,'ISO 3166-2:VE',
                'Americas','Latin America and the Caribbean',
                'South America',019,419,005)
            ,('Viet Nam','VN','VNM',704,'ISO 3166-2:VN',
                'Asia','South-eastern Asia',NULL,142,035,NULL)
            ,('Virgin Islands (British)','VG','VGB',092,'ISO 3166-2:VG',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Virgin Islands (U.S.)','VI','VIR',850,'ISO 3166-2:VI',
                'Americas','Latin America and the Caribbean',
                'Caribbean',019,419,029)
            ,('Wallis and Futuna','WF','WLF',876,'ISO 3166-2:WF','Oceania',
                'Polynesia',NULL,009,061,NULL)
            ,('Western Sahara','EH','ESH',732,'ISO 3166-2:EH','Africa',
                'Northern Africa',NULL,002,015,NULL)
            ,('Yemen','YE','YEM',887,'ISO 3166-2:YE','Asia',
                'Western Asia',NULL,142,145,NULL)
            ,('Zambia','ZM','ZMB',894,'ISO 3166-2:ZM','Africa',
                'Sub-Saharan Africa','Eastern Africa',002,202,014)
            ,('Zimbabwe','ZW','ZWE',716,'ISO 3166-2:ZW','Africa',
                'Sub-Saharan Africa','Eastern Africa',002,202,014);

        CREATE UNIQUE INDEX idx_iso_nations_id
        ON iso_nations (nation_iso_alpha_3);

        """
        return sql_script.replace("        ", "")

    def iso_3166_2_states() -> str:
        """
        Returns a SQLite3 script that creates a table to hold ISO 3166-2 data.
        Data sourced from Wikipedia.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a table to hold ISO 3166-2 data.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "iso_3166_2" (
            "nation_iso_alpha_2"            char(2) NOT NULL,
            "nation_iso_alpha_3"            char(3) NOT NULL,
            "nation_iso_numeric"            INT NOT NULL,
            "subdivision_iso_3166_2_code"   char(6) PRIMARY KEY,
            "subdivision_name"              TEXT NOT NULL,
            "subdivision_category"          TEXT NOT NULL,
            "subdivision_parent"            char(6)
        );
        """
        return sql_script.replace("        ", "")

    def iso_3166_2_data() -> str:
        """
        Returns a SQL INSERT script that inserts ISO 3166-2 data
        into a table designed to hold that data.
        Data sourced from Wikipedia.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a SQL INSERT script
        that inserts ISO 3166-2 data.
        """

        sql_script = """
        INSERT INTO iso_3166_2(
            nation_iso_alpha_2,
            nation_iso_alpha_3,
            nation_iso_numeric,
            subdivision_iso_3166_2_code,
            subdivision_name,
            subdivision_category,
            subdivision_parent
        )
        VALUES
            ("AD","AND",20,"AD-02","Canillo","parish",NULL)
            ,("AD","AND",20,"AD-03","Encamp","parish",NULL)
            ,("AD","AND",20,"AD-04","La Massana","parish",NULL)
            ,("AD","AND",20,"AD-05","Ordino","parish",NULL)
            ,("AD","AND",20,"AD-06","Sant Julià de Lòria","parish",NULL)
            ,("AD","AND",20,"AD-07","Andorra la Vella","parish",NULL)
            ,("AD","AND",20,"AD-08","Escaldes-Engordany","parish",NULL)
            ,("AE","ARE",784,"AE-AJ","Ajmān","emirate",NULL)
            ,("AE","ARE",784,"AE-AZ","Abū Z̧aby","emirate",NULL)
            ,("AE","ARE",784,"AE-DU","Dubayy","emirate",NULL)
            ,("AE","ARE",784,"AE-FU","Al Fujayrah","emirate",NULL)
            ,("AE","ARE",784,"AE-RK","Ra's al Khaymah","emirate",NULL)
            ,("AE","ARE",784,"AE-SH","Ash Shāriqah","emirate",NULL)
            ,("AE","ARE",784,"AE-UQ","Umm al Qaywayn","emirate",NULL)
            ,("AF","AFG",4,"AF-BAL","Balkh","province",NULL)
            ,("AF","AFG",4,"AF-BAM","Bāmyān","province",NULL)
            ,("AF","AFG",4,"AF-BDG","Bādghīs","province",NULL)
            ,("AF","AFG",4,"AF-BDS","Badakhshān","province",NULL)
            ,("AF","AFG",4,"AF-BGL","Baghlān","province",NULL)
            ,("AF","AFG",4,"AF-DAY","Dāykundī","province",NULL)
            ,("AF","AFG",4,"AF-FRA","Farāh","province",NULL)
            ,("AF","AFG",4,"AF-FYB","Fāryāb","province",NULL)
            ,("AF","AFG",4,"AF-GHA","Ghaznī","province",NULL)
            ,("AF","AFG",4,"AF-GHO","Ghōr","province",NULL)
            ,("AF","AFG",4,"AF-HEL","Helmand","province",NULL)
            ,("AF","AFG",4,"AF-HER","Herāt","province",NULL)
            ,("AF","AFG",4,"AF-JOW","Jowzjān","province",NULL)
            ,("AF","AFG",4,"AF-KAB","Kābul","province",NULL)
            ,("AF","AFG",4,"AF-KAN","Kandahār","province",NULL)
            ,("AF","AFG",4,"AF-KAP","Kāpīsā","province",NULL)
            ,("AF","AFG",4,"AF-KDZ","Kunduz","province",NULL)
            ,("AF","AFG",4,"AF-KHO","Khōst","province",NULL)
            ,("AF","AFG",4,"AF-KNR","Kunaṟ","province",NULL)
            ,("AF","AFG",4,"AF-LAG","Laghmān","province",NULL)
            ,("AF","AFG",4,"AF-LOG","Lōgar","province",NULL)
            ,("AF","AFG",4,"AF-NAN","Nangarhār","province",NULL)
            ,("AF","AFG",4,"AF-NIM","Nīmrōz","province",NULL)
            ,("AF","AFG",4,"AF-NUR","Nūristān","province",NULL)
            ,("AF","AFG",4,"AF-PAN","Panjshayr","province",NULL)
            ,("AF","AFG",4,"AF-PAR","Parwān","province",NULL)
            ,("AF","AFG",4,"AF-PIA","Paktiyā","province",NULL)
            ,("AF","AFG",4,"AF-PKA","Paktīkā","province",NULL)
            ,("AF","AFG",4,"AF-SAM","Samangān","province",NULL)
            ,("AF","AFG",4,"AF-SAR","Sar-e Pul","province",NULL)
            ,("AF","AFG",4,"AF-TAK","Takhār","province",NULL)
            ,("AF","AFG",4,"AF-URU","Uruzgān","province",NULL)
            ,("AF","AFG",4,"AF-WAR","Wardak","province",NULL)
            ,("AF","AFG",4,"AF-ZAB","Zābul","province",NULL)
            ,("AG","ATG",28,"AG-03","Saint George","parish",NULL)
            ,("AG","ATG",28,"AG-04","Saint John","parish",NULL)
            ,("AG","ATG",28,"AG-05","Saint Mary","parish",NULL)
            ,("AG","ATG",28,"AG-06","Saint Paul","parish",NULL)
            ,("AG","ATG",28,"AG-07","Saint Peter","parish",NULL)
            ,("AG","ATG",28,"AG-08","Saint Philip","parish",NULL)
            ,("AG","ATG",28,"AG-10","Barbuda","dependency",NULL)
            ,("AG","ATG",28,"AG-11","Redonda","dependency",NULL)
            ,("AI","AIA",660,"AI-??","Anguilla","country",NULL)
            ,("AL","ALB",8,"AL-01","Berat","county",NULL)
            ,("AL","ALB",8,"AL-02","Durrës","county",NULL)
            ,("AL","ALB",8,"AL-03","Elbasan","county",NULL)
            ,("AL","ALB",8,"AL-04","Fier","county",NULL)
            ,("AL","ALB",8,"AL-05","Gjirokastër","county",NULL)
            ,("AL","ALB",8,"AL-06","Korçë","county",NULL)
            ,("AL","ALB",8,"AL-07","Kukës","county",NULL)
            ,("AL","ALB",8,"AL-08","Lezhë","county",NULL)
            ,("AL","ALB",8,"AL-09","Dibër","county",NULL)
            ,("AL","ALB",8,"AL-10","Shkodër","county",NULL)
            ,("AL","ALB",8,"AL-11","Tiranë","county",NULL)
            ,("AL","ALB",8,"AL-12","Vlorë","county",NULL)
            ,("AM","ARM",51,"AM-AG","Aragac̣otn","region",NULL)
            ,("AM","ARM",51,"AM-AR","Ararat","region",NULL)
            ,("AM","ARM",51,"AM-AV","Armavir","region",NULL)
            ,("AM","ARM",51,"AM-ER","Erevan","city",NULL)
            ,("AM","ARM",51,"AM-GR","Geġark'unik'","region",NULL)
            ,("AM","ARM",51,"AM-KT","Kotayk","region",NULL)
            ,("AM","ARM",51,"AM-LO","Loṙi","region",NULL)
            ,("AM","ARM",51,"AM-SH","Širak","region",NULL)
            ,("AM","ARM",51,"AM-SU","Syunik","region",NULL)
            ,("AM","ARM",51,"AM-TV","Tavuš","region",NULL)
            ,("AM","ARM",51,"AM-VD","Vayoć Jor","region",NULL)
            ,("AO","AGO",24,"AO-BGO","Bengo","province",NULL)
            ,("AO","AGO",24,"AO-BGU","Benguela","province",NULL)
            ,("AO","AGO",24,"AO-BIE","Bié","province",NULL)
            ,("AO","AGO",24,"AO-CAB","Cabinda","province",NULL)
            ,("AO","AGO",24,"AO-CCU","Cuando Cubango","province",NULL)
            ,("AO","AGO",24,"AO-CNN","Cunene","province",NULL)
            ,("AO","AGO",24,"AO-CNO","Cuanza-Norte","province",NULL)
            ,("AO","AGO",24,"AO-CUS","Cuanza-Sul","province",NULL)
            ,("AO","AGO",24,"AO-HUA","Huambo","province",NULL)
            ,("AO","AGO",24,"AO-HUI","Huíla","province",NULL)
            ,("AO","AGO",24,"AO-LNO","Lunda-Norte","province",NULL)
            ,("AO","AGO",24,"AO-LSU","Lunda-Sul","province",NULL)
            ,("AO","AGO",24,"AO-LUA","Luanda","province",NULL)
            ,("AO","AGO",24,"AO-MAL","Malange","province",NULL)
            ,("AO","AGO",24,"AO-MOX","Moxico","province",NULL)
            ,("AO","AGO",24,"AO-NAM","Namibe","province",NULL)
            ,("AO","AGO",24,"AO-UIG","Uíge","province",NULL)
            ,("AO","AGO",24,"AO-ZAI","Zaire","province",NULL)
            ,("AQ","ATA",10,"AQ-??","Antartica","continent",NULL)
            ,("AR","ARG",32,"AR-A","Salta","province",NULL)
            ,("AR","ARG",32,"AR-B","Buenos Aires","province",NULL)
            ,("AR","ARG",32,"AR-C",
                "Ciudad Autónoma de Buenos Aires","city",NULL)
            ,("AR","ARG",32,"AR-D","San Luis","province",NULL)
            ,("AR","ARG",32,"AR-E","Entre Ríos","province",NULL)
            ,("AR","ARG",32,"AR-F","La Rioja","province",NULL)
            ,("AR","ARG",32,"AR-G","Santiago del Estero","province",NULL)
            ,("AR","ARG",32,"AR-H","Chaco","province",NULL)
            ,("AR","ARG",32,"AR-J","San Juan","province",NULL)
            ,("AR","ARG",32,"AR-K","Catamarca","province",NULL)
            ,("AR","ARG",32,"AR-L","La Pampa","province",NULL)
            ,("AR","ARG",32,"AR-M","Mendoza","province",NULL)
            ,("AR","ARG",32,"AR-N","Misiones","province",NULL)
            ,("AR","ARG",32,"AR-P","Formosa","province",NULL)
            ,("AR","ARG",32,"AR-Q","Neuquén","province",NULL)
            ,("AR","ARG",32,"AR-R","Río Negro","province",NULL)
            ,("AR","ARG",32,"AR-S","Santa Fe","province",NULL)
            ,("AR","ARG",32,"AR-T","Tucumán","province",NULL)
            ,("AR","ARG",32,"AR-U","Chubut","province",NULL)
            ,("AR","ARG",32,"AR-V","Tierra del Fuego","province",NULL)
            ,("AR","ARG",32,"AR-W","Corrientes","province",NULL)
            ,("AR","ARG",32,"AR-X","Córdoba","province",NULL)
            ,("AR","ARG",32,"AR-Y","Jujuy","province",NULL)
            ,("AR","ARG",32,"AR-Z","Santa Cruz","province",NULL)
            ,("AS","ASM",16,"AS-??","American Samoa","country",NULL)
            ,("AT","AUT",40,"AT-1","Burgenland","state",NULL)
            ,("AT","AUT",40,"AT-2","Kärnten","state",NULL)
            ,("AT","AUT",40,"AT-3","Niederösterreich","state",NULL)
            ,("AT","AUT",40,"AT-4","Oberösterreich","state",NULL)
            ,("AT","AUT",40,"AT-5","Salzburg","state",NULL)
            ,("AT","AUT",40,"AT-6","Steiermark","state",NULL)
            ,("AT","AUT",40,"AT-7","Tirol","state",NULL)
            ,("AT","AUT",40,"AT-8","Vorarlberg","state",NULL)
            ,("AT","AUT",40,"AT-9","Wien","state",NULL)
            ,("AU","AUS",36,"AU-ACT",
                "Australian Capital Territory","territory",NULL)
            ,("AU","AUS",36,"AU-NSW","New South Wales","state",NULL)
            ,("AU","AUS",36,"AU-NT","Northern Territory","territory",NULL)
            ,("AU","AUS",36,"AU-QLD","Queensland","state",NULL)
            ,("AU","AUS",36,"AU-SA","South Australia","state",NULL)
            ,("AU","AUS",36,"AU-TAS","Tasmania","state",NULL)
            ,("AU","AUS",36,"AU-VIC","Victoria","state",NULL)
            ,("AU","AUS",36,"AU-WA","Western Australia","state",NULL)
            ,("AW","ABW",533,"AW-??","Aruba","country",NULL)
            ,("AX","ALA",248,"AX-??","Åland Islands","country",NULL)
            ,("AZ","AZE",31,"AZ-ABS","Abşeron","rayon",NULL)
            ,("AZ","AZE",31,"AZ-AGA","Ağstafa","rayon",NULL)
            ,("AZ","AZE",31,"AZ-AGC","Ağcabədi","rayon",NULL)
            ,("AZ","AZE",31,"AZ-AGM","Ağdam","rayon",NULL)
            ,("AZ","AZE",31,"AZ-AGS","Ağdaş","rayon",NULL)
            ,("AZ","AZE",31,"AZ-AGU","Ağsu","rayon",NULL)
            ,("AZ","AZE",31,"AZ-AST","Astara","rayon",NULL)
            ,("AZ","AZE",31,"AZ-BA","Baki","municipality",NULL)
            ,("AZ","AZE",31,"AZ-BAB","Babək","rayon","AZ-NX")
            ,("AZ","AZE",31,"AZ-BAL","Balakən","rayon",NULL)
            ,("AZ","AZE",31,"AZ-BAR","Bərdə","rayon",NULL)
            ,("AZ","AZE",31,"AZ-BEY","Beyləqan","rayon",NULL)
            ,("AZ","AZE",31,"AZ-BIL","Biləsuvar","rayon",NULL)
            ,("AZ","AZE",31,"AZ-CAB","Cəbrayil","rayon",NULL)
            ,("AZ","AZE",31,"AZ-CAL","Cəlilabad","rayon",NULL)
            ,("AZ","AZE",31,"AZ-CUL","Culfa","rayon","AZ-NX")
            ,("AZ","AZE",31,"AZ-DAS","Daşkəsən","rayon",NULL)
            ,("AZ","AZE",31,"AZ-FUZ","Füzuli","rayon",NULL)
            ,("AZ","AZE",31,"AZ-GA","Gəncə","municipality",NULL)
            ,("AZ","AZE",31,"AZ-GAD","Gədəbəy","rayon",NULL)
            ,("AZ","AZE",31,"AZ-GOR","Goranboy","rayon",NULL)
            ,("AZ","AZE",31,"AZ-GOY","Göyçay","rayon",NULL)
            ,("AZ","AZE",31,"AZ-GYG","Göygöl","rayon",NULL)
            ,("AZ","AZE",31,"AZ-HAC","Haciqabul","rayon",NULL)
            ,("AZ","AZE",31,"AZ-IMI","İmişli","rayon",NULL)
            ,("AZ","AZE",31,"AZ-ISM","İsmayilli","rayon",NULL)
            ,("AZ","AZE",31,"AZ-KAL","Kəlbəcər","rayon",NULL)
            ,("AZ","AZE",31,"AZ-KAN","Kǝngǝrli","rayon","AZ-NX")
            ,("AZ","AZE",31,"AZ-KUR","Kürdəmir","rayon",NULL)
            ,("AZ","AZE",31,"AZ-LA","Lənkəran","municipality",NULL)
            ,("AZ","AZE",31,"AZ-LAC","Laçin","rayon",NULL)
            ,("AZ","AZE",31,"AZ-LAN","Lənkəran","rayon",NULL)
            ,("AZ","AZE",31,"AZ-LER","Lerik","rayon",NULL)
            ,("AZ","AZE",31,"AZ-MAS","Masalli","rayon",NULL)
            ,("AZ","AZE",31,"AZ-MI","Mingəçevir","municipality",NULL)
            ,("AZ","AZE",31,"AZ-NA","Naftalan","municipality",NULL)
            ,("AZ","AZE",31,"AZ-NEF","Neftçala","rayon",NULL)
            ,("AZ","AZE",31,"AZ-NV","Naxçivan","municipality","AZ-NX")
            ,("AZ","AZE",31,"AZ-NX","Naxçivan","autonomous_republic",NULL)
            ,("AZ","AZE",31,"AZ-OGU","Oğuz","rayon",NULL)
            ,("AZ","AZE",31,"AZ-ORD","Ordubad","rayon","AZ-NX")
            ,("AZ","AZE",31,"AZ-QAB","Qəbələ","rayon",NULL)
            ,("AZ","AZE",31,"AZ-QAX","Qax","rayon",NULL)
            ,("AZ","AZE",31,"AZ-QAZ","Qazax","rayon",NULL)
            ,("AZ","AZE",31,"AZ-QBA","Quba","rayon",NULL)
            ,("AZ","AZE",31,"AZ-QBI","Qubadli","rayon",NULL)
            ,("AZ","AZE",31,"AZ-QOB","Qobustan","rayon",NULL)
            ,("AZ","AZE",31,"AZ-QUS","Qusar","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SA","Şəki","municipality",NULL)
            ,("AZ","AZE",31,"AZ-SAB","Sabirabad","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SAD","Sədərək","rayon","AZ-NX")
            ,("AZ","AZE",31,"AZ-SAH","Şahbuz","rayon","AZ-NX")
            ,("AZ","AZE",31,"AZ-SAK","Şəki","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SAL","Salyan","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SAR","Şərur","rayon","AZ-NX")
            ,("AZ","AZE",31,"AZ-SAT","Saatli","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SBN","Şabran","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SIY","Siyəzən","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SKR","Şəmkir","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SM","Sumqayit","municipality",NULL)
            ,("AZ","AZE",31,"AZ-SMI","Şamaxi","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SMX","Samux","rayon",NULL)
            ,("AZ","AZE",31,"AZ-SR","Şirvan","municipality",NULL)
            ,("AZ","AZE",31,"AZ-SUS","Şuşa","rayon",NULL)
            ,("AZ","AZE",31,"AZ-TAR","Tərtər","rayon",NULL)
            ,("AZ","AZE",31,"AZ-TOV","Tovuz","rayon",NULL)
            ,("AZ","AZE",31,"AZ-UCA","Ucar","rayon",NULL)
            ,("AZ","AZE",31,"AZ-XA","Xankəndi","municipality",NULL)
            ,("AZ","AZE",31,"AZ-XAC","Xaçmaz","rayon",NULL)
            ,("AZ","AZE",31,"AZ-XCI","Xocali","rayon",NULL)
            ,("AZ","AZE",31,"AZ-XIZ","Xizi","rayon",NULL)
            ,("AZ","AZE",31,"AZ-XVD","Xocavənd","rayon",NULL)
            ,("AZ","AZE",31,"AZ-YAR","Yardimli","rayon",NULL)
            ,("AZ","AZE",31,"AZ-YE","Yevlax","municipality",NULL)
            ,("AZ","AZE",31,"AZ-YEV","Yevlax","rayon",NULL)
            ,("AZ","AZE",31,"AZ-ZAN","Zəngilan","rayon",NULL)
            ,("AZ","AZE",31,"AZ-ZAQ","Zaqatala","rayon",NULL)
            ,("AZ","AZE",31,"AZ-ZAR","Zərdab","rayon",NULL)
            ,("BA","BIH",70,"BA-BIH",
                "Federacija Bosne i Hercegovine","entity",NULL)
            ,("BA","BIH",70,"BA-BRC",
                "Brčko distrikt","district_with_special_status",NULL)
            ,("BA","BIH",70,"BA-SRP","Republika Srpska","entity",NULL)
            ,("BB","BRB",52,"BB-01","Christ Church","parish",NULL)
            ,("BB","BRB",52,"BB-02","Saint Andrew","parish",NULL)
            ,("BB","BRB",52,"BB-03","Saint George","parish",NULL)
            ,("BB","BRB",52,"BB-04","Saint James","parish",NULL)
            ,("BB","BRB",52,"BB-05","Saint John","parish",NULL)
            ,("BB","BRB",52,"BB-06","Saint Joseph","parish",NULL)
            ,("BB","BRB",52,"BB-07","Saint Lucy","parish",NULL)
            ,("BB","BRB",52,"BB-08","Saint Michael","parish",NULL)
            ,("BB","BRB",52,"BB-09","Saint Peter","parish",NULL)
            ,("BB","BRB",52,"BB-10","Saint Philip","parish",NULL)
            ,("BB","BRB",52,"BB-11","Saint Thomas","parish",NULL)
            ,("BD","BGD",50,"BD-01","Bandarban","district","BD-B")
            ,("BD","BGD",50,"BD-02","Barguna","district","BD-A")
            ,("BD","BGD",50,"BD-03","Bogura","district","BD-E")
            ,("BD","BGD",50,"BD-04","Brahmanbaria","district","BD-B")
            ,("BD","BGD",50,"BD-05","Bagerhat","district","BD-D")
            ,("BD","BGD",50,"BD-06","Barishal","district","BD-A")
            ,("BD","BGD",50,"BD-07","Bhola","district","BD-A")
            ,("BD","BGD",50,"BD-08","Cumilla","district","BD-B")
            ,("BD","BGD",50,"BD-09","Chandpur","district","BD-B")
            ,("BD","BGD",50,"BD-10","Chattogram","district","BD-B")
            ,("BD","BGD",50,"BD-11","Cox's Bazar","district","BD-B")
            ,("BD","BGD",50,"BD-12","Chuadanga","district","BD-D")
            ,("BD","BGD",50,"BD-13","Dhaka","district","BD-C")
            ,("BD","BGD",50,"BD-14","Dinajpur","district","BD-F")
            ,("BD","BGD",50,"BD-15","Faridpur","district","BD-C")
            ,("BD","BGD",50,"BD-16","Feni","district","BD-B")
            ,("BD","BGD",50,"BD-17","Gopalganj","district","BD-C")
            ,("BD","BGD",50,"BD-18","Gazipur","district","BD-C")
            ,("BD","BGD",50,"BD-19","Gaibandha","district","BD-F")
            ,("BD","BGD",50,"BD-20","Habiganj","district","BD-G")
            ,("BD","BGD",50,"BD-21","Jamalpur","district","BD-H")
            ,("BD","BGD",50,"BD-22","Jashore","district","BD-D")
            ,("BD","BGD",50,"BD-23","Jhenaidah","district","BD-D")
            ,("BD","BGD",50,"BD-24","Joypurhat","district","BD-E")
            ,("BD","BGD",50,"BD-25","Jhalakathi","district","BD-A")
            ,("BD","BGD",50,"BD-26","Kishoreganj","district","BD-C")
            ,("BD","BGD",50,"BD-27","Khulna","district","BD-D")
            ,("BD","BGD",50,"BD-28","Kurigram","district","BD-F")
            ,("BD","BGD",50,"BD-29","Khagrachhari","district","BD-B")
            ,("BD","BGD",50,"BD-30","Kushtia","district","BD-D")
            ,("BD","BGD",50,"BD-31","Lakshmipur","district","BD-B")
            ,("BD","BGD",50,"BD-32","Lalmonirhat","district","BD-F")
            ,("BD","BGD",50,"BD-33","Manikganj","district","BD-C")
            ,("BD","BGD",50,"BD-34","Mymensingh","district","BD-H")
            ,("BD","BGD",50,"BD-35","Munshiganj","district","BD-C")
            ,("BD","BGD",50,"BD-36","Madaripur","district","BD-C")
            ,("BD","BGD",50,"BD-37","Magura","district","BD-D")
            ,("BD","BGD",50,"BD-38","Moulvibazar","district","BD-G")
            ,("BD","BGD",50,"BD-39","Meherpur","district","BD-D")
            ,("BD","BGD",50,"BD-40","Narayanganj","district","BD-C")
            ,("BD","BGD",50,"BD-41","Netrakona","district","BD-H")
            ,("BD","BGD",50,"BD-42","Narsingdi","district","BD-C")
            ,("BD","BGD",50,"BD-43","Narail","district","BD-D")
            ,("BD","BGD",50,"BD-44","Natore","district","BD-E")
            ,("BD","BGD",50,"BD-45","Chapai Nawabganj","district","BD-E")
            ,("BD","BGD",50,"BD-46","Nilphamari","district","BD-F")
            ,("BD","BGD",50,"BD-47","Noakhali","district","BD-B")
            ,("BD","BGD",50,"BD-48","Naogaon","district","BD-E")
            ,("BD","BGD",50,"BD-49","Pabna","district","BD-E")
            ,("BD","BGD",50,"BD-50","Pirojpur","district","BD-A")
            ,("BD","BGD",50,"BD-51","Patuakhali","district","BD-A")
            ,("BD","BGD",50,"BD-52","Panchagarh","district","BD-F")
            ,("BD","BGD",50,"BD-53","Rajbari","district","BD-C")
            ,("BD","BGD",50,"BD-54","Rajshahi","district","BD-E")
            ,("BD","BGD",50,"BD-55","Rangpur","district","BD-F")
            ,("BD","BGD",50,"BD-56","Rangamati","district","BD-B")
            ,("BD","BGD",50,"BD-57","Sherpur","district","BD-H")
            ,("BD","BGD",50,"BD-58","Satkhira","district","BD-D")
            ,("BD","BGD",50,"BD-59","Sirajganj","district","BD-E")
            ,("BD","BGD",50,"BD-60","Sylhet","district","BD-G")
            ,("BD","BGD",50,"BD-61","Sunamganj","district","BD-G")
            ,("BD","BGD",50,"BD-62","Shariatpur","district","BD-C")
            ,("BD","BGD",50,"BD-63","Tangail","district","BD-C")
            ,("BD","BGD",50,"BD-64","Thakurgaon","district","BD-F")
            ,("BD","BGD",50,"BD-A","Barishal","division",NULL)
            ,("BD","BGD",50,"BD-B","Chattogram","division",NULL)
            ,("BD","BGD",50,"BD-C","Dhaka","division",NULL)
            ,("BD","BGD",50,"BD-D","Khulna","division",NULL)
            ,("BD","BGD",50,"BD-E","Rajshahi","division",NULL)
            ,("BD","BGD",50,"BD-F","Rangpur","division",NULL)
            ,("BD","BGD",50,"BD-G","Sylhet","division",NULL)
            ,("BD","BGD",50,"BD-H","Mymensingh","division",NULL)
            ,("BE","BEL",56,"BE-BRU",
                "Brussels Hoofdstedelijk Gewest","region",NULL)
            ,("BE","BEL",56,"BE-VAN","Antwerpen","province",NULL)
            ,("BE","BEL",56,"BE-VBR","Vlaams-Brabant","province",NULL)
            ,("BE","BEL",56,"BE-VLG","Vlaams Gewest","region",NULL)
            ,("BE","BEL",56,"BE-VLI","Limburg","province",NULL)
            ,("BE","BEL",56,"BE-VOV","Oost-Vlaanderen","province",NULL)
            ,("BE","BEL",56,"BE-VWV","West-Vlaanderen","province",NULL)
            ,("BE","BEL",56,"BE-WAL","Waals Gewest","region",NULL)
            ,("BE","BEL",56,"BE-WBR","Brabant wallon","province",NULL)
            ,("BE","BEL",56,"BE-WHT","Hainaut","province",NULL)
            ,("BE","BEL",56,"BE-WLG","Liège","province",NULL)
            ,("BE","BEL",56,"BE-WLX","Luxembourg","province",NULL)
            ,("BE","BEL",56,"BE-WNA","Namur","province",NULL)
            ,("BF","BFA",854,"BF-01","Boucle du Mouhoun","region",NULL)
            ,("BF","BFA",854,"BF-02","Cascades","region",NULL)
            ,("BF","BFA",854,"BF-03","Centre","region",NULL)
            ,("BF","BFA",854,"BF-04","Centre-Est","region",NULL)
            ,("BF","BFA",854,"BF-05","Centre-Nord","region",NULL)
            ,("BF","BFA",854,"BF-06","Centre-Ouest","region",NULL)
            ,("BF","BFA",854,"BF-07","Centre-Sud","region",NULL)
            ,("BF","BFA",854,"BF-08","Est","region",NULL)
            ,("BF","BFA",854,"BF-09","Hauts-Bassins","region",NULL)
            ,("BF","BFA",854,"BF-10","Nord","region",NULL)
            ,("BF","BFA",854,"BF-11","Plateau-Central","region",NULL)
            ,("BF","BFA",854,"BF-12","Sahel","region",NULL)
            ,("BF","BFA",854,"BF-13","Sud-Ouest","region",NULL)
            ,("BF","BFA",854,"BF-BAL","Balé","province",NULL)
            ,("BF","BFA",854,"BF-BAM","Bam","province",NULL)
            ,("BF","BFA",854,"BF-BAN","Banwa","province",NULL)
            ,("BF","BFA",854,"BF-BAZ","Bazèga","province",NULL)
            ,("BF","BFA",854,"BF-BGR","Bougouriba","province",NULL)
            ,("BF","BFA",854,"BF-BLG","Boulgou","province",NULL)
            ,("BF","BFA",854,"BF-BLK","Boulkiemdé","province",NULL)
            ,("BF","BFA",854,"BF-COM","Comoé","province",NULL)
            ,("BF","BFA",854,"BF-GAN","Ganzourgou","province",NULL)
            ,("BF","BFA",854,"BF-GNA","Gnagna","province",NULL)
            ,("BF","BFA",854,"BF-GOU","Gourma","province",NULL)
            ,("BF","BFA",854,"BF-HOU","Houet","province",NULL)
            ,("BF","BFA",854,"BF-IOB","Ioba","province",NULL)
            ,("BF","BFA",854,"BF-KAD","Kadiogo","province",NULL)
            ,("BF","BFA",854,"BF-KEN","Kénédougou","province",NULL)
            ,("BF","BFA",854,"BF-KMD","Komondjari","province",NULL)
            ,("BF","BFA",854,"BF-KMP","Kompienga","province",NULL)
            ,("BF","BFA",854,"BF-KOP","Koulpélogo","province",NULL)
            ,("BF","BFA",854,"BF-KOS","Kossi","province",NULL)
            ,("BF","BFA",854,"BF-KOT","Kouritenga","province",NULL)
            ,("BF","BFA",854,"BF-KOW","Kourwéogo","province",NULL)
            ,("BF","BFA",854,"BF-LER","Léraba","province",NULL)
            ,("BF","BFA",854,"BF-LOR","Loroum","province",NULL)
            ,("BF","BFA",854,"BF-MOU","Mouhoun","province",NULL)
            ,("BF","BFA",854,"BF-NAM","Namentenga","province",NULL)
            ,("BF","BFA",854,"BF-NAO","Nahouri","province",NULL)
            ,("BF","BFA",854,"BF-NAY","Nayala","province",NULL)
            ,("BF","BFA",854,"BF-NOU","Noumbiel","province",NULL)
            ,("BF","BFA",854,"BF-OUB","Oubritenga","province",NULL)
            ,("BF","BFA",854,"BF-OUD","Oudalan","province",NULL)
            ,("BF","BFA",854,"BF-PAS","Passoré","province",NULL)
            ,("BF","BFA",854,"BF-PON","Poni","province",NULL)
            ,("BF","BFA",854,"BF-SEN","Séno","province",NULL)
            ,("BF","BFA",854,"BF-SIS","Sissili","province",NULL)
            ,("BF","BFA",854,"BF-SMT","Sanmatenga","province",NULL)
            ,("BF","BFA",854,"BF-SNG","Sanguié","province",NULL)
            ,("BF","BFA",854,"BF-SOM","Soum","province",NULL)
            ,("BF","BFA",854,"BF-SOR","Sourou","province",NULL)
            ,("BF","BFA",854,"BF-TAP","Tapoa","province",NULL)
            ,("BF","BFA",854,"BF-TUI","Tuy","province",NULL)
            ,("BF","BFA",854,"BF-YAG","Yagha","province",NULL)
            ,("BF","BFA",854,"BF-YAT","Yatenga","province",NULL)
            ,("BF","BFA",854,"BF-ZIR","Ziro","province",NULL)
            ,("BF","BFA",854,"BF-ZON","Zondoma","province",NULL)
            ,("BF","BFA",854,"BF-ZOU","Zoundwéogo","province",NULL)
            ,("BG","BGR",100,"BG-01","Blagoevgrad","district",NULL)
            ,("BG","BGR",100,"BG-02","Burgas","district",NULL)
            ,("BG","BGR",100,"BG-03","Varna","district",NULL)
            ,("BG","BGR",100,"BG-04","Veliko Tarnovo","district",NULL)
            ,("BG","BGR",100,"BG-05","Vidin","district",NULL)
            ,("BG","BGR",100,"BG-06","Vratsa","district",NULL)
            ,("BG","BGR",100,"BG-07","Gabrovo","district",NULL)
            ,("BG","BGR",100,"BG-08","Dobrich","district",NULL)
            ,("BG","BGR",100,"BG-09","Kardzhali","district",NULL)
            ,("BG","BGR",100,"BG-10","Kyustendil","district",NULL)
            ,("BG","BGR",100,"BG-11","Lovech","district",NULL)
            ,("BG","BGR",100,"BG-12","Montana","district",NULL)
            ,("BG","BGR",100,"BG-13","Pazardzhik","district",NULL)
            ,("BG","BGR",100,"BG-14","Pernik","district",NULL)
            ,("BG","BGR",100,"BG-15","Pleven","district",NULL)
            ,("BG","BGR",100,"BG-16","Plovdiv","district",NULL)
            ,("BG","BGR",100,"BG-17","Razgrad","district",NULL)
            ,("BG","BGR",100,"BG-18","Ruse","district",NULL)
            ,("BG","BGR",100,"BG-19","Silistra","district",NULL)
            ,("BG","BGR",100,"BG-20","Sliven","district",NULL)
            ,("BG","BGR",100,"BG-21","Smolyan","district",NULL)
            ,("BG","BGR",100,"BG-22","Sofia (stolitsa)","district",NULL)
            ,("BG","BGR",100,"BG-23","Sofia","district",NULL)
            ,("BG","BGR",100,"BG-24","Stara Zagora","district",NULL)
            ,("BG","BGR",100,"BG-25","Targovishte","district",NULL)
            ,("BG","BGR",100,"BG-26","Haskovo","district",NULL)
            ,("BG","BGR",100,"BG-27","Shumen","district",NULL)
            ,("BG","BGR",100,"BG-28","Yambol","district",NULL)
            ,("BH","BHR",48,"BH-13","Al 'Āşimah","governorate",NULL)
            ,("BH","BHR",48,"BH-14","Al Janūbīyah","governorate",NULL)
            ,("BH","BHR",48,"BH-15","Al Muḩarraq","governorate",NULL)
            ,("BH","BHR",48,"BH-17","Ash Shamālīyah","governorate",NULL)
            ,("BI","BDI",108,"BI-BB","Bubanza","province",NULL)
            ,("BI","BDI",108,"BI-BL","Bujumbura Rural","province",NULL)
            ,("BI","BDI",108,"BI-BM","Bujumbura Mairie","province",NULL)
            ,("BI","BDI",108,"BI-BR","Bururi","province",NULL)
            ,("BI","BDI",108,"BI-CA","Cankuzo","province",NULL)
            ,("BI","BDI",108,"BI-CI","Cibitoke","province",NULL)
            ,("BI","BDI",108,"BI-GI","Gitega","province",NULL)
            ,("BI","BDI",108,"BI-KI","Kirundo","province",NULL)
            ,("BI","BDI",108,"BI-KR","Karuzi","province",NULL)
            ,("BI","BDI",108,"BI-KY","Kayanza","province",NULL)
            ,("BI","BDI",108,"BI-MA","Makamba","province",NULL)
            ,("BI","BDI",108,"BI-MU","Muramvya","province",NULL)
            ,("BI","BDI",108,"BI-MW","Mwaro","province",NULL)
            ,("BI","BDI",108,"BI-MY","Muyinga","province",NULL)
            ,("BI","BDI",108,"BI-NG","Ngozi","province",NULL)
            ,("BI","BDI",108,"BI-RM","Rumonge","province",NULL)
            ,("BI","BDI",108,"BI-RT","Rutana","province",NULL)
            ,("BI","BDI",108,"BI-RY","Ruyigi","province",NULL)
            ,("BJ","BEN",204,"BJ-AK","Atacora","department",NULL)
            ,("BJ","BEN",204,"BJ-AL","Alibori","department",NULL)
            ,("BJ","BEN",204,"BJ-AQ","Atlantique","department",NULL)
            ,("BJ","BEN",204,"BJ-BO","Borgou","department",NULL)
            ,("BJ","BEN",204,"BJ-CO","Collines","department",NULL)
            ,("BJ","BEN",204,"BJ-DO","Donga","department",NULL)
            ,("BJ","BEN",204,"BJ-KO","Couffo","department",NULL)
            ,("BJ","BEN",204,"BJ-LI","Littoral","department",NULL)
            ,("BJ","BEN",204,"BJ-MO","Mono","department",NULL)
            ,("BJ","BEN",204,"BJ-OU","Ouémé","department",NULL)
            ,("BJ","BEN",204,"BJ-PL","Plateau","department",NULL)
            ,("BJ","BEN",204,"BJ-ZO","Zou","department",NULL)
            ,("BL","BLM",652,"BL-??","Saint Barthélemy","country",NULL)
            ,("BM","BMU",60,"BM-??","Bermuda","country",NULL)
            ,("BN","BRN",96,"BN-BE","Belait","district",NULL)
            ,("BN","BRN",96,"BN-BM","Brunei-Muara","district",NULL)
            ,("BN","BRN",96,"BN-TE","Temburong","district",NULL)
            ,("BN","BRN",96,"BN-TU","Tutong","district",NULL)
            ,("BO","BOL",68,"BO-B","El Beni","department",NULL)
            ,("BO","BOL",68,"BO-C","Cochabamba","department",NULL)
            ,("BO","BOL",68,"BO-H","Chuquisaca","department",NULL)
            ,("BO","BOL",68,"BO-L","La Paz","department",NULL)
            ,("BO","BOL",68,"BO-N","Pando","department",NULL)
            ,("BO","BOL",68,"BO-O","Oruro","department",NULL)
            ,("BO","BOL",68,"BO-P","Potosí","department",NULL)
            ,("BO","BOL",68,"BO-S","Santa Cruz","department",NULL)
            ,("BO","BOL",68,"BO-T","Tarija","department",NULL)
            ,("BQ","BES",535,"BQ-BO","Bonaire","special_municipalities",NULL)
            ,("BQ","BES",535,"BQ-SA","Saba","special_municipalities",NULL)
            ,("BQ","BES",535,"BQ-SE",
                "Sint Eustatius","special_municipalities",NULL)
            ,("BR","BRA",76,"BR-AC","Acre","state",NULL)
            ,("BR","BRA",76,"BR-AL","Alagoas","state",NULL)
            ,("BR","BRA",76,"BR-AM","Amazonas","state",NULL)
            ,("BR","BRA",76,"BR-AP","Amapá","state",NULL)
            ,("BR","BRA",76,"BR-BA","Bahia","state",NULL)
            ,("BR","BRA",76,"BR-CE","Ceará","state",NULL)
            ,("BR","BRA",76,"BR-DF","Distrito Federal","federal_district",NULL)
            ,("BR","BRA",76,"BR-ES","Espírito Santo","state",NULL)
            ,("BR","BRA",76,"BR-GO","Goiás","state",NULL)
            ,("BR","BRA",76,"BR-MA","Maranhão","state",NULL)
            ,("BR","BRA",76,"BR-MG","Minas Gerais","state",NULL)
            ,("BR","BRA",76,"BR-MS","Mato Grosso do Sul","state",NULL)
            ,("BR","BRA",76,"BR-MT","Mato Grosso","state",NULL)
            ,("BR","BRA",76,"BR-PA","Pará","state",NULL)
            ,("BR","BRA",76,"BR-PB","Paraíba","state",NULL)
            ,("BR","BRA",76,"BR-PE","Pernambuco","state",NULL)
            ,("BR","BRA",76,"BR-PI","Piauí","state",NULL)
            ,("BR","BRA",76,"BR-PR","Paraná","state",NULL)
            ,("BR","BRA",76,"BR-RJ","Rio de Janeiro","state",NULL)
            ,("BR","BRA",76,"BR-RN","Rio Grande do Norte","state",NULL)
            ,("BR","BRA",76,"BR-RO","Rondônia","state",NULL)
            ,("BR","BRA",76,"BR-RR","Roraima","state",NULL)
            ,("BR","BRA",76,"BR-RS","Rio Grande do Sul","state",NULL)
            ,("BR","BRA",76,"BR-SC","Santa Catarina","state",NULL)
            ,("BR","BRA",76,"BR-SE","Sergipe","state",NULL)
            ,("BR","BRA",76,"BR-SP","São Paulo","state",NULL)
            ,("BR","BRA",76,"BR-TO","Tocantins","state",NULL)
            ,("BS","BHS",44,"BS-AK","Acklins","district",NULL)
            ,("BS","BHS",44,"BS-BI","Bimini","district",NULL)
            ,("BS","BHS",44,"BS-BP","Black Point","district",NULL)
            ,("BS","BHS",44,"BS-BY","Berry Islands","district",NULL)
            ,("BS","BHS",44,"BS-CE","Central Eleuthera","district",NULL)
            ,("BS","BHS",44,"BS-CI","Cat Island","district",NULL)
            ,("BS","BHS",44,"BS-CK",
                "Crooked Island and Long Cay","district",NULL)
            ,("BS","BHS",44,"BS-CO","Central Abaco","district",NULL)
            ,("BS","BHS",44,"BS-CS","Central Andros","district",NULL)
            ,("BS","BHS",44,"BS-EG","East Grand Bahama","district",NULL)
            ,("BS","BHS",44,"BS-EX","Exuma","district",NULL)
            ,("BS","BHS",44,"BS-FP","City of Freeport","district",NULL)
            ,("BS","BHS",44,"BS-GC","Grand Cay","district",NULL)
            ,("BS","BHS",44,"BS-HI","Harbour Island","district",NULL)
            ,("BS","BHS",44,"BS-HT","Hope Town","district",NULL)
            ,("BS","BHS",44,"BS-IN","Inagua","district",NULL)
            ,("BS","BHS",44,"BS-LI","Long Island","district",NULL)
            ,("BS","BHS",44,"BS-MC","Mangrove Cay","district",NULL)
            ,("BS","BHS",44,"BS-MG","Mayaguana","district",NULL)
            ,("BS","BHS",44,"BS-MI","Moore's Island","district",NULL)
            ,("BS","BHS",44,"BS-NE","North Eleuthera","district",NULL)
            ,("BS","BHS",44,"BS-NO","North Abaco","district",NULL)
            ,("BS","BHS",44,"BS-NP","New Providence","island",NULL)
            ,("BS","BHS",44,"BS-NS","North Andros","district",NULL)
            ,("BS","BHS",44,"BS-RC","Rum Cay","district",NULL)
            ,("BS","BHS",44,"BS-RI","Ragged Island","district",NULL)
            ,("BS","BHS",44,"BS-SA","South Andros","district",NULL)
            ,("BS","BHS",44,"BS-SE","South Eleuthera","district",NULL)
            ,("BS","BHS",44,"BS-SO","South Abaco","district",NULL)
            ,("BS","BHS",44,"BS-SS","San Salvador","district",NULL)
            ,("BS","BHS",44,"BS-SW","Spanish Wells","district",NULL)
            ,("BS","BHS",44,"BS-WG","West Grand Bahama","district",NULL)
            ,("BT","BTN",64,"BT-11","Paro","district",NULL)
            ,("BT","BTN",64,"BT-12","Chhukha","district",NULL)
            ,("BT","BTN",64,"BT-13","Haa","district",NULL)
            ,("BT","BTN",64,"BT-14","Samtse","district",NULL)
            ,("BT","BTN",64,"BT-15","Thimphu","district",NULL)
            ,("BT","BTN",64,"BT-21","Tsirang","district",NULL)
            ,("BT","BTN",64,"BT-22","Dagana","district",NULL)
            ,("BT","BTN",64,"BT-23","Punakha","district",NULL)
            ,("BT","BTN",64,"BT-24","Wangdue Phodrang","district",NULL)
            ,("BT","BTN",64,"BT-31","Sarpang","district",NULL)
            ,("BT","BTN",64,"BT-32","Trongsa","district",NULL)
            ,("BT","BTN",64,"BT-33","Bumthang","district",NULL)
            ,("BT","BTN",64,"BT-34","Zhemgang","district",NULL)
            ,("BT","BTN",64,"BT-41","Trashigang","district",NULL)
            ,("BT","BTN",64,"BT-42","Monggar","district",NULL)
            ,("BT","BTN",64,"BT-43","Pema Gatshel","district",NULL)
            ,("BT","BTN",64,"BT-44","Lhuentse","district",NULL)
            ,("BT","BTN",64,"BT-45","Samdrup Jongkhar","district",NULL)
            ,("BT","BTN",64,"BT-GA","Gasa","district",NULL)
            ,("BT","BTN",64,"BT-TY","Trashi Yangtse","district",NULL)
            ,("BV","BVT",74,"BV-??","Bouvet Island","country",NULL)
            ,("BW","BWA",72,"BW-CE","Central","district",NULL)
            ,("BW","BWA",72,"BW-CH","Chobe","district",NULL)
            ,("BW","BWA",72,"BW-FR","Francistown","city",NULL)
            ,("BW","BWA",72,"BW-GA","Gaborone","city",NULL)
            ,("BW","BWA",72,"BW-GH","Ghanzi","district",NULL)
            ,("BW","BWA",72,"BW-JW","Jwaneng","town",NULL)
            ,("BW","BWA",72,"BW-KG","Kgalagadi","district",NULL)
            ,("BW","BWA",72,"BW-KL","Kgatleng","district",NULL)
            ,("BW","BWA",72,"BW-KW","Kweneng","district",NULL)
            ,("BW","BWA",72,"BW-LO","Lobatse","town",NULL)
            ,("BW","BWA",72,"BW-NE","North East","district",NULL)
            ,("BW","BWA",72,"BW-NW","North West","district",NULL)
            ,("BW","BWA",72,"BW-SE","South East","district",NULL)
            ,("BW","BWA",72,"BW-SO","Southern","district",NULL)
            ,("BW","BWA",72,"BW-SP","Selibe Phikwe","town",NULL)
            ,("BW","BWA",72,"BW-ST","Sowa Town","town",NULL)
            ,("BY","BLR",112,"BY-BR","Brestskaya voblasts","oblast",NULL)
            ,("BY","BLR",112,"BY-HM","Horad Minsk","city",NULL)
            ,("BY","BLR",112,"BY-HO","Homyel'skaya voblasts","oblast",NULL)
            ,("BY","BLR",112,"BY-HR","Hrodzyenskaya voblasts","oblast",NULL)
            ,("BY","BLR",112,"BY-MA","Mahilyowskaya voblasts","oblast",NULL)
            ,("BY","BLR",112,"BY-MI","Minskaya voblasts","oblast",NULL)
            ,("BY","BLR",112,"BY-VI","Vitsyebskaya voblasts","oblast",NULL)
            ,("BZ","BLZ",84,"BZ-BZ","Belize","district",NULL)
            ,("BZ","BLZ",84,"BZ-CY","Cayo","district",NULL)
            ,("BZ","BLZ",84,"BZ-CZL","Corozal","district",NULL)
            ,("BZ","BLZ",84,"BZ-OW","Orange Walk","district",NULL)
            ,("BZ","BLZ",84,"BZ-SC","Stann Creek","district",NULL)
            ,("BZ","BLZ",84,"BZ-TOL","Toledo","district",NULL)
            ,("CA","CAN",124,"CA-AB","Alberta","province",NULL)
            ,("CA","CAN",124,"CA-BC","British Columbia","province",NULL)
            ,("CA","CAN",124,"CA-MB","Manitoba","province",NULL)
            ,("CA","CAN",124,"CA-NB","New Brunswick","province",NULL)
            ,("CA","CAN",124,"CA-NL",
                "Newfoundland and Labrador","province",NULL)
            ,("CA","CAN",124,"CA-NS","Nova Scotia","province",NULL)
            ,("CA","CAN",124,"CA-NT","Northwest Territories","territory",NULL)
            ,("CA","CAN",124,"CA-NU","Nunavut","territory",NULL)
            ,("CA","CAN",124,"CA-ON","Ontario","province",NULL)
            ,("CA","CAN",124,"CA-PE","Prince Edward Island","province",NULL)
            ,("CA","CAN",124,"CA-QC","Quebec","province",NULL)
            ,("CA","CAN",124,"CA-SK","Saskatchewan","province",NULL)
            ,("CA","CAN",124,"CA-YT","Yukon","territory",NULL)
            ,("CC","CCK",166,"CC-??","Cocos (Keeling) Islands","country",NULL)
            ,("CD","COD",180,"CD-BC","Kongo Central","province",NULL)
            ,("CD","COD",180,"CD-BU","Bas-Uélé","province",NULL)
            ,("CD","COD",180,"CD-EQ","Équateur","province",NULL)
            ,("CD","COD",180,"CD-HK","Haut-Katanga","province",NULL)
            ,("CD","COD",180,"CD-HL","Haut-Lomami","province",NULL)
            ,("CD","COD",180,"CD-HU","Haut-Uélé","province",NULL)
            ,("CD","COD",180,"CD-IT","Ituri","province",NULL)
            ,("CD","COD",180,"CD-KC","Kasaï Central","province",NULL)
            ,("CD","COD",180,"CD-KE","Kasaï Oriental","province",NULL)
            ,("CD","COD",180,"CD-KG","Kwango","province",NULL)
            ,("CD","COD",180,"CD-KL","Kwilu","province",NULL)
            ,("CD","COD",180,"CD-KN","Kinshasa","city",NULL)
            ,("CD","COD",180,"CD-KS","Kasaï","province",NULL)
            ,("CD","COD",180,"CD-LO","Lomami","province",NULL)
            ,("CD","COD",180,"CD-LU","Lualaba","province",NULL)
            ,("CD","COD",180,"CD-MA","Maniema","province",NULL)
            ,("CD","COD",180,"CD-MN","Mai-Ndombe","province",NULL)
            ,("CD","COD",180,"CD-MO","Mongala","province",NULL)
            ,("CD","COD",180,"CD-NK","Nord-Kivu","province",NULL)
            ,("CD","COD",180,"CD-NU","Nord-Ubangi","province",NULL)
            ,("CD","COD",180,"CD-SA","Sankuru","province",NULL)
            ,("CD","COD",180,"CD-SK","Sud-Kivu","province",NULL)
            ,("CD","COD",180,"CD-SU","Sud-Ubangi","province",NULL)
            ,("CD","COD",180,"CD-TA","Tanganyika","province",NULL)
            ,("CD","COD",180,"CD-TO","Tshopo","province",NULL)
            ,("CD","COD",180,"CD-TU","Tshuapa","province",NULL)
            ,("CF","CAF",140,"CF-AC","Ouham","prefecture",NULL)
            ,("CF","CAF",140,"CF-BB","Bamingui-Bangoran","prefecture",NULL)
            ,("CF","CAF",140,"CF-BGF","Bangui","commune",NULL)
            ,("CF","CAF",140,"CF-BK","Basse-Kotto","prefecture",NULL)
            ,("CF","CAF",140,"CF-HK","Haute-Kotto","prefecture",NULL)
            ,("CF","CAF",140,"CF-HM","Haut-Mbomou","prefecture",NULL)
            ,("CF","CAF",140,"CF-HS","Haute-Sangha/Mambéré-Kadéï","prefecture",NULL)
            ,("CF","CAF",140,"CF-KB","Gribingui","economic_prefecture",NULL)
            ,("CF","CAF",140,"CF-KG","Kémo-Gribingui","prefecture",NULL)
            ,("CF","CAF",140,"CF-LB","Lobaye","prefecture",NULL)
            ,("CF","CAF",140,"CF-MB","Mbomou","prefecture",NULL)
            ,("CF","CAF",140,"CF-MP","Ombella-Mpoko","prefecture",NULL)
            ,("CF","CAF",140,"CF-NM","Nana-Mambéré","prefecture",NULL)
            ,("CF","CAF",140,"CF-OP","Ouham-Pendé","prefecture",NULL)
            ,("CF","CAF",140,"CF-SE","Sangha","economic_prefecture",NULL)
            ,("CF","CAF",140,"CF-UK","Ouaka","prefecture",NULL)
            ,("CF","CAF",140,"CF-VK","Vakaga","prefecture",NULL)
            ,("CG","COG",178,"CG-11","Bouenza","department",NULL)
            ,("CG","COG",178,"CG-12","Pool","department",NULL)
            ,("CG","COG",178,"CG-13","Sangha","department",NULL)
            ,("CG","COG",178,"CG-14","Plateaux","department",NULL)
            ,("CG","COG",178,"CG-15","Cuvette-Ouest","department",NULL)
            ,("CG","COG",178,"CG-16","Pointe-Noire","department",NULL)
            ,("CG","COG",178,"CG-2","Lékoumou","department",NULL)
            ,("CG","COG",178,"CG-5","Kouilou","department",NULL)
            ,("CG","COG",178,"CG-7","Likouala","department",NULL)
            ,("CG","COG",178,"CG-8","Cuvette","department",NULL)
            ,("CG","COG",178,"CG-9","Niari","department",NULL)
            ,("CG","COG",178,"CG-BZV","Brazzaville","department",NULL)
            ,("CH","CHE",756,"CH-AG","Aargau","canton",NULL)
            ,("CH","CHE",756,"CH-AI","Appenzell Innerrhoden","canton",NULL)
            ,("CH","CHE",756,"CH-AR","Appenzell Ausserrhoden","canton",NULL)
            ,("CH","CHE",756,"CH-BE","Bern","canton",NULL)
            ,("CH","CHE",756,"CH-BL","Basel-Landschaft","canton",NULL)
            ,("CH","CHE",756,"CH-BS","Basel-Stadt","canton",NULL)
            ,("CH","CHE",756,"CH-FR","Fribourg","canton",NULL)
            ,("CH","CHE",756,"CH-GE","Genève","canton",NULL)
            ,("CH","CHE",756,"CH-GL","Glarus","canton",NULL)
            ,("CH","CHE",756,"CH-GR","Graubünden","canton",NULL)
            ,("CH","CHE",756,"CH-JU","Jura","canton",NULL)
            ,("CH","CHE",756,"CH-LU","Luzern","canton",NULL)
            ,("CH","CHE",756,"CH-NE","Neuchâtel","canton",NULL)
            ,("CH","CHE",756,"CH-NW","Nidwalden","canton",NULL)
            ,("CH","CHE",756,"CH-OW","Obwalden","canton",NULL)
            ,("CH","CHE",756,"CH-SG","Sankt Gallen","canton",NULL)
            ,("CH","CHE",756,"CH-SH","Schaffhausen","canton",NULL)
            ,("CH","CHE",756,"CH-SO","Solothurn","canton",NULL)
            ,("CH","CHE",756,"CH-SZ","Schwyz","canton",NULL)
            ,("CH","CHE",756,"CH-TG","Thurgau","canton",NULL)
            ,("CH","CHE",756,"CH-TI","Ticino","canton",NULL)
            ,("CH","CHE",756,"CH-UR","Uri","canton",NULL)
            ,("CH","CHE",756,"CH-VD","Vaud","canton",NULL)
            ,("CH","CHE",756,"CH-VS","Valais","canton",NULL)
            ,("CH","CHE",756,"CH-ZG","Zug","canton",NULL)
            ,("CH","CHE",756,"CH-ZH","Zürich","canton",NULL)
            ,("CI","CIV",384,"CI-AB","Abidjan","autonomous_district",NULL)
            ,("CI","CIV",384,"CI-BS","Bas-Sassandra","district",NULL)
            ,("CI","CIV",384,"CI-CM","Comoé","district",NULL)
            ,("CI","CIV",384,"CI-DN","Denguélé","district",NULL)
            ,("CI","CIV",384,"CI-GD","Gôh-Djiboua","district",NULL)
            ,("CI","CIV",384,"CI-LC","Lacs","district",NULL)
            ,("CI","CIV",384,"CI-LG","Lagunes","district",NULL)
            ,("CI","CIV",384,"CI-MG","Montagnes","district",NULL)
            ,("CI","CIV",384,"CI-SM","Sassandra-Marahoué","district",NULL)
            ,("CI","CIV",384,"CI-SV","Savanes","district",NULL)
            ,("CI","CIV",384,"CI-VB","Vallée du Bandama","district",NULL)
            ,("CI","CIV",384,"CI-WR","Woroba","district",NULL)
            ,("CI","CIV",384,"CI-YM","Yamoussoukro","autonomous_district",NULL)
            ,("CI","CIV",384,"CI-ZZ","Zanzan","district",NULL)
            ,("CK","COK",184,"CK-??","Cook Islands","country",NULL)
            ,("CL","CHL",152,"CL-AI",
                "Aisén del General Carlos Ibañez del Campo","region",NULL)
            ,("CL","CHL",152,"CL-AN","Antofagasta","region",NULL)
            ,("CL","CHL",152,"CL-AP","Arica y Parinacota","region",NULL)
            ,("CL","CHL",152,"CL-AR","La Araucanía","region",NULL)
            ,("CL","CHL",152,"CL-AT","Atacama","region",NULL)
            ,("CL","CHL",152,"CL-BI","Biobío","region",NULL)
            ,("CL","CHL",152,"CL-CO","Coquimbo","region",NULL)
            ,("CL","CHL",152,"CL-LI",
                "Libertador General Bernardo O'Higgins","region",NULL)
            ,("CL","CHL",152,"CL-LL","Los Lagos","region",NULL)
            ,("CL","CHL",152,"CL-LR","Los Ríos","region",NULL)
            ,("CL","CHL",152,"CL-MA","Magallanes","region",NULL)
            ,("CL","CHL",152,"CL-ML","Maule","region",NULL)
            ,("CL","CHL",152,"CL-NB","Ñuble","region",NULL)
            ,("CL","CHL",152,"CL-RM",
                "Región Metropolitana de Santiago","region",NULL)
            ,("CL","CHL",152,"CL-TA","Tarapacá","region",NULL)
            ,("CL","CHL",152,"CL-VS","Valparaíso","region",NULL)
            ,("CM","CMR",120,"CM-AD","Adamaoua","region",NULL)
            ,("CM","CMR",120,"CM-CE","Centre","region",NULL)
            ,("CM","CMR",120,"CM-EN","Far North","region",NULL)
            ,("CM","CMR",120,"CM-ES","East","region",NULL)
            ,("CM","CMR",120,"CM-LT","Littoral","region",NULL)
            ,("CM","CMR",120,"CM-NO","North","region",NULL)
            ,("CM","CMR",120,"CM-NW","North-West","region",NULL)
            ,("CM","CMR",120,"CM-OU","West","region",NULL)
            ,("CM","CMR",120,"CM-SU","South","region",NULL)
            ,("CM","CMR",120,"CM-SW","South-West","region",NULL)
            ,("CN","CHN",156,"CN-AH","Anhui Sheng","province",NULL)
            ,("CN","CHN",156,"CN-BJ","Beijing Shi","municipality",NULL)
            ,("CN","CHN",156,"CN-CQ","Chongqing Shi","municipality",NULL)
            ,("CN","CHN",156,"CN-FJ","Fujian Sheng","province",NULL)
            ,("CN","CHN",156,"CN-GD","Guangdong Sheng","province",NULL)
            ,("CN","CHN",156,"CN-GS","Gansu Sheng","province",NULL)
            ,("CN","CHN",156,"CN-GX",
                "Guangxi Zhuangzu Zizhiqu","autonomous_region",NULL)
            ,("CN","CHN",156,"CN-GZ","Guizhou Sheng","province",NULL)
            ,("CN","CHN",156,"CN-HA","Henan Sheng","province",NULL)
            ,("CN","CHN",156,"CN-HB","Hubei Sheng","province",NULL)
            ,("CN","CHN",156,"CN-HE","Hebei Sheng","province",NULL)
            ,("CN","CHN",156,"CN-HI","Hainan Sheng","province",NULL)
            ,("CN","CHN",156,"CN-HK",
                "Hong Kong SAR","special_administrative_region",NULL)
            ,("CN","CHN",156,"CN-HL","Heilongjiang Sheng","province",NULL)
            ,("CN","CHN",156,"CN-HN","Hunan Sheng","province",NULL)
            ,("CN","CHN",156,"CN-JL","Jilin Sheng","province",NULL)
            ,("CN","CHN",156,"CN-JS","Jiangsu Sheng","province",NULL)
            ,("CN","CHN",156,"CN-JX","Jiangxi Sheng","province",NULL)
            ,("CN","CHN",156,"CN-LN","Liaoning Sheng","province",NULL)
            ,("CN","CHN",156,"CN-MO",
                "Macao SAR","special_administrative_region",NULL)
            ,("CN","CHN",156,"CN-NM",
                "Nei Mongol Zizhiqu","autonomous_region",NULL)
            ,("CN","CHN",156,"CN-NX",
                "Ningxia Huizu Zizhiqu","autonomous_region",NULL)
            ,("CN","CHN",156,"CN-QH","Qinghai Sheng","province",NULL)
            ,("CN","CHN",156,"CN-SC","Sichuan Sheng","province",NULL)
            ,("CN","CHN",156,"CN-SD","Shandong Sheng","province",NULL)
            ,("CN","CHN",156,"CN-SH","Shanghai Shi","municipality",NULL)
            ,("CN","CHN",156,"CN-SN","Shaanxi Sheng","province",NULL)
            ,("CN","CHN",156,"CN-SX","Shanxi Sheng","province",NULL)
            ,("CN","CHN",156,"CN-TJ","Tianjin Shi","municipality",NULL)
            ,("CN","CHN",156,"CN-TW","Taiwan Sheng","province",NULL)
            ,("CN","CHN",156,"CN-XJ",
                "Xinjiang Uygur Zizhiqu","autonomous_region",NULL)
            ,("CN","CHN",156,"CN-XZ","Xizang Zizhiqu","autonomous_region",NULL)
            ,("CN","CHN",156,"CN-YN","Yunnan Sheng","province",NULL)
            ,("CN","CHN",156,"CN-ZJ","Zhejiang Sheng","province",NULL)
            ,("CO","COL",170,"CO-AMA","Amazonas","department",NULL)
            ,("CO","COL",170,"CO-ANT","Antioquia","department",NULL)
            ,("CO","COL",170,"CO-ARA","Arauca","department",NULL)
            ,("CO","COL",170,"CO-ATL","Atlántico","department",NULL)
            ,("CO","COL",170,"CO-BOL","Bolívar","department",NULL)
            ,("CO","COL",170,"CO-BOY","Boyacá","department",NULL)
            ,("CO","COL",170,"CO-CAL","Caldas","department",NULL)
            ,("CO","COL",170,"CO-CAQ","Caquetá","department",NULL)
            ,("CO","COL",170,"CO-CAS","Casanare","department",NULL)
            ,("CO","COL",170,"CO-CAU","Cauca","department",NULL)
            ,("CO","COL",170,"CO-CES","Cesar","department",NULL)
            ,("CO","COL",170,"CO-CHO","Chocó","department",NULL)
            ,("CO","COL",170,"CO-COR","Córdoba","department",NULL)
            ,("CO","COL",170,"CO-CUN","Cundinamarca","department",NULL)
            ,("CO","COL",170,"CO-DC",
                "Distrito Capital de Bogotá","capital_district",NULL)
            ,("CO","COL",170,"CO-GUA","Guainía","department",NULL)
            ,("CO","COL",170,"CO-GUV","Guaviare","department",NULL)
            ,("CO","COL",170,"CO-HUI","Huila","department",NULL)
            ,("CO","COL",170,"CO-LAG","La Guajira","department",NULL)
            ,("CO","COL",170,"CO-MAG","Magdalena","department",NULL)
            ,("CO","COL",170,"CO-MET","Meta","department",NULL)
            ,("CO","COL",170,"CO-NAR","Nariño","department",NULL)
            ,("CO","COL",170,"CO-NSA","Norte de Santander","department",NULL)
            ,("CO","COL",170,"CO-PUT","Putumayo","department",NULL)
            ,("CO","COL",170,"CO-QUI","Quindío","department",NULL)
            ,("CO","COL",170,"CO-RIS","Risaralda","department",NULL)
            ,("CO","COL",170,"CO-SAN","Santander","department",NULL)
            ,("CO","COL",170,"CO-SAP",
                "San Andrés, Providencia y Santa Catalina","department",NULL)
            ,("CO","COL",170,"CO-SUC","Sucre","department",NULL)
            ,("CO","COL",170,"CO-TOL","Tolima","department",NULL)
            ,("CO","COL",170,"CO-VAC","Valle del Cauca","department",NULL)
            ,("CO","COL",170,"CO-VAU","Vaupés","department",NULL)
            ,("CO","COL",170,"CO-VID","Vichada","department",NULL)
            ,("CR","CRI",188,"CR-A","Alajuela","province",NULL)
            ,("CR","CRI",188,"CR-C","Cartago","province",NULL)
            ,("CR","CRI",188,"CR-G","Guanacaste","province",NULL)
            ,("CR","CRI",188,"CR-H","Heredia","province",NULL)
            ,("CR","CRI",188,"CR-L","Limón","province",NULL)
            ,("CR","CRI",188,"CR-P","Puntarenas","province",NULL)
            ,("CR","CRI",188,"CR-SJ","San José","province",NULL)
            ,("CU","CUB",192,"CU-01","Pinar del Río","province",NULL)
            ,("CU","CUB",192,"CU-03","La Habana","province",NULL)
            ,("CU","CUB",192,"CU-04","Matanzas","province",NULL)
            ,("CU","CUB",192,"CU-05","Villa Clara","province",NULL)
            ,("CU","CUB",192,"CU-06","Cienfuegos","province",NULL)
            ,("CU","CUB",192,"CU-07","Sancti Spíritus","province",NULL)
            ,("CU","CUB",192,"CU-08","Ciego de Ávila","province",NULL)
            ,("CU","CUB",192,"CU-09","Camagüey","province",NULL)
            ,("CU","CUB",192,"CU-10","Las Tunas","province",NULL)
            ,("CU","CUB",192,"CU-11","Holguín","province",NULL)
            ,("CU","CUB",192,"CU-12","Granma","province",NULL)
            ,("CU","CUB",192,"CU-13","Santiago de Cuba","province",NULL)
            ,("CU","CUB",192,"CU-14","Guantánamo","province",NULL)
            ,("CU","CUB",192,"CU-15","Artemisa","province",NULL)
            ,("CU","CUB",192,"CU-16","Mayabeque","province",NULL)
            ,("CU","CUB",192,"CU-99",
                "Isla de la Juventud","special_municipality",NULL)
            ,("CV","CPV",132,"CV-B",
                "Ilhas de Barlavento","geographical_region",NULL)
            ,("CV","CPV",132,"CV-BR","Brava","municipality","CV-S")
            ,("CV","CPV",132,"CV-BV","Boa Vista","municipality","CV-B")
            ,("CV","CPV",132,"CV-CA","Santa Catarina","municipality","CV-S")
            ,("CV","CPV",132,"CV-CF",
                "Santa Catarina do Fogo","municipality","CV-S")
            ,("CV","CPV",132,"CV-CR","Santa Cruz","municipality","CV-S")
            ,("CV","CPV",132,"CV-MA","Maio","municipality","CV-S")
            ,("CV","CPV",132,"CV-MO","Mosteiros","municipality","CV-S")
            ,("CV","CPV",132,"CV-PA","Paul","municipality","CV-B")
            ,("CV","CPV",132,"CV-PN","Porto Novo","municipality","CV-B")
            ,("CV","CPV",132,"CV-PR","Praia","municipality","CV-S")
            ,("CV","CPV",132,"CV-RB","Ribeira Brava","municipality","CV-B")
            ,("CV","CPV",132,"CV-RG","Ribeira Grande","municipality","CV-B")
            ,("CV","CPV",132,"CV-RS",
                "Ribeira Grande de Santiago","municipality","CV-S")
            ,("CV","CPV",132,"CV-S",
                "Ilhas de Sotavento","geographical_region",NULL)
            ,("CV","CPV",132,"CV-SD","São Domingos","municipality","CV-S")
            ,("CV","CPV",132,"CV-SF","São Filipe","municipality","CV-S")
            ,("CV","CPV",132,"CV-SL","Sal","municipality","CV-B")
            ,("CV","CPV",132,"CV-SM","São Miguel","municipality","CV-S")
            ,("CV","CPV",132,"CV-SO",
                "São Lourenço dos Órgãos","municipality","CV-S")
            ,("CV","CPV",132,"CV-SS",
                "São Salvador do Mundo","municipality","CV-S")
            ,("CV","CPV",132,"CV-SV","São Vicente","municipality","CV-B")
            ,("CV","CPV",132,"CV-TA","Tarrafal","municipality","CV-S")
            ,("CV","CPV",132,"CV-TS",
                "Tarrafal de São Nicolau","municipality","CV-B")
            ,("CW","CUW",531,"CW-??","Curaçao","country",NULL)
            ,("CX","CXR",162,"CX-??","Christmas Island","country",NULL)
            ,("CY","CYP",196,"CY-01","Lefkosia","district",NULL)
            ,("CY","CYP",196,"CY-02","Lemesos","district",NULL)
            ,("CY","CYP",196,"CY-03","Larnaka","district",NULL)
            ,("CY","CYP",196,"CY-04","Ammochostos","district",NULL)
            ,("CY","CYP",196,"CY-05","Pafos","district",NULL)
            ,("CY","CYP",196,"CY-06","Keryneia","district",NULL)
            ,("CZ","CZE",203,"CZ-10","Praha, Hlavní město","capital_city",NULL)
            ,("CZ","CZE",203,"CZ-20","Středočeský kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-201","Benešov","district","CZ-20")
            ,("CZ","CZE",203,"CZ-202","Beroun","district","CZ-20")
            ,("CZ","CZE",203,"CZ-203","Kladno","district","CZ-20")
            ,("CZ","CZE",203,"CZ-204","Kolín","district","CZ-20")
            ,("CZ","CZE",203,"CZ-205","Kutná Hora","district","CZ-20")
            ,("CZ","CZE",203,"CZ-206","Mělník","district","CZ-20")
            ,("CZ","CZE",203,"CZ-207","Mladá Boleslav","district","CZ-20")
            ,("CZ","CZE",203,"CZ-208","Nymburk","district","CZ-20")
            ,("CZ","CZE",203,"CZ-209","Praha-východ","district","CZ-20")
            ,("CZ","CZE",203,"CZ-20A","Praha-západ","district","CZ-20")
            ,("CZ","CZE",203,"CZ-20B","Příbram","district","CZ-20")
            ,("CZ","CZE",203,"CZ-20C","Rakovník","district","CZ-20")
            ,("CZ","CZE",203,"CZ-31","Jihočeský kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-311","České Budějovice","district","CZ-31")
            ,("CZ","CZE",203,"CZ-312","Český Krumlov","district","CZ-31")
            ,("CZ","CZE",203,"CZ-313","Jindřichův Hradec","district","CZ-31")
            ,("CZ","CZE",203,"CZ-314","Písek","district","CZ-31")
            ,("CZ","CZE",203,"CZ-315","Prachatice","district","CZ-31")
            ,("CZ","CZE",203,"CZ-316","Strakonice","district","CZ-31")
            ,("CZ","CZE",203,"CZ-317","Tábor","district","CZ-31")
            ,("CZ","CZE",203,"CZ-32","Plzeňský kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-321","Domažlice","district","CZ-32")
            ,("CZ","CZE",203,"CZ-322","Klatovy","district","CZ-32")
            ,("CZ","CZE",203,"CZ-323","Plzeň-město","district","CZ-32")
            ,("CZ","CZE",203,"CZ-324","Plzeň-jih","district","CZ-32")
            ,("CZ","CZE",203,"CZ-325","Plzeň-sever","district","CZ-32")
            ,("CZ","CZE",203,"CZ-326","Rokycany","district","CZ-32")
            ,("CZ","CZE",203,"CZ-327","Tachov","district","CZ-32")
            ,("CZ","CZE",203,"CZ-41","Karlovarský kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-411","Cheb","district","CZ-41")
            ,("CZ","CZE",203,"CZ-412","Karlovy Vary","district","CZ-41")
            ,("CZ","CZE",203,"CZ-413","Sokolov","district","CZ-41")
            ,("CZ","CZE",203,"CZ-42","Ústecký kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-421","Děčín","district","CZ-42")
            ,("CZ","CZE",203,"CZ-422","Chomutov","district","CZ-42")
            ,("CZ","CZE",203,"CZ-423","Litoměřice","district","CZ-42")
            ,("CZ","CZE",203,"CZ-424","Louny","district","CZ-42")
            ,("CZ","CZE",203,"CZ-425","Most","district","CZ-42")
            ,("CZ","CZE",203,"CZ-426","Teplice","district","CZ-42")
            ,("CZ","CZE",203,"CZ-427","Ústí nad Labem","district","CZ-42")
            ,("CZ","CZE",203,"CZ-51","Liberecký kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-511","Česká Lípa","district","CZ-51")
            ,("CZ","CZE",203,"CZ-512","Jablonec nad Nisou","district","CZ-51")
            ,("CZ","CZE",203,"CZ-513","Liberec","district","CZ-51")
            ,("CZ","CZE",203,"CZ-514","Semily","district","CZ-51")
            ,("CZ","CZE",203,"CZ-52","Královéhradecký kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-521","Hradec Králové","district","CZ-52")
            ,("CZ","CZE",203,"CZ-522","Jičín","district","CZ-52")
            ,("CZ","CZE",203,"CZ-523","Náchod","district","CZ-52")
            ,("CZ","CZE",203,"CZ-524","Rychnov nad Kněžnou","district","CZ-52")
            ,("CZ","CZE",203,"CZ-525","Trutnov","district","CZ-52")
            ,("CZ","CZE",203,"CZ-53","Pardubický kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-531","Chrudim","district","CZ-53")
            ,("CZ","CZE",203,"CZ-532","Pardubice","district","CZ-53")
            ,("CZ","CZE",203,"CZ-533","Svitavy","district","CZ-53")
            ,("CZ","CZE",203,"CZ-534","Ústí nad Orlicí","district","CZ-53")
            ,("CZ","CZE",203,"CZ-63","Kraj Vysočina","region",NULL)
            ,("CZ","CZE",203,"CZ-631","Havlíčkův Brod","district","CZ-63")
            ,("CZ","CZE",203,"CZ-632","Jihlava","district","CZ-63")
            ,("CZ","CZE",203,"CZ-633","Pelhřimov","district","CZ-63")
            ,("CZ","CZE",203,"CZ-634","Třebíč","district","CZ-63")
            ,("CZ","CZE",203,"CZ-635","Žďár nad Sázavou","district","CZ-63")
            ,("CZ","CZE",203,"CZ-64","Jihomoravský kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-641","Blansko","district","CZ-64")
            ,("CZ","CZE",203,"CZ-642","Brno-město","district","CZ-64")
            ,("CZ","CZE",203,"CZ-643","Brno-venkov","district","CZ-64")
            ,("CZ","CZE",203,"CZ-644","Břeclav","district","CZ-64")
            ,("CZ","CZE",203,"CZ-645","Hodonín","district","CZ-64")
            ,("CZ","CZE",203,"CZ-646","Vyškov","district","CZ-64")
            ,("CZ","CZE",203,"CZ-647","Znojmo","district","CZ-64")
            ,("CZ","CZE",203,"CZ-71","Olomoucký kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-711","Jeseník","district","CZ-71")
            ,("CZ","CZE",203,"CZ-712","Olomouc","district","CZ-71")
            ,("CZ","CZE",203,"CZ-713","Prostějov","district","CZ-71")
            ,("CZ","CZE",203,"CZ-714","Přerov","district","CZ-71")
            ,("CZ","CZE",203,"CZ-715","Šumperk","district","CZ-71")
            ,("CZ","CZE",203,"CZ-72","Zlínský kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-721","Kroměříž","district","CZ-72")
            ,("CZ","CZE",203,"CZ-722","Uherské Hradiště","district","CZ-72")
            ,("CZ","CZE",203,"CZ-723","Vsetín","district","CZ-72")
            ,("CZ","CZE",203,"CZ-724","Zlín","district","CZ-72")
            ,("CZ","CZE",203,"CZ-80","Moravskoslezský kraj","region",NULL)
            ,("CZ","CZE",203,"CZ-801","Bruntál","district","CZ-80")
            ,("CZ","CZE",203,"CZ-802","Frýdek-Místek","district","CZ-80")
            ,("CZ","CZE",203,"CZ-803","Karviná","district","CZ-80")
            ,("CZ","CZE",203,"CZ-804","Nový Jičín","district","CZ-80")
            ,("CZ","CZE",203,"CZ-805","Opava","district","CZ-80")
            ,("CZ","CZE",203,"CZ-806","Ostrava-město","district","CZ-80")
            ,("DE","DEU",276,"DE-BB","Brandenburg","state",NULL)
            ,("DE","DEU",276,"DE-BE","Berlin","state",NULL)
            ,("DE","DEU",276,"DE-BW","Baden-Württemberg","state",NULL)
            ,("DE","DEU",276,"DE-BY","Bayern","state",NULL)
            ,("DE","DEU",276,"DE-HB","Bremen","state",NULL)
            ,("DE","DEU",276,"DE-HE","Hessen","state",NULL)
            ,("DE","DEU",276,"DE-HH","Hamburg","state",NULL)
            ,("DE","DEU",276,"DE-MV","Mecklenburg-Vorpommern","state",NULL)
            ,("DE","DEU",276,"DE-NI","Niedersachsen","state",NULL)
            ,("DE","DEU",276,"DE-NW","Nordrhein-Westfalen","state",NULL)
            ,("DE","DEU",276,"DE-RP","Rheinland-Pfalz","state",NULL)
            ,("DE","DEU",276,"DE-SH","Schleswig-Holstein","state",NULL)
            ,("DE","DEU",276,"DE-SL","Saarland","state",NULL)
            ,("DE","DEU",276,"DE-SN","Sachsen","state",NULL)
            ,("DE","DEU",276,"DE-ST","Sachsen-Anhalt","state",NULL)
            ,("DE","DEU",276,"DE-TH","Thüringen","state",NULL)
            ,("DJ","DJI",262,"DJ-AR","Arta","region",NULL)
            ,("DJ","DJI",262,"DJ-AS","Ali Sabieh","region",NULL)
            ,("DJ","DJI",262,"DJ-DI","Dikhil","city",NULL)
            ,("DJ","DJI",262,"DJ-DJ","Djibouti","region",NULL)
            ,("DJ","DJI",262,"DJ-OB","Obock","region",NULL)
            ,("DJ","DJI",262,"DJ-TA","Tadjourah","region",NULL)
            ,("DK","DNK",208,"DK-81","Nordjylland","region",NULL)
            ,("DK","DNK",208,"DK-82","Midtjylland","region",NULL)
            ,("DK","DNK",208,"DK-83","Syddanmark","region",NULL)
            ,("DK","DNK",208,"DK-84","Hovedstaden","region",NULL)
            ,("DK","DNK",208,"DK-85","Sjælland","region",NULL)
            ,("DM","DMA",212,"DM-02","Saint Andrew","parish",NULL)
            ,("DM","DMA",212,"DM-03","Saint David","parish",NULL)
            ,("DM","DMA",212,"DM-04","Saint George","parish",NULL)
            ,("DM","DMA",212,"DM-05","Saint John","parish",NULL)
            ,("DM","DMA",212,"DM-06","Saint Joseph","parish",NULL)
            ,("DM","DMA",212,"DM-07","Saint Luke","parish",NULL)
            ,("DM","DMA",212,"DM-08","Saint Mark","parish",NULL)
            ,("DM","DMA",212,"DM-09","Saint Patrick","parish",NULL)
            ,("DM","DMA",212,"DM-10","Saint Paul","parish",NULL)
            ,("DM","DMA",212,"DM-11","Saint Peter","parish",NULL)
            ,("DO","DOM",214,"DO-01",
                "Distrito Nacional (Santo Domingo)","district","DO-40")
            ,("DO","DOM",214,"DO-02","Azua","province","DO-41")
            ,("DO","DOM",214,"DO-03","Baoruco","province","DO-38")
            ,("DO","DOM",214,"DO-04","Barahona","province","DO-38")
            ,("DO","DOM",214,"DO-05","Dajabón","province","DO-34")
            ,("DO","DOM",214,"DO-06","Duarte","province","DO-33")
            ,("DO","DOM",214,"DO-07","Elías Piña","province","DO-37")
            ,("DO","DOM",214,"DO-08","El Seibo","province","DO-42")
            ,("DO","DOM",214,"DO-09","Espaillat","province","DO-35")
            ,("DO","DOM",214,"DO-10","Independencia","province","DO-38")
            ,("DO","DOM",214,"DO-11","La Altagracia","province","DO-42")
            ,("DO","DOM",214,"DO-12","La Romana","province","DO-42")
            ,("DO","DOM",214,"DO-13","La Vega","province","DO-36")
            ,("DO","DOM",214,"DO-14",
                "María Trinidad Sánchez","province","DO-33")
            ,("DO","DOM",214,"DO-15","Monte Cristi","province","DO-34")
            ,("DO","DOM",214,"DO-16","Pedernales","province","DO-38")
            ,("DO","DOM",214,"DO-17","Peravia","province","DO-41")
            ,("DO","DOM",214,"DO-18","Puerto Plata","province","DO-35")
            ,("DO","DOM",214,"DO-19","Hermanas Mirabal","province","DO-33")
            ,("DO","DOM",214,"DO-20","Samaná","province","DO-33")
            ,("DO","DOM",214,"DO-21","San Cristóbal","province","DO-41")
            ,("DO","DOM",214,"DO-22","San Juan","province","DO-37")
            ,("DO","DOM",214,"DO-23","San Pedro de Macorís","province","DO-39")
            ,("DO","DOM",214,"DO-24","Sánchez Ramírez","province","DO-36")
            ,("DO","DOM",214,"DO-25","Santiago","province","DO-35")
            ,("DO","DOM",214,"DO-26","Santiago Rodríguez","province","DO-34")
            ,("DO","DOM",214,"DO-27","Valverde","province","DO-34")
            ,("DO","DOM",214,"DO-28","Monseñor Nouel","province","DO-36")
            ,("DO","DOM",214,"DO-29","Monte Plata","province","DO-39")
            ,("DO","DOM",214,"DO-30","Hato Mayor","province","DO-39")
            ,("DO","DOM",214,"DO-31","San José de Ocoa","province","DO-41")
            ,("DO","DOM",214,"DO-32","Santo Domingo","province","DO-40")
            ,("DO","DOM",214,"DO-33","Cibao Nordeste","region",NULL)
            ,("DO","DOM",214,"DO-34","Cibao Noroeste","region",NULL)
            ,("DO","DOM",214,"DO-35","Cibao Norte","region",NULL)
            ,("DO","DOM",214,"DO-36","Cibao Sur","region",NULL)
            ,("DO","DOM",214,"DO-37","El Valle","region",NULL)
            ,("DO","DOM",214,"DO-38","Enriquillo","region",NULL)
            ,("DO","DOM",214,"DO-39","Higuamo","region",NULL)
            ,("DO","DOM",214,"DO-40","Ozama","region",NULL)
            ,("DO","DOM",214,"DO-41","Valdesia","region",NULL)
            ,("DO","DOM",214,"DO-42","Yuma","region",NULL)
            ,("DZ","DZA",12,"DZ-01","Adrar","province",NULL)
            ,("DZ","DZA",12,"DZ-02","Chlef","province",NULL)
            ,("DZ","DZA",12,"DZ-03","Laghouat","province",NULL)
            ,("DZ","DZA",12,"DZ-04","Oum el Bouaghi","province",NULL)
            ,("DZ","DZA",12,"DZ-05","Batna","province",NULL)
            ,("DZ","DZA",12,"DZ-06","Béjaïa","province",NULL)
            ,("DZ","DZA",12,"DZ-07","Biskra","province",NULL)
            ,("DZ","DZA",12,"DZ-08","Béchar","province",NULL)
            ,("DZ","DZA",12,"DZ-09","Blida","province",NULL)
            ,("DZ","DZA",12,"DZ-10","Bouira","province",NULL)
            ,("DZ","DZA",12,"DZ-11","Tamanrasset","province",NULL)
            ,("DZ","DZA",12,"DZ-12","Tébessa","province",NULL)
            ,("DZ","DZA",12,"DZ-13","Tlemcen","province",NULL)
            ,("DZ","DZA",12,"DZ-14","Tiaret","province",NULL)
            ,("DZ","DZA",12,"DZ-15","Tizi Ouzou","province",NULL)
            ,("DZ","DZA",12,"DZ-16","Alger","province",NULL)
            ,("DZ","DZA",12,"DZ-17","Djelfa","province",NULL)
            ,("DZ","DZA",12,"DZ-18","Jijel","province",NULL)
            ,("DZ","DZA",12,"DZ-19","Sétif","province",NULL)
            ,("DZ","DZA",12,"DZ-20","Saïda","province",NULL)
            ,("DZ","DZA",12,"DZ-21","Skikda","province",NULL)
            ,("DZ","DZA",12,"DZ-22","Sidi Bel Abbès","province",NULL)
            ,("DZ","DZA",12,"DZ-23","Annaba","province",NULL)
            ,("DZ","DZA",12,"DZ-24","Guelma","province",NULL)
            ,("DZ","DZA",12,"DZ-25","Constantine","province",NULL)
            ,("DZ","DZA",12,"DZ-26","Médéa","province",NULL)
            ,("DZ","DZA",12,"DZ-27","Mostaganem","province",NULL)
            ,("DZ","DZA",12,"DZ-28","M'sila","province",NULL)
            ,("DZ","DZA",12,"DZ-29","Mascara","province",NULL)
            ,("DZ","DZA",12,"DZ-30","Ouargla","province",NULL)
            ,("DZ","DZA",12,"DZ-31","Oran","province",NULL)
            ,("DZ","DZA",12,"DZ-32","El Bayadh","province",NULL)
            ,("DZ","DZA",12,"DZ-33","Illizi","province",NULL)
            ,("DZ","DZA",12,"DZ-34","Bordj Bou Arréridj","province",NULL)
            ,("DZ","DZA",12,"DZ-35","Boumerdès","province",NULL)
            ,("DZ","DZA",12,"DZ-36","El Tarf","province",NULL)
            ,("DZ","DZA",12,"DZ-37","Tindouf","province",NULL)
            ,("DZ","DZA",12,"DZ-38","Tissemsilt","province",NULL)
            ,("DZ","DZA",12,"DZ-39","El Oued","province",NULL)
            ,("DZ","DZA",12,"DZ-40","Khenchela","province",NULL)
            ,("DZ","DZA",12,"DZ-41","Souk Ahras","province",NULL)
            ,("DZ","DZA",12,"DZ-42","Tipaza","province",NULL)
            ,("DZ","DZA",12,"DZ-43","Mila","province",NULL)
            ,("DZ","DZA",12,"DZ-44","Aïn Defla","province",NULL)
            ,("DZ","DZA",12,"DZ-45","Naama","province",NULL)
            ,("DZ","DZA",12,"DZ-46","Aïn Témouchent","province",NULL)
            ,("DZ","DZA",12,"DZ-47","Ghardaïa","province",NULL)
            ,("DZ","DZA",12,"DZ-48","Relizane","province",NULL)
            ,("DZ","DZA",12,"DZ-49","Timimoun","province",NULL)
            ,("DZ","DZA",12,"DZ-50","Bordj Badji Mokhtar","province",NULL)
            ,("DZ","DZA",12,"DZ-51","Ouled Djellal","province",NULL)
            ,("DZ","DZA",12,"DZ-52","Béni Abbès","province",NULL)
            ,("DZ","DZA",12,"DZ-53","In Salah","province",NULL)
            ,("DZ","DZA",12,"DZ-54","In Guezzam","province",NULL)
            ,("DZ","DZA",12,"DZ-55","Touggourt","province",NULL)
            ,("DZ","DZA",12,"DZ-56","Djanet","province",NULL)
            ,("DZ","DZA",12,"DZ-57","El Meghaier","province",NULL)
            ,("DZ","DZA",12,"DZ-58","El Meniaa","province",NULL)
            ,("EC","ECU",218,"EC-A","Azuay","province",NULL)
            ,("EC","ECU",218,"EC-B","Bolívar","province",NULL)
            ,("EC","ECU",218,"EC-C","Carchi","province",NULL)
            ,("EC","ECU",218,"EC-D","Orellana","province",NULL)
            ,("EC","ECU",218,"EC-E","Esmeraldas","province",NULL)
            ,("EC","ECU",218,"EC-F","Cañar","province",NULL)
            ,("EC","ECU",218,"EC-G","Guayas","province",NULL)
            ,("EC","ECU",218,"EC-H","Chimborazo","province",NULL)
            ,("EC","ECU",218,"EC-I","Imbabura","province",NULL)
            ,("EC","ECU",218,"EC-L","Loja","province",NULL)
            ,("EC","ECU",218,"EC-M","Manabí","province",NULL)
            ,("EC","ECU",218,"EC-N","Napo","province",NULL)
            ,("EC","ECU",218,"EC-O","El Oro","province",NULL)
            ,("EC","ECU",218,"EC-P","Pichincha","province",NULL)
            ,("EC","ECU",218,"EC-R","Los Ríos","province",NULL)
            ,("EC","ECU",218,"EC-S","Morona Santiago","province",NULL)
            ,("EC","ECU",218,"EC-SD",
                "Santo Domingo de los Tsáchilas","province",NULL)
            ,("EC","ECU",218,"EC-SE","Santa Elena","province",NULL)
            ,("EC","ECU",218,"EC-T","Tungurahua","province",NULL)
            ,("EC","ECU",218,"EC-U","Sucumbíos","province",NULL)
            ,("EC","ECU",218,"EC-W","Galápagos","province",NULL)
            ,("EC","ECU",218,"EC-X","Cotopaxi","province",NULL)
            ,("EC","ECU",218,"EC-Y","Pastaza","province",NULL)
            ,("EC","ECU",218,"EC-Z","Zamora Chinchipe","province",NULL)
            ,("EE","EST",233,"EE-130","Alutaguse","rural_municipality","EE-45")
            ,("EE","EST",233,"EE-141","Anija","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-142","Antsla","rural_municipality","EE-87")
            ,("EE","EST",233,"EE-171","Elva","rural_municipality","EE-79")
            ,("EE","EST",233,"EE-184","Haapsalu","urban_municipality","EE-56")
            ,("EE","EST",233,"EE-191","Haljala","rural_municipality","EE-60")
            ,("EE","EST",233,"EE-198","Harku","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-205","Hiiumaa","rural_municipality","EE-39")
            ,("EE","EST",233,"EE-214","Häädemeeste","rural_municipality","EE-68")
            ,("EE","EST",233,"EE-245","Jõelähtme","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-247","Jõgeva","rural_municipality","EE-50")
            ,("EE","EST",233,"EE-251","Jõhvi","rural_municipality","EE-45")
            ,("EE","EST",233,"EE-255","Järva","rural_municipality","EE-52")
            ,("EE","EST",233,"EE-272","Kadrina","rural_municipality","EE-60")
            ,("EE","EST",233,"EE-283","Kambja","rural_municipality","EE-79")
            ,("EE","EST",233,"EE-284","Kanepi","rural_municipality","EE-64")
            ,("EE","EST",233,"EE-291","Kastre","rural_municipality","EE-79")
            ,("EE","EST",233,"EE-293","Kehtna","rural_municipality","EE-71")
            ,("EE","EST",233,"EE-296","Keila","urban_municipality","EE-37")
            ,("EE","EST",233,"EE-303","Kihnu","rural_municipality","EE-68")
            ,("EE","EST",233,"EE-305","Kiili","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-317","Kohila","rural_municipality","EE-71")
            ,("EE","EST",233,"EE-321","Kohtla-Järve","urban_municipality","EE-45")
            ,("EE","EST",233,"EE-338","Kose","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-353","Kuusalu","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-37","Harjumaa","county",NULL)
            ,("EE","EST",233,"EE-39","Hiiumaa","county",NULL)
            ,("EE","EST",233,"EE-424","Loksa","urban_municipality","EE-37")
            ,("EE","EST",233,"EE-430","Lääneranna","rural_municipality","EE-68")
            ,("EE","EST",233,"EE-431","Lääne-Harju","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-432","Luunja","rural_municipality","EE-79")
            ,("EE","EST",233,"EE-441","Lääne-Nigula","rural_municipality","EE-56")
            ,("EE","EST",233,"EE-442","Lüganuse","rural_municipality","EE-45")
            ,("EE","EST",233,"EE-446","Maardu","urban_municipality","EE-37")
            ,("EE","EST",233,"EE-45","Ida-Virumaa","county",NULL)
            ,("EE","EST",233,"EE-478","Muhu","rural_municipality","EE-74")
            ,("EE","EST",233,"EE-480","Mulgi","rural_municipality","EE-84")
            ,("EE","EST",233,"EE-486","Mustvee","rural_municipality","EE-50")
            ,("EE","EST",233,"EE-50","Jõgevamaa","county",NULL)
            ,("EE","EST",233,"EE-503","Märjamaa","rural_municipality","EE-71")
            ,("EE","EST",233,"EE-511","Narva","urban_municipality","EE-45")
            ,("EE","EST",233,"EE-514","Narva-Jõesuu","urban_municipality","EE-45")
            ,("EE","EST",233,"EE-52","Järvamaa","county",NULL)
            ,("EE","EST",233,"EE-528","Nõo","rural_municipality","EE-79")
            ,("EE","EST",233,"EE-557","Otepää","rural_municipality","EE-81")
            ,("EE","EST",233,"EE-56","Läänemaa","county",NULL)
            ,("EE","EST",233,"EE-567","Paide","urban_municipality","EE-52")
            ,("EE","EST",233,"EE-586","Peipsiääre","rural_municipality","EE-79")
            ,("EE","EST",233,"EE-60","Lääne-Virumaa","county",NULL)
            ,("EE","EST",233,"EE-615","Põhja-Sakala","rural_municipality","EE-84")
            ,("EE","EST",233,"EE-618","Põltsamaa","rural_municipality","EE-50")
            ,("EE","EST",233,"EE-622","Põlva","rural_municipality","EE-64")
            ,("EE","EST",233,"EE-624","Pärnu","urban_municipality","EE-68")
            ,("EE","EST",233,"EE-638","Põhja-Pärnumaa","rural_municipality","EE-68")
            ,("EE","EST",233,"EE-64","Põlvamaa","county",NULL)
            ,("EE","EST",233,"EE-651","Raasiku","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-653","Rae","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-661","Rakvere","rural_municipality","EE-60")
            ,("EE","EST",233,"EE-663","Rakvere","urban_municipality","EE-60")
            ,("EE","EST",233,"EE-668","Rapla","rural_municipality","EE-71")
            ,("EE","EST",233,"EE-68","Pärnumaa","county",NULL)
            ,("EE","EST",233,"EE-689","Ruhnu","rural_municipality","EE-74")
            ,("EE","EST",233,"EE-698","Rõuge","rural_municipality","EE-87")
            ,("EE","EST",233,"EE-708","Räpina","rural_municipality","EE-64")
            ,("EE","EST",233,"EE-71","Raplamaa","county",NULL)
            ,("EE","EST",233,"EE-712","Saarde","rural_municipality","EE-68")
            ,("EE","EST",233,"EE-714","Saaremaa","rural_municipality","EE-74")
            ,("EE","EST",233,"EE-719","Saku","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-726","Saue","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-732","Setomaa","rural_municipality","EE-87")
            ,("EE","EST",233,"EE-735","Sillamäe","urban_municipality","EE-45")
            ,("EE","EST",233,"EE-74","Saaremaa","county",NULL)
            ,("EE","EST",233,"EE-784","Tallinn","urban_municipality","EE-37")
            ,("EE","EST",233,"EE-79","Tartumaa","county",NULL)
            ,("EE","EST",233,"EE-792","Tapa","rural_municipality","EE-60")
            ,("EE","EST",233,"EE-793","Tartu","urban_municipality","EE-79")
            ,("EE","EST",233,"EE-796","Tartu","rural_municipality","EE-79")
            ,("EE","EST",233,"EE-803","Toila","rural_municipality","EE-45")
            ,("EE","EST",233,"EE-809","Tori","rural_municipality","EE-68")
            ,("EE","EST",233,"EE-81","Valgamaa","county",NULL)
            ,("EE","EST",233,"EE-824","Tõrva","rural_municipality","EE-81")
            ,("EE","EST",233,"EE-834","Türi","rural_municipality","EE-52")
            ,("EE","EST",233,"EE-84","Viljandimaa","county",NULL)
            ,("EE","EST",233,"EE-855","Valga","rural_municipality","EE-81")
            ,("EE","EST",233,"EE-87","Võrumaa","county",NULL)
            ,("EE","EST",233,"EE-890","Viimsi","rural_municipality","EE-37")
            ,("EE","EST",233,"EE-897","Viljandi","urban_municipality","EE-84")
            ,("EE","EST",233,"EE-899","Viljandi","rural_municipality","EE-84")
            ,("EE","EST",233,"EE-901","Vinni","rural_municipality","EE-60")
            ,("EE","EST",233,"EE-903","Viru-Nigula","rural_municipality","EE-60")
            ,("EE","EST",233,"EE-907","Vormsi","rural_municipality","EE-56")
            ,("EE","EST",233,"EE-917","Võru","rural_municipality","EE-87")
            ,("EE","EST",233,"EE-919","Võru","urban_municipality","EE-87")
            ,("EE","EST",233,"EE-928","Väike-Maarja","rural_municipality","EE-60")
            ,("EG","EGY",818,"EG-ALX","Al Iskandarīyah","governorate",NULL)
            ,("EG","EGY",818,"EG-ASN","Aswān","governorate",NULL)
            ,("EG","EGY",818,"EG-AST","Asyūţ","governorate",NULL)
            ,("EG","EGY",818,"EG-BA","Al Baḩr al Aḩmar","governorate",NULL)
            ,("EG","EGY",818,"EG-BH","Al Buḩayrah","governorate",NULL)
            ,("EG","EGY",818,"EG-BNS","Banī Suwayf","governorate",NULL)
            ,("EG","EGY",818,"EG-C","Al Qāhirah","governorate",NULL)
            ,("EG","EGY",818,"EG-DK","Ad Daqahlīyah","governorate",NULL)
            ,("EG","EGY",818,"EG-DT","Dumyāţ","governorate",NULL)
            ,("EG","EGY",818,"EG-FYM","Al Fayyūm","governorate",NULL)
            ,("EG","EGY",818,"EG-GH","Al Gharbīyah","governorate",NULL)
            ,("EG","EGY",818,"EG-GZ","Al Jīzah","governorate",NULL)
            ,("EG","EGY",818,"EG-IS","Al Ismā'īlīyah","governorate",NULL)
            ,("EG","EGY",818,"EG-JS","Janūb Sīnā'","governorate",NULL)
            ,("EG","EGY",818,"EG-KB","Al Qalyūbīyah","governorate",NULL)
            ,("EG","EGY",818,"EG-KFS","Kafr ash Shaykh","governorate",NULL)
            ,("EG","EGY",818,"EG-KN","Qinā","governorate",NULL)
            ,("EG","EGY",818,"EG-LX","Al Uqşur","governorate",NULL)
            ,("EG","EGY",818,"EG-MN","Al Minyā","governorate",NULL)
            ,("EG","EGY",818,"EG-MNF","Al Minūfīyah","governorate",NULL)
            ,("EG","EGY",818,"EG-MT","Maţrūḩ","governorate",NULL)
            ,("EG","EGY",818,"EG-PTS","Būr Sa'īd","governorate",NULL)
            ,("EG","EGY",818,"EG-SHG","Sūhāj","governorate",NULL)
            ,("EG","EGY",818,"EG-SHR","Ash Sharqīyah","governorate",NULL)
            ,("EG","EGY",818,"EG-SIN","Shamāl Sīnā'","governorate",NULL)
            ,("EG","EGY",818,"EG-SUZ","As Suways","governorate",NULL)
            ,("EG","EGY",818,"EG-WAD","Al Wādī al Jadīd","governorate",NULL)
            ,("ER","ERI",232,"ER-AN","Ansabā","region",NULL)
            ,("ER","ERI",232,"ER-DK","Janūbī al Baḩrī al Aḩmar","region",NULL)
            ,("ER","ERI",232,"ER-DU","Al Janūbī","region",NULL)
            ,("ER","ERI",232,"ER-GB","Qāsh-Barkah","region",NULL)
            ,("ER","ERI",232,"ER-MA","Al Awsaţ","region",NULL)
            ,("ER","ERI",232,"ER-SK","Shimālī al Baḩrī al Aḩmar","region",NULL)
            ,("ES","ESP",724,"ES-A","Alicante","province","ES-VC")
            ,("ES","ESP",724,"ES-AB","Albacete","province","ES-CM")
            ,("ES","ESP",724,"ES-AL","Almería","province","ES-AN")
            ,("ES","ESP",724,"ES-AN","Andalucía","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-AR","Aragón","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-AS",
                "Asturias, Principado de","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-AV","Ávila","province","ES-CL")
            ,("ES","ESP",724,"ES-B","Barcelona","province","ES-CT")
            ,("ES","ESP",724,"ES-BA","Badajoz","province","ES-EX")
            ,("ES","ESP",724,"ES-BI","Bizkaia","province","ES-PV")
            ,("ES","ESP",724,"ES-BU","Burgos","province","ES-CL")
            ,("ES","ESP",724,"ES-C","A Coruña","province","ES-GA")
            ,("ES","ESP",724,"ES-CA","Cádiz","province","ES-AN")
            ,("ES","ESP",724,"ES-CB","Cantabria","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-CC","Cáceres","province","ES-EX")
            ,("ES","ESP",724,"ES-CE","Ceuta","autonomous_north_africa_city",NULL)
            ,("ES","ESP",724,"ES-CL",
                "Castilla y León","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-CM",
                "Castilla-La Mancha","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-CN","Canarias","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-CO","Córdoba","province","ES-AN")
            ,("ES","ESP",724,"ES-CR","Ciudad Real","province","ES-CM")
            ,("ES","ESP",724,"ES-CS","Castellón","province","ES-VC")
            ,("ES","ESP",724,"ES-CT","Catalunya","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-CU","Cuenca","province","ES-CM")
            ,("ES","ESP",724,"ES-EX","Extremadura","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-GA","Galicia","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-GC","Las Palmas","province","ES-CN")
            ,("ES","ESP",724,"ES-GI","Girona","province","ES-CT")
            ,("ES","ESP",724,"ES-GR","Granada","province","ES-AN")
            ,("ES","ESP",724,"ES-GU","Guadalajara","province","ES-CM")
            ,("ES","ESP",724,"ES-H","Huelva","province","ES-AN")
            ,("ES","ESP",724,"ES-HU","Huesca","province","ES-AR")
            ,("ES","ESP",724,"ES-IB",
                "Illes Balears","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-J","Jaén","province","ES-AN")
            ,("ES","ESP",724,"ES-L","Lleida","province","ES-CT")
            ,("ES","ESP",724,"ES-LE","León","province","ES-CL")
            ,("ES","ESP",724,"ES-LO","La Rioja","province","ES-RI")
            ,("ES","ESP",724,"ES-LU","Lugo","province","ES-GA")
            ,("ES","ESP",724,"ES-M","Madrid","province","ES-MD")
            ,("ES","ESP",724,"ES-MA","Málaga","province","ES-AN")
            ,("ES","ESP",724,"ES-MC",
                "Murcia, Región de","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-MD",
                "Madrid, Comunidad de","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-ML","Melilla","autonomous_north_africa_city",NULL)
            ,("ES","ESP",724,"ES-MU","Murcia","province","ES-MC")
            ,("ES","ESP",724,"ES-NA","Navarra","province","ES-NC")
            ,("ES","ESP",724,"ES-NC",
                "Navarra, Comunidad Foral de","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-O","Asturias","province","ES-AS")
            ,("ES","ESP",724,"ES-OR","Ourense","province","ES-GA")
            ,("ES","ESP",724,"ES-P","Palencia","province","ES-CL")
            ,("ES","ESP",724,"ES-PM","Illes Balears","province","ES-IB")
            ,("ES","ESP",724,"ES-PO","Pontevedra","province","ES-GA")
            ,("ES","ESP",724,"ES-PV","País Vasco","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-RI","La Rioja","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-S","Cantabria","province","ES-CB")
            ,("ES","ESP",724,"ES-SA","Salamanca","province","ES-CL")
            ,("ES","ESP",724,"ES-SE","Sevilla","province","ES-AN")
            ,("ES","ESP",724,"ES-SG","Segovia","province","ES-CL")
            ,("ES","ESP",724,"ES-SO","Soria","province","ES-CL")
            ,("ES","ESP",724,"ES-SS","Gipuzkoa","province","ES-PV")
            ,("ES","ESP",724,"ES-T","Tarragona","province","ES-CT")
            ,("ES","ESP",724,"ES-TE","Teruel","province","ES-AR")
            ,("ES","ESP",724,"ES-TF",
                "Santa Cruz de Tenerife","province","ES-CN")
            ,("ES","ESP",724,"ES-TO","Toledo","province","ES-CM")
            ,("ES","ESP",724,"ES-V","Valencia","province","ES-VC")
            ,("ES","ESP",724,"ES-VA","Valladolid","province","ES-CL")
            ,("ES","ESP",724,"ES-VC",
                "Valenciana, Comunidad","autonomous_community",NULL)
            ,("ES","ESP",724,"ES-VI","Álava","province","ES-PV")
            ,("ES","ESP",724,"ES-Z","Zaragoza","province","ES-AR")
            ,("ES","ESP",724,"ES-ZA","Zamora","province","ES-CL")
            ,("ET","ETH",231,"ET-AA","Ādīs Ābeba","administration",NULL)
            ,("ET","ETH",231,"ET-AF","Āfar","regional_state",NULL)
            ,("ET","ETH",231,"ET-AM","Āmara","regional_state",NULL)
            ,("ET","ETH",231,"ET-BE","Bīnshangul Gumuz","regional_state",NULL)
            ,("ET","ETH",231,"ET-DD","Dirē Dawa","administration",NULL)
            ,("ET","ETH",231,"ET-GA","Gambēla Hizboch","regional_state",NULL)
            ,("ET","ETH",231,"ET-HA","Hārerī Hizb","regional_state",NULL)
            ,("ET","ETH",231,"ET-OR","Oromīya","regional_state",NULL)
            ,("ET","ETH",231,"ET-SI","Sīdama","regional_state",NULL)
            ,("ET","ETH",231,"ET-SN",
                "YeDebub Bihēroch Bihēreseboch na Hizboch",
                "regional_state",NULL)
            ,("ET","ETH",231,"ET-SO","Sumalē","regional_state",NULL)
            ,("ET","ETH",231,"ET-SW",
                "YeDebub M'irab Ītyop'iya Hizboch","regional_state",NULL)
            ,("ET","ETH",231,"ET-TI","Tigray","regional_state",NULL)
            ,("FI","FIN",246,"FI-01","Ahvenanmaan maakunta","region",NULL)
            ,("FI","FIN",246,"FI-02","Etelä-Karjala","region",NULL)
            ,("FI","FIN",246,"FI-03","Etelä-Pohjanmaa","region",NULL)
            ,("FI","FIN",246,"FI-04","Etelä-Savo","region",NULL)
            ,("FI","FIN",246,"FI-05","Kainuu","region",NULL)
            ,("FI","FIN",246,"FI-06","Kanta-Häme","region",NULL)
            ,("FI","FIN",246,"FI-07","Keski-Pohjanmaa","region",NULL)
            ,("FI","FIN",246,"FI-08","Keski-Suomi","region",NULL)
            ,("FI","FIN",246,"FI-09","Kymenlaakso","region",NULL)
            ,("FI","FIN",246,"FI-10","Lappi","region",NULL)
            ,("FI","FIN",246,"FI-11","Pirkanmaa","region",NULL)
            ,("FI","FIN",246,"FI-12","Pohjanmaa","region",NULL)
            ,("FI","FIN",246,"FI-13","Pohjois-Karjala","region",NULL)
            ,("FI","FIN",246,"FI-14","Pohjois-Pohjanmaa","region",NULL)
            ,("FI","FIN",246,"FI-15","Pohjois-Savo","region",NULL)
            ,("FI","FIN",246,"FI-16","Päijät-Häme","region",NULL)
            ,("FI","FIN",246,"FI-17","Satakunta","region",NULL)
            ,("FI","FIN",246,"FI-18","Uusimaa","region",NULL)
            ,("FI","FIN",246,"FI-19","Varsinais-Suomi","region",NULL)
            ,("FJ","FJI",242,"FJ-01","Ba","province","FJ-W")
            ,("FJ","FJI",242,"FJ-02","Bua","province","FJ-N")
            ,("FJ","FJI",242,"FJ-03","Cakaudrove","province","FJ-N")
            ,("FJ","FJI",242,"FJ-04","Kadavu","province","FJ-E")
            ,("FJ","FJI",242,"FJ-05","Lau","province","FJ-E")
            ,("FJ","FJI",242,"FJ-06","Lomaiviti","province","FJ-E")
            ,("FJ","FJI",242,"FJ-07","Macuata","province","FJ-N")
            ,("FJ","FJI",242,"FJ-08","Nadroga and Navosa","province","FJ-W")
            ,("FJ","FJI",242,"FJ-09","Naitasiri","province","FJ-C")
            ,("FJ","FJI",242,"FJ-10","Namosi","province","FJ-C")
            ,("FJ","FJI",242,"FJ-11","Ra","province","FJ-W")
            ,("FJ","FJI",242,"FJ-12","Rewa","province","FJ-C")
            ,("FJ","FJI",242,"FJ-13","Serua","province","FJ-C")
            ,("FJ","FJI",242,"FJ-14","Tailevu","province","FJ-C")
            ,("FJ","FJI",242,"FJ-C","Central","division",NULL)
            ,("FJ","FJI",242,"FJ-E","Eastern","division",NULL)
            ,("FJ","FJI",242,"FJ-N","Northern","division",NULL)
            ,("FJ","FJI",242,"FJ-R","Rotuma","division",NULL)
            ,("FJ","FJI",242,"FJ-W","Western","division",NULL)
            ,("FK","FLK",238,"FK-??","Falkland Islands","country",NULL)
            ,("FM","FSM",583,"FM-KSA","Kosrae","state",NULL)
            ,("FM","FSM",583,"FM-PNI","Pohnpei","state",NULL)
            ,("FM","FSM",583,"FM-TRK","Chuuk","state",NULL)
            ,("FM","FSM",583,"FM-YAP","Yap","state",NULL)
            ,("FO","FRO",234,"FO-??","Faroe Islands","country",NULL)
            ,("FR","FRA",250,"FR-01","Ain","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-02","Aisne","metropolitan_department","FR-HDF")
            ,("FR","FRA",250,"FR-03","Allier","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-04","Alpes-de-Haute-Provence","metropolitan_department","FR-PAC")
            ,("FR","FRA",250,"FR-05","Hautes-Alpes","metropolitan_department","FR-PAC")
            ,("FR","FRA",250,"FR-06","Alpes-Maritimes","metropolitan_department","FR-PAC")
            ,("FR","FRA",250,"FR-07","Ardèche","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-08","Ardennes","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-09","Ariège","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-10","Aube","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-11","Aude","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-12","Aveyron","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-13","Bouches-du-Rhône","metropolitan_department","FR-PAC")
            ,("FR","FRA",250,"FR-14","Calvados","metropolitan_department","FR-NOR")
            ,("FR","FRA",250,"FR-15","Cantal","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-16","Charente","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-17","Charente-Maritime","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-18","Cher","metropolitan_department","FR-CVL")
            ,("FR","FRA",250,"FR-19","Corrèze","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-20R","Corse","special_status_metropolitan_collectivity",NULL)
            ,("FR","FRA",250,"FR-21","Côte-d'Or","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-22","Côtes-d'Armor","metropolitan_department","FR-BRE")
            ,("FR","FRA",250,"FR-23","Creuse","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-24","Dordogne","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-25","Doubs","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-26","Drôme","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-27","Eure","metropolitan_department","FR-NOR")
            ,("FR","FRA",250,"FR-28","Eure-et-Loir","metropolitan_department","FR-CVL")
            ,("FR","FRA",250,"FR-29","Finistère","metropolitan_department","FR-BRE")
            ,("FR","FRA",250,"FR-2A","Corse-du-Sud","metropolitan_department","FR-20R")
            ,("FR","FRA",250,"FR-2B","Haute-Corse","metropolitan_department","FR-20R")
            ,("FR","FRA",250,"FR-30","Gard","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-31","Haute-Garonne","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-32","Gers","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-33","Gironde","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-34","Hérault","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-35","Ille-et-Vilaine","metropolitan_department","FR-BRE")
            ,("FR","FRA",250,"FR-36","Indre","metropolitan_department","FR-CVL")
            ,("FR","FRA",250,"FR-37","Indre-et-Loire","metropolitan_department","FR-CVL")
            ,("FR","FRA",250,"FR-38","Isère","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-39","Jura","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-40","Landes","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-41","Loir-et-Cher","metropolitan_department","FR-CVL")
            ,("FR","FRA",250,"FR-42","Loire","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-43","Haute-Loire","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-44","Loire-Atlantique","metropolitan_department","FR-PDL")
            ,("FR","FRA",250,"FR-45","Loiret","metropolitan_department","FR-CVL")
            ,("FR","FRA",250,"FR-46","Lot","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-47","Lot-et-Garonne","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-48","Lozère","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-49","Maine-et-Loire","metropolitan_department","FR-PDL")
            ,("FR","FRA",250,"FR-50","Manche","metropolitan_department","FR-NOR")
            ,("FR","FRA",250,"FR-51","Marne","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-52","Haute-Marne","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-53","Mayenne","metropolitan_department","FR-PDL")
            ,("FR","FRA",250,"FR-54","Meurthe-et-Moselle","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-55","Meuse","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-56","Morbihan","metropolitan_department","FR-BRE")
            ,("FR","FRA",250,"FR-57","Moselle","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-58","Nièvre","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-59","Nord","metropolitan_department","FR-HDF")
            ,("FR","FRA",250,"FR-60","Oise","metropolitan_department","FR-HDF")
            ,("FR","FRA",250,"FR-61","Orne","metropolitan_department","FR-NOR")
            ,("FR","FRA",250,"FR-62","Pas-de-Calais","metropolitan_department","FR-HDF")
            ,("FR","FRA",250,"FR-63","Puy-de-Dôme","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-64","Pyrénées-Atlantiques","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-65","Hautes-Pyrénées","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-66","Pyrénées-Orientales","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-67","Bas-Rhin","metropolitan_department","FR-6AE")
            ,("FR","FRA",250,"FR-68","Haut-Rhin","metropolitan_department","FR-6AE")
            ,("FR","FRA",250,"FR-69","Rhône","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-69M",
                "Métropole de Lyon",
                "metropolitan_collectivity_with_special_status","FR-ARA")
            ,("FR","FRA",250,"FR-6AE","Alsace","European_collectivity","FR-GES")
            ,("FR","FRA",250,"FR-70","Haute-Saône","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-71","Saône-et-Loire","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-72","Sarthe","metropolitan_department","FR-PDL")
            ,("FR","FRA",250,"FR-73","Savoie","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-74","Haute-Savoie","metropolitan_department","FR-ARA")
            ,("FR","FRA",250,"FR-75C","Paris","metropolitan_collectivity_with_special_status","FR-IDF")
            ,("FR","FRA",250,"FR-76","Seine-Maritime","metropolitan_department","FR-NOR")
            ,("FR","FRA",250,"FR-77","Seine-et-Marne","metropolitan_department","FR-IDF")
            ,("FR","FRA",250,"FR-78","Yvelines","metropolitan_department","FR-IDF")
            ,("FR","FRA",250,"FR-79","Deux-Sèvres","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-80","Somme","metropolitan_department","FR-HDF")
            ,("FR","FRA",250,"FR-81","Tarn","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-82","Tarn-et-Garonne","metropolitan_department","FR-OCC")
            ,("FR","FRA",250,"FR-83","Var","metropolitan_department","FR-PAC")
            ,("FR","FRA",250,"FR-84","Vaucluse","metropolitan_department","FR-PAC")
            ,("FR","FRA",250,"FR-85","Vendée","metropolitan_department","FR-PDL")
            ,("FR","FRA",250,"FR-86","Vienne","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-87","Haute-Vienne","metropolitan_department","FR-NAQ")
            ,("FR","FRA",250,"FR-88","Vosges","metropolitan_department","FR-GES")
            ,("FR","FRA",250,"FR-89","Yonne","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-90",
                "Territoire de Belfort","metropolitan_department","FR-BFC")
            ,("FR","FRA",250,"FR-91","Essonne","metropolitan_department","FR-IDF")
            ,("FR","FRA",250,"FR-92","Hauts-de-Seine","metropolitan_department","FR-IDF")
            ,("FR","FRA",250,"FR-93","Seine-Saint-Denis","metropolitan_department","FR-IDF")
            ,("FR","FRA",250,"FR-94","Val-de-Marne","metropolitan_department","FR-IDF")
            ,("FR","FRA",250,"FR-95","Val-d'Oise","metropolitan_department","FR-IDF")
            ,("FR","FRA",250,"FR-971","Guadeloupe","overseas_departmental_collectivity",NULL)
            ,("FR","FRA",250,"FR-972","Martinique","overseas_unique_territorial_collectivity",NULL)
            ,("FR","FRA",250,"FR-973",
                "Guyane (française)",
                "overseas_unique_territorial_collectivity",NULL)
            ,("FR","FRA",250,"FR-974",
                "La Réunion","overseas_departmental_collectivity",NULL)
            ,("FR","FRA",250,"FR-976","Mayotte","overseas_departmental_collectivity",NULL)
            ,("FR","FRA",250,"FR-ARA","Auvergne-Rhône-Alpes","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-BFC","Bourgogne-Franche-Comté","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-BL","Saint-Barthélemy","overseas_collectivity",NULL)
            ,("FR","FRA",250,"FR-BRE","Bretagne","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-CP","Clipperton","dependency",NULL)
            ,("FR","FRA",250,"FR-CVL",
                "Centre-Val de Loire","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-GES","Grand-Est","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-HDF","Hauts-de-France","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-IDF","Île-de-France","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-MF","Saint-Martin","overseas_collectivity",NULL)
            ,("FR","FRA",250,"FR-NAQ","Nouvelle-Aquitaine","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-NC","Nouvelle-Calédonie","special_status_overseas_collectivity",NULL)
            ,("FR","FRA",250,"FR-NOR","Normandie","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-OCC","Occitanie","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-PAC","Provence-Alpes-Côte-d'Azur","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-PDL","Pays-de-la-Loire","metropolitan_region",NULL)
            ,("FR","FRA",250,"FR-PF",
                "Polynésie française","overseas_collectivity",NULL)
            ,("FR","FRA",250,"FR-PM",
                "Saint-Pierre-et-Miquelon","overseas_collectivity",NULL)
            ,("FR","FRA",250,"FR-TF",
                "Terres australes françaises","overseas_territory",NULL)
            ,("FR","FRA",250,"FR-WF","Wallis-et-Futuna","overseas_collectivity",NULL)
            ,("GA","GAB",266,"GA-1","Estuaire","province",NULL)
            ,("GA","GAB",266,"GA-2","Haut-Ogooué","province",NULL)
            ,("GA","GAB",266,"GA-3","Moyen-Ogooué","province",NULL)
            ,("GA","GAB",266,"GA-4","Ngounié","province",NULL)
            ,("GA","GAB",266,"GA-5","Nyanga","province",NULL)
            ,("GA","GAB",266,"GA-6","Ogooué-Ivindo","province",NULL)
            ,("GA","GAB",266,"GA-7","Ogooué-Lolo","province",NULL)
            ,("GA","GAB",266,"GA-8","Ogooué-Maritime","province",NULL)
            ,("GA","GAB",266,"GA-9","Woleu-Ntem","province",NULL)
            ,("GB","GBR",826,"GB-ABC",
                "Armagh City, Banbridge and Craigavon","district","GB-NIR")
            ,("GB","GBR",826,"GB-ABD","Aberdeenshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-ABE","Aberdeen City","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-AGB",
                "Argyll and Bute","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-AGY",
                "Isle of Anglesey","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-AND",
                "Ards and North Down","district","GB-NIR")
            ,("GB","GBR",826,"GB-ANN",
                "Antrim and Newtownabbey","district","GB-NIR")
            ,("GB","GBR",826,"GB-ANS","Angus","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-BAS",
                "Bath and North East Somerset","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BBD",
                "Blackburn with Darwen","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BCP",
                "Bournemouth, Christchurch and Poole",
                "unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BDF",
                "Bedford","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BDG",
                "Barking and Dagenham","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-BEN","Brent","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-BEX","Bexley","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-BFS","Belfast City","district","GB-NIR")
            ,("GB","GBR",826,"GB-BGE","Bridgend","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-BGW",
                "Blaenau Gwent","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-BIR","Birmingham","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-BKM","Buckinghamshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BNE","Barnet","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-BNH",
                "Brighton and Hove","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BNS","Barnsley","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-BOL","Bolton","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-BPL","Blackpool","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BRC",
                "Bracknell Forest","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BRD","Bradford","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-BRY","Bromley","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-BST",
                "Bristol, City of","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-BUR","Bury","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-CAM","Cambridgeshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-CAY","Caerphilly","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-CBF",
                "Central Bedfordshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-CCG",
                "Causeway Coast and Glens","district","GB-NIR")
            ,("GB","GBR",826,"GB-CGN","Ceredigion","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-CHE",
                "Cheshire East","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-CHW",
                "Cheshire West and Chester","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-CLD","Calderdale","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-CLK","Clackmannanshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-CMA","Cumbria","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-CMD","Camden","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-CMN","Carmarthenshire","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-CON","Cornwall","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-COV","Coventry","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-CRF","Cardiff","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-CRY","Croydon","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-CWY","Conwy","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-DAL","Darlington","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-DBY","Derbyshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-DEN","Denbighshire","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-DER","Derby","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-DEV","Devon","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-DGY",
                "Dumfries and Galloway","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-DNC","Doncaster","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-DND","Dundee City","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-DOR","Dorset","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-DRS","Derry and Strabane","district","GB-NIR")
            ,("GB","GBR",826,"GB-DUD","Dudley","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-DUR",
                "Durham, County","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-EAL","Ealing","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-EAW","England and Wales","country",NULL)
            ,("GB","GBR",826,"GB-EAY","East Ayrshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-EDH",
                "Edinburgh, City of","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-EDU",
                "East Dunbartonshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-ELN","East Lothian","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-ELS","Eilean Siar","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-ENF","Enfield","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-ENG","England","country",NULL)
            ,("GB","GBR",826,"GB-ERW",
                "East Renfrewshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-ERY",
                "East Riding of Yorkshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-ESS","Essex","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-ESX","East Sussex","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-FAL","Falkirk","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-FIF","Fife","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-FLN","Flintshire","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-FMO",
                "Fermanagh and Omagh","district","GB-NIR")
            ,("GB","GBR",826,"GB-GAT","Gateshead","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-GBN","Great Britain","country",NULL)
            ,("GB","GBR",826,"GB-GLG","Glasgow City","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-GLS","Gloucestershire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-GRE","Greenwich","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-GWN","Gwynedd","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-HAL","Halton","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-HAM","Hampshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-HAV","Havering","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-HCK","Hackney","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-HEF","Herefordshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-HIL","Hillingdon","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-HLD","Highland","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-HMF",
                "Hammersmith and Fulham","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-HNS","Hounslow","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-HPL","Hartlepool","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-HRT","Hertfordshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-HRW","Harrow","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-HRY","Haringey","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-IOS",
                "Isles of Scilly","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-IOW",
                "Isle of Wight","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-ISL","Islington","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-IVC","Inverclyde","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-KEC",
                "Kensington and Chelsea","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-KEN","Kent","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-KHL",
                "Kingston upon Hull","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-KIR","Kirklees","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-KTT",
                "Kingston upon Thames","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-KWL","Knowsley","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-LAN","Lancashire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-LBC",
                "Lisburn and Castlereagh","district","GB-NIR")
            ,("GB","GBR",826,"GB-LBH","Lambeth","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-LCE","Leicester","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-LDS","Leeds","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-LEC","Leicestershire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-LEW","Lewisham","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-LIN","Lincolnshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-LIV","Liverpool","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-LND",
                "London, City of","city_corporation","GB-ENG")
            ,("GB","GBR",826,"GB-LUT","Luton","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-MAN","Manchester","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-MDB","Middlesbrough","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-MDW","Medway","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-MEA",
                "Mid and East Antrim","district","GB-NIR")
            ,("GB","GBR",826,"GB-MIK",
                "Milton Keynes","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-MLN","Midlothian","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-MON","Monmouthshire","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-MRT","Merton","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-MRY","Moray","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-MTY",
                "Merthyr Tydfil","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-MUL","Mid-Ulster","district","GB-NIR")
            ,("GB","GBR",826,"GB-NAY","North Ayrshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-NBL","Northumberland","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-NEL",
                "North East Lincolnshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-NET",
                "Newcastle upon Tyne","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-NFK","Norfolk","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-NGM","Nottingham","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-NIR","Northern Ireland","province",NULL)
            ,("GB","GBR",826,"GB-NLK",
                "North Lanarkshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-NLN",
                "North Lincolnshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-NMD",
                "Newry, Mourne and Down","district","GB-NIR")
            ,("GB","GBR",826,"GB-NNH",
                "North Northamptonshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-NSM",
                "North Somerset","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-NTL",
                "Neath Port Talbot","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-NTT",
                "Nottinghamshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-NTY",
                "North Tyneside","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-NWM","Newham","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-NWP","Newport","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-NYK",
                "North Yorkshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-OLD","Oldham","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-ORK","Orkney Islands","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-OXF","Oxfordshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-PEM","Pembrokeshire","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-PKN",
                "Perth and Kinross","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-PLY","Plymouth","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-POR","Portsmouth","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-POW","Powys","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-PTE","Peterborough","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-RCC",
                "Redcar and Cleveland","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-RCH",
                "Rochdale","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-RCT",
                "Rhondda Cynon Taff","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-RDB","Redbridge","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-RDG","Reading","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-RFW","Renfrewshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-RIC",
                "Richmond upon Thames","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-ROT","Rotherham","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-RUT","Rutland","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-SAW","Sandwell","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SAY","South Ayrshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-SCB",
                "Scottish Borders","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-SCT","Scotland","country",NULL)
            ,("GB","GBR",826,"GB-SFK","Suffolk","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-SFT","Sefton","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SGC",
                "South Gloucestershire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-SHF",
                "Sheffield","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SHN",
                "St. Helens","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SHR","Shropshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-SKP","Stockport","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SLF","Salford","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SLG","Slough","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-SLK",
                "South Lanarkshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-SND","Sunderland","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SOL","Solihull","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SOM","Somerset","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-SOS","Southend-on-Sea","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-SRY","Surrey","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-STE","Stoke-on-Trent","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-STG","Stirling","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-STH","Southampton","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-STN","Sutton","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-STS","Staffordshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-STT","Stockton-on-Tees","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-STY",
                "South Tyneside","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-SWA","Swansea","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-SWD","Swindon","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-SWK","Southwark","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-TAM","Tameside","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-TFW",
                "Telford and Wrekin","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-THR","Thurrock","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-TOB","Torbay","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-TOF","Torfaen","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-TRF","Trafford","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-TWH",
                "Tower Hamlets","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-UKM","United Kingdom","country",NULL)
            ,("GB","GBR",826,"GB-VGL",
                "Vale of Glamorgan, The","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-WAR","Warwickshire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-WBK",
                "West Berkshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-WDU",
                "West Dunbartonshire","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-WFT",
                "Waltham Forest","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-WGN","Wigan","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-WIL","Wiltshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-WKF","Wakefield","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-WLL","Walsall","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-WLN","West Lothian","council_area","GB-SCT")
            ,("GB","GBR",826,"GB-WLS","Wales","country",NULL)
            ,("GB","GBR",826,"GB-WLV","Wolverhampton","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-WND","Wandsworth","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-WNH",
                "West Northamptonshire","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-WNM",
                "Windsor and Maidenhead","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-WOK","Wokingham","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-WOR","Worcestershire","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-WRL","Wirral","metropolitan_district","GB-ENG")
            ,("GB","GBR",826,"GB-WRT","Warrington","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-WRX","Wrexham","unitary_authority","GB-WLS")
            ,("GB","GBR",826,"GB-WSM","Westminster","london_borough","GB-ENG")
            ,("GB","GBR",826,"GB-WSX","West Sussex","two-tier_county","GB-ENG")
            ,("GB","GBR",826,"GB-YOR","York","unitary_authority","GB-ENG")
            ,("GB","GBR",826,"GB-ZET",
                "Shetland Islands","council_area","GB-SCT")
            ,("GD","GRD",308,"GD-01","Saint Andrew","parish",NULL)
            ,("GD","GRD",308,"GD-02","Saint David","parish",NULL)
            ,("GD","GRD",308,"GD-03","Saint George","parish",NULL)
            ,("GD","GRD",308,"GD-04","Saint John","parish",NULL)
            ,("GD","GRD",308,"GD-05","Saint Mark","parish",NULL)
            ,("GD","GRD",308,"GD-06","Saint Patrick","parish",NULL)
            ,("GD","GRD",308,"GD-10",
                "Southern Grenadine Islands","dependency",NULL)
            ,("GE","GEO",239,"GE-AB","Abkhazia","autonomous_republic",NULL)
            ,("GE","GEO",239,"GE-AJ","Ajaria","autonomous_republic",NULL)
            ,("GE","GEO",239,"GE-GU","Guria","region",NULL)
            ,("GE","GEO",239,"GE-IM","Imereti","region",NULL)
            ,("GE","GEO",239,"GE-KA","K'akheti","region",NULL)
            ,("GE","GEO",239,"GE-KK","Kvemo Kartli","region",NULL)
            ,("GE","GEO",239,"GE-MM","Mtskheta-Mtianeti","region",NULL)
            ,("GE","GEO",239,"GE-RL",
                "Rach'a-Lechkhumi-Kvemo Svaneti","region",NULL)
            ,("GE","GEO",239,"GE-SJ","Samtskhe-Javakheti","region",NULL)
            ,("GE","GEO",239,"GE-SK","Shida Kartli","region",NULL)
            ,("GE","GEO",239,"GE-SZ","Samegrelo-Zemo Svaneti","region",NULL)
            ,("GE","GEO",239,"GE-TB","Tbilisi","city",NULL)
            ,("GF","GUF",254,"GF-??","French Guiana","country",NULL)
            ,("GG","GGY",831,"GG-??","Guernsey","country",NULL)
            ,("GH","GHA",288,"GH-AA","Greater Accra","region",NULL)
            ,("GH","GHA",288,"GH-AF","Ahafo","region",NULL)
            ,("GH","GHA",288,"GH-AH","Ashanti","region",NULL)
            ,("GH","GHA",288,"GH-BE","Bono East","region",NULL)
            ,("GH","GHA",288,"GH-BO","Bono","region",NULL)
            ,("GH","GHA",288,"GH-CP","Central","region",NULL)
            ,("GH","GHA",288,"GH-EP","Eastern","region",NULL)
            ,("GH","GHA",288,"GH-NE","North East","region",NULL)
            ,("GH","GHA",288,"GH-NP","Northern","region",NULL)
            ,("GH","GHA",288,"GH-OT","Oti","region",NULL)
            ,("GH","GHA",288,"GH-SV","Savannah","region",NULL)
            ,("GH","GHA",288,"GH-TV","Volta","region",NULL)
            ,("GH","GHA",288,"GH-UE","Upper East","region",NULL)
            ,("GH","GHA",288,"GH-UW","Upper West","region",NULL)
            ,("GH","GHA",288,"GH-WN","Western North","region",NULL)
            ,("GH","GHA",288,"GH-WP","Western","region",NULL)
            ,("GI","GIB",292,"GI-??","Gibraltar","country",NULL)
            ,("GL","GRL",304,"GL-AV","Avannaata Kommunia","municipality",NULL)
            ,("GL","GRL",304,"GL-KU","Kommune Kujalleq","municipality",NULL)
            ,("GL","GRL",304,"GL-QE","Qeqqata Kommunia","municipality",NULL)
            ,("GL","GRL",304,"GL-QT","Kommune Qeqertalik","municipality",NULL)
            ,("GL","GRL",304,"GL-SM",
                "Kommuneqarfik Sermersooq","municipality",NULL)
            ,("GM","GMB",270,"GM-B","Banjul","city",NULL)
            ,("GM","GMB",270,"GM-L","Lower River","division",NULL)
            ,("GM","GMB",270,"GM-M","Central River","division",NULL)
            ,("GM","GMB",270,"GM-N","North Bank","division",NULL)
            ,("GM","GMB",270,"GM-U","Upper River","division",NULL)
            ,("GM","GMB",270,"GM-W","Western","division",NULL)
            ,("GN","GIN",324,"GN-B","Boké","administrative_region",NULL)
            ,("GN","GIN",324,"GN-BE","Beyla","prefecture","GN-N")
            ,("GN","GIN",324,"GN-BF","Boffa","prefecture","GN-B")
            ,("GN","GIN",324,"GN-BK","Boké","prefecture","GN-B")
            ,("GN","GIN",324,"GN-C","Conakry","governorate",NULL)
            ,("GN","GIN",324,"GN-CO","Coyah","prefecture","GN-D")
            ,("GN","GIN",324,"GN-D","Kindia","administrative_region",NULL)
            ,("GN","GIN",324,"GN-DB","Dabola","prefecture","GN-F")
            ,("GN","GIN",324,"GN-DI","Dinguiraye","prefecture","GN-F")
            ,("GN","GIN",324,"GN-DL","Dalaba","prefecture","GN-M")
            ,("GN","GIN",324,"GN-DU","Dubréka","prefecture","GN-D")
            ,("GN","GIN",324,"GN-F","Faranah","administrative_region",NULL)
            ,("GN","GIN",324,"GN-FA","Faranah","prefecture","GN-F")
            ,("GN","GIN",324,"GN-FO","Forécariah","prefecture","GN-D")
            ,("GN","GIN",324,"GN-FR","Fria","prefecture","GN-B")
            ,("GN","GIN",324,"GN-GA","Gaoual","prefecture","GN-B")
            ,("GN","GIN",324,"GN-GU","Guékédou","prefecture","GN-N")
            ,("GN","GIN",324,"GN-K","Kankan","administrative_region",NULL)
            ,("GN","GIN",324,"GN-KA","Kankan","prefecture","GN-K")
            ,("GN","GIN",324,"GN-KB","Koubia","prefecture","GN-L")
            ,("GN","GIN",324,"GN-KD","Kindia","prefecture","GN-D")
            ,("GN","GIN",324,"GN-KE","Kérouané","prefecture","GN-K")
            ,("GN","GIN",324,"GN-KN","Koundara","prefecture","GN-B")
            ,("GN","GIN",324,"GN-KO","Kouroussa","prefecture","GN-K")
            ,("GN","GIN",324,"GN-KS","Kissidougou","prefecture","GN-F")
            ,("GN","GIN",324,"GN-L","Labé","administrative_region",NULL)
            ,("GN","GIN",324,"GN-LA","Labé","prefecture","GN-L")
            ,("GN","GIN",324,"GN-LE","Lélouma","prefecture","GN-L")
            ,("GN","GIN",324,"GN-LO","Lola","prefecture","GN-N")
            ,("GN","GIN",324,"GN-M","Mamou","administrative_region",NULL)
            ,("GN","GIN",324,"GN-MC","Macenta","prefecture","GN-N")
            ,("GN","GIN",324,"GN-MD","Mandiana","prefecture","GN-K")
            ,("GN","GIN",324,"GN-ML","Mali","prefecture","GN-L")
            ,("GN","GIN",324,"GN-MM","Mamou","prefecture","GN-M")
            ,("GN","GIN",324,"GN-N","Nzérékoré","administrative_region",NULL)
            ,("GN","GIN",324,"GN-NZ","Nzérékoré","prefecture","GN-N")
            ,("GN","GIN",324,"GN-PI","Pita","prefecture","GN-M")
            ,("GN","GIN",324,"GN-SI","Siguiri","prefecture","GN-K")
            ,("GN","GIN",324,"GN-TE","Télimélé","prefecture","GN-D")
            ,("GN","GIN",324,"GN-TO","Tougué","prefecture","GN-L")
            ,("GN","GIN",324,"GN-YO","Yomou","prefecture","GN-N")
            ,("GP","GLP",312,"GP-??","Guadeloupe","country",NULL)
            ,("GQ","GNQ",226,"GQ-AN","Annobón","province","GQ-I")
            ,("GQ","GNQ",226,"GQ-BN","Bioko Norte","province","GQ-I")
            ,("GQ","GNQ",226,"GQ-BS","Bioko Sur","province","GQ-I")
            ,("GQ","GNQ",226,"GQ-C","Región Continental","region",NULL)
            ,("GQ","GNQ",226,"GQ-CS","Centro Sur","province","GQ-C")
            ,("GQ","GNQ",226,"GQ-DJ","Djibloho","province","GQ-C")
            ,("GQ","GNQ",226,"GQ-I","Región Insular","region",NULL)
            ,("GQ","GNQ",226,"GQ-KN","Kié-Ntem","province","GQ-C")
            ,("GQ","GNQ",226,"GQ-LI","Litoral","province","GQ-C")
            ,("GQ","GNQ",226,"GQ-WN","Wele-Nzas","province","GQ-C")
            ,("GR","GRC",300,"GR-69","Ágion Óros","self_governed_part",NULL)
            ,("GR","GRC",300,"GR-A",
                "Anatolikí Makedonía kai Thráki","region",NULL)
            ,("GR","GRC",300,"GR-B","Kentrikí Makedonía","region",NULL)
            ,("GR","GRC",300,"GR-C","Dytikí Makedonía","region",NULL)
            ,("GR","GRC",300,"GR-D","Ípeiros","region",NULL)
            ,("GR","GRC",300,"GR-E","Thessalía","region",NULL)
            ,("GR","GRC",300,"GR-F","Ionía Nísia","region",NULL)
            ,("GR","GRC",300,"GR-G","Dytikí Elláda","region",NULL)
            ,("GR","GRC",300,"GR-H","Stereá Elláda","region",NULL)
            ,("GR","GRC",300,"GR-I","Attikí","region",NULL)
            ,("GR","GRC",300,"GR-J","Pelopónnisos","region",NULL)
            ,("GR","GRC",300,"GR-K","Vóreio Aigaío","region",NULL)
            ,("GR","GRC",300,"GR-L","Nótio Aigaío","region",NULL)
            ,("GR","GRC",300,"GR-M","Kríti","region",NULL)
            ,("GS","SGS",239,"GS-??",
                "South Georgia and the South Sandwich Islands","country",NULL)
            ,("GT","GTM",320,"GT-01","Guatemala","department",NULL)
            ,("GT","GTM",320,"GT-02","El Progreso","department",NULL)
            ,("GT","GTM",320,"GT-03","Sacatepéquez","department",NULL)
            ,("GT","GTM",320,"GT-04","Chimaltenango","department",NULL)
            ,("GT","GTM",320,"GT-05","Escuintla","department",NULL)
            ,("GT","GTM",320,"GT-06","Santa Rosa","department",NULL)
            ,("GT","GTM",320,"GT-07","Sololá","department",NULL)
            ,("GT","GTM",320,"GT-08","Totonicapán","department",NULL)
            ,("GT","GTM",320,"GT-09","Quetzaltenango","department",NULL)
            ,("GT","GTM",320,"GT-10","Suchitepéquez","department",NULL)
            ,("GT","GTM",320,"GT-11","Retalhuleu","department",NULL)
            ,("GT","GTM",320,"GT-12","San Marcos","department",NULL)
            ,("GT","GTM",320,"GT-13","Huehuetenango","department",NULL)
            ,("GT","GTM",320,"GT-14","Quiché","department",NULL)
            ,("GT","GTM",320,"GT-15","Baja Verapaz","department",NULL)
            ,("GT","GTM",320,"GT-16","Alta Verapaz","department",NULL)
            ,("GT","GTM",320,"GT-17","Petén","department",NULL)
            ,("GT","GTM",320,"GT-18","Izabal","department",NULL)
            ,("GT","GTM",320,"GT-19","Zacapa","department",NULL)
            ,("GT","GTM",320,"GT-20","Chiquimula","department",NULL)
            ,("GT","GTM",320,"GT-21","Jalapa","department",NULL)
            ,("GT","GTM",320,"GT-22","Jutiapa","department",NULL)
            ,("GU","GUM",316,"GU-??","Guam","country",NULL)
            ,("GW","GNB",624,"GW-BA","Bafatá","region","GW-L")
            ,("GW","GNB",624,"GW-BL","Bolama/Bijagós","region","GW-S")
            ,("GW","GNB",624,"GW-BM","Biombo","region","GW-N")
            ,("GW","GNB",624,"GW-BS","Bissau","autonomous_sector",NULL)
            ,("GW","GNB",624,"GW-CA","Cacheu","region","GW-N")
            ,("GW","GNB",624,"GW-GA","Gabú","region","GW-L")
            ,("GW","GNB",624,"GW-L","Leste","province",NULL)
            ,("GW","GNB",624,"GW-N","Norte","province",NULL)
            ,("GW","GNB",624,"GW-OI","Oio","region","GW-N")
            ,("GW","GNB",624,"GW-QU","Quinara","region","GW-S")
            ,("GW","GNB",624,"GW-S","Sul","province",NULL)
            ,("GW","GNB",624,"GW-TO","Tombali","region","GW-S")
            ,("GY","GUY",328,"GY-BA","Barima-Waini","region",NULL)
            ,("GY","GUY",328,"GY-CU","Cuyuni-Mazaruni","region",NULL)
            ,("GY","GUY",328,"GY-DE","Demerara-Mahaica","region",NULL)
            ,("GY","GUY",328,"GY-EB","East Berbice-Corentyne","region",NULL)
            ,("GY","GUY",328,"GY-ES",
                "Essequibo Islands-West Demerara","region",NULL)
            ,("GY","GUY",328,"GY-MA","Mahaica-Berbice","region",NULL)
            ,("GY","GUY",328,"GY-PM","Pomeroon-Supenaam","region",NULL)
            ,("GY","GUY",328,"GY-PT","Potaro-Siparuni","region",NULL)
            ,("GY","GUY",328,"GY-UD","Upper Demerara-Berbice","region",NULL)
            ,("GY","GUY",328,"GY-UT",
                "Upper Takutu-Upper Essequibo","region",NULL)
            ,("HK","HKG",344,"HK-??",
                "Hong Kong","special_administrative_region",NULL)
            ,("HM","HMD",334,"HM-??",
                "Heard Island and McDonald Islands","country",NULL)
            ,("HN","HND",340,"HN-AT","Atlántida","department",NULL)
            ,("HN","HND",340,"HN-CH","Choluteca","department",NULL)
            ,("HN","HND",340,"HN-CL","Colón","department",NULL)
            ,("HN","HND",340,"HN-CM","Comayagua","department",NULL)
            ,("HN","HND",340,"HN-CP","Copán","department",NULL)
            ,("HN","HND",340,"HN-CR","Cortés","department",NULL)
            ,("HN","HND",340,"HN-EP","El Paraíso","department",NULL)
            ,("HN","HND",340,"HN-FM","Francisco Morazán","department",NULL)
            ,("HN","HND",340,"HN-GD","Gracias a Dios","department",NULL)
            ,("HN","HND",340,"HN-IB","Islas de la Bahía","department",NULL)
            ,("HN","HND",340,"HN-IN","Intibucá","department",NULL)
            ,("HN","HND",340,"HN-LE","Lempira","department",NULL)
            ,("HN","HND",340,"HN-LP","La Paz","department",NULL)
            ,("HN","HND",340,"HN-OC","Ocotepeque","department",NULL)
            ,("HN","HND",340,"HN-OL","Olancho","department",NULL)
            ,("HN","HND",340,"HN-SB","Santa Bárbara","department",NULL)
            ,("HN","HND",340,"HN-VA","Valle","department",NULL)
            ,("HN","HND",340,"HN-YO","Yoro","department",NULL)
            ,("HR","HRV",191,"HR-01","Zagrebačka županija","county",NULL)
            ,("HR","HRV",191,"HR-02",
                "Krapinsko-zagorska županija","county",NULL)
            ,("HR","HRV",191,"HR-03",
                "Sisačko-moslavačka županija","county",NULL)
            ,("HR","HRV",191,"HR-04","Karlovačka županija","county",NULL)
            ,("HR","HRV",191,"HR-05","Varaždinska županija","county",NULL)
            ,("HR","HRV",191,"HR-06",
                "Koprivničko-križevačka županija","county",NULL)
            ,("HR","HRV",191,"HR-07",
                "Bjelovarsko-bilogorska županija","county",NULL)
            ,("HR","HRV",191,"HR-08",
                "Primorsko-goranska županija","county",NULL)
            ,("HR","HRV",191,"HR-09",
                "Ličko-senjska županija","county",NULL)
            ,("HR","HRV",191,"HR-10",
                "Virovitičko-podravska županija","county",NULL)
            ,("HR","HRV",191,"HR-11",
                "Požeško-slavonska županija","county",NULL)
            ,("HR","HRV",191,"HR-12","Brodsko-posavska županija","county",NULL)
            ,("HR","HRV",191,"HR-13","Zadarska županija","county",NULL)
            ,("HR","HRV",191,"HR-14",
                "Osječko-baranjska županija","county",NULL)
            ,("HR","HRV",191,"HR-15",
                "Šibensko-kninska županija","county",NULL)
            ,("HR","HRV",191,"HR-16",
                "Vukovarsko-srijemska županija","county",NULL)
            ,("HR","HRV",191,"HR-17",
                "Splitsko-dalmatinska županija","county",NULL)
            ,("HR","HRV",191,"HR-18",
                "Istarska županija","county",NULL)
            ,("HR","HRV",191,"HR-19",
                "Dubrovačko-neretvanska županija","county",NULL)
            ,("HR","HRV",191,"HR-20","Međimurska županija","county",NULL)
            ,("HR","HRV",191,"HR-21","Grad Zagreb","city",NULL)
            ,("HT","HTI",332,"HT-AR","Artibonite","department",NULL)
            ,("HT","HTI",332,"HT-CE","Centre","department",NULL)
            ,("HT","HTI",332,"HT-GA","Grande'Anse","department",NULL)
            ,("HT","HTI",332,"HT-ND","Nord","department",NULL)
            ,("HT","HTI",332,"HT-NE","Nord-Est","department",NULL)
            ,("HT","HTI",332,"HT-NI","Nippes","department",NULL)
            ,("HT","HTI",332,"HT-NO","Nord-Ouest","department",NULL)
            ,("HT","HTI",332,"HT-OU","Ouest","department",NULL)
            ,("HT","HTI",332,"HT-SD","Sud","department",NULL)
            ,("HT","HTI",332,"HT-SE","Sud-Est","department",NULL)
            ,("HU","HUN",348,"HU-BA","Baranya","county",NULL)
            ,("HU","HUN",348,"HU-BC","Békéscsaba","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-BE","Békés","county",NULL)
            ,("HU","HUN",348,"HU-BK","Bács-Kiskun","county",NULL)
            ,("HU","HUN",348,"HU-BU","Budapest","capital_city",NULL)
            ,("HU","HUN",348,"HU-BZ","Borsod-Abaúj-Zemplén","county",NULL)
            ,("HU","HUN",348,"HU-CS","Csongrád-Csanád","county",NULL)
            ,("HU","HUN",348,"HU-DE","Debrecen","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-DU","Dunaújváros","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-EG","Eger","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-ER","Érd","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-FE","Fejér","county",NULL)
            ,("HU","HUN",348,"HU-GS","Győr-Moson-Sopron","county",NULL)
            ,("HU","HUN",348,"HU-GY","Győr","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-HB","Hajdú-Bihar","county",NULL)
            ,("HU","HUN",348,"HU-HE","Heves","county",NULL)
            ,("HU","HUN",348,"HU-HV","Hódmezővásárhely","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-JN","Jász-Nagykun-Szolnok","county",NULL)
            ,("HU","HUN",348,"HU-KE","Komárom-Esztergom","county",NULL)
            ,("HU","HUN",348,"HU-KM","Kecskemét","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-KV","Kaposvár","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-MI","Miskolc","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-NK","Nagykanizsa","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-NO","Nógrád","county",NULL)
            ,("HU","HUN",348,"HU-NY","Nyíregyháza","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-PE","Pest","county",NULL)
            ,("HU","HUN",348,"HU-PS","Pécs","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-SD","Szeged","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-SF","Székesfehérvár","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-SH","Szombathely","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-SK","Szolnok","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-SN","Sopron","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-SO","Somogy","county",NULL)
            ,("HU","HUN",348,"HU-SS","Szekszárd","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-ST","Salgótarján","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-SZ","Szabolcs-Szatmár-Bereg","county",NULL)
            ,("HU","HUN",348,"HU-TB","Tatabánya","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-TO","Tolna","county",NULL)
            ,("HU","HUN",348,"HU-VA","Vas","county",NULL)
            ,("HU","HUN",348,"HU-VE","Veszprém","county",NULL)
            ,("HU","HUN",348,"HU-VM","Veszprém","city_with_county_rights",NULL)
            ,("HU","HUN",348,"HU-ZA","Zala","county",NULL)
            ,("HU","HUN",348,"HU-ZE","Zalaegerszeg","city_with_county_rights",NULL)
            ,("ID","IDN",360,"ID-AC","Aceh","province","ID-SM")
            ,("ID","IDN",360,"ID-BA","Bali","province","ID-NU")
            ,("ID","IDN",360,"ID-BB",
                "Bangka Belitung Islands Kepulauan Bangka Belitung",
                "province","ID-SM")
            ,("ID","IDN",360,"ID-BE","Bengkulu","province","ID-SM")
            ,("ID","IDN",360,"ID-BT","Banten","province","ID-JW")
            ,("ID","IDN",360,"ID-GO","Gorontalo","province","ID-SL")
            ,("ID","IDN",360,"ID-JA","Jambi","province","ID-SM")
            ,("ID","IDN",360,"ID-JB","West Java Jawa Barat","province","ID-JW")
            ,("ID","IDN",360,"ID-JI","East Java Jawa Timur","province","ID-JW")
            ,("ID","IDN",360,"ID-JK",
                "Jakarta Jakarta Raya","capital_region","ID-JW")
            ,("ID","IDN",360,"ID-JT",
                "Central Java Jawa Tengah","province","ID-JW")
            ,("ID","IDN",360,"ID-JW","Jawa","geographical_unit",NULL)
            ,("ID","IDN",360,"ID-KA","Kalimantan","geographical_unit",NULL)
            ,("ID","IDN",360,"ID-KB",
                "West Kalimantan Kalimantan Barat","province","ID-KA")
            ,("ID","IDN",360,"ID-KI",
                "East Kalimantan Kalimantan Timur","province","ID-KA")
            ,("ID","IDN",360,"ID-KR",
                "Riau Islands Kepulauan Riau","province","ID-SM")
            ,("ID","IDN",360,"ID-KS",
                "South Kalimantan Kalimantan Selatan","province","ID-KA")
            ,("ID","IDN",360,"ID-KT",
                "Central Kalimantan Kalimantan Tengah","province","ID-KA")
            ,("ID","IDN",360,"ID-KU",
                "North Kalimantan Kalimantan Utara","province","ID-KA")
            ,("ID","IDN",360,"ID-LA","Lampung","province","ID-SM")
            ,("ID","IDN",360,"ID-MA","Maluku","province","ID-ML")
            ,("ID","IDN",360,"ID-ML","Maluku","geographical_unit",NULL)
            ,("ID","IDN",360,"ID-MU",
                "North Maluku Maluku Utara","province","ID-ML")
            ,("ID","IDN",360,"ID-NB",
                "West Nusa Tenggara Nusa Tenggara Barat","province","ID-NU")
            ,("ID","IDN",360,"ID-NT",
                "East Nusa Tenggara Nusa Tenggara Timur","province","ID-NU")
            ,("ID","IDN",360,"ID-NU","Nusa Tenggara","geographical_unit",NULL)
            ,("ID","IDN",360,"ID-PA","Papua","province","ID-PP")
            ,("ID","IDN",360,"ID-PB","West Papua","province","ID-PP")
            ,("ID","IDN",360,"ID-PE",
                "Highland Papua Papua Pengunungan","province","ID-PP")
            ,("ID","IDN",360,"ID-PP",
                "Papua","geographical_unit",NULL)
            ,("ID","IDN",360,"ID-PS",
                "South Papua Papua Selatan","province","ID-PP")
            ,("ID","IDN",360,"ID-PT",
                "Central Papua Papua Tengah","province","ID-PP")
            ,("ID","IDN",360,"ID-RI",
                "Riau","province","ID-SM")
            ,("ID","IDN",360,"ID-SA",
                "North Sulawesi Sulawesi Utara","province","ID-SL")
            ,("ID","IDN",360,"ID-SB",
                "West Sumatra Sumatera Barat","province","ID-SM")
            ,("ID","IDN",360,"ID-SG",
                "Southeast Sulawesi Sulawesi Tenggara","province","ID-SL")
            ,("ID","IDN",360,"ID-SL","Sulawesi","geographical_unit",NULL)
            ,("ID","IDN",360,"ID-SM","Sumatera","geographical_unit",NULL)
            ,("ID","IDN",360,"ID-SN",
                "South Sulawesi Sulawesi Selatan","province","ID-SL")
            ,("ID","IDN",360,"ID-SR",
                "West Sulawesi Sulawesi Barat","province","ID-SL")
            ,("ID","IDN",360,"ID-SS",
                "South Sumatra Sumatera Selatan","province","ID-SM")
            ,("ID","IDN",360,"ID-ST",
                "Central Sulawesi Sulawesi Tengah","province","ID-SL")
            ,("ID","IDN",360,"ID-SU",
                "North Sumatra Sumatera Utara","province","ID-SM")
            ,("ID","IDN",360,"ID-YO","Yogyakarta","special_region","ID-JW")
            ,("IE","IRL",372,"IE-C","Connaught","province",NULL)
            ,("IE","IRL",372,"IE-CE","Clare","county","IE-M")
            ,("IE","IRL",372,"IE-CN","Cavan","county","IE-U")
            ,("IE","IRL",372,"IE-CO","Cork","county","IE-M")
            ,("IE","IRL",372,"IE-CW","Carlow","county","IE-L")
            ,("IE","IRL",372,"IE-D","Dublin","county","IE-L")
            ,("IE","IRL",372,"IE-DL","Donegal","county","IE-U")
            ,("IE","IRL",372,"IE-G","Galway","county","IE-C")
            ,("IE","IRL",372,"IE-KE","Kildare","county","IE-L")
            ,("IE","IRL",372,"IE-KK","Kilkenny","county","IE-L")
            ,("IE","IRL",372,"IE-KY","Kerry","county","IE-M")
            ,("IE","IRL",372,"IE-L","Leinster","province",NULL)
            ,("IE","IRL",372,"IE-LD","Longford","county","IE-L")
            ,("IE","IRL",372,"IE-LH","Louth","county","IE-L")
            ,("IE","IRL",372,"IE-LK","Limerick","county","IE-M")
            ,("IE","IRL",372,"IE-LM","Leitrim","county","IE-C")
            ,("IE","IRL",372,"IE-LS","Laois","county","IE-L")
            ,("IE","IRL",372,"IE-M","Munster","province",NULL)
            ,("IE","IRL",372,"IE-MH","Meath","county","IE-L")
            ,("IE","IRL",372,"IE-MN","Monaghan","county","IE-U")
            ,("IE","IRL",372,"IE-MO","Mayo","county","IE-C")
            ,("IE","IRL",372,"IE-OY","Offaly","county","IE-L")
            ,("IE","IRL",372,"IE-RN","Roscommon","county","IE-C")
            ,("IE","IRL",372,"IE-SO","Sligo","county","IE-C")
            ,("IE","IRL",372,"IE-TA","Tipperary","county","IE-M")
            ,("IE","IRL",372,"IE-U","Ulster","province",NULL)
            ,("IE","IRL",372,"IE-WD","Waterford","county","IE-M")
            ,("IE","IRL",372,"IE-WH","Westmeath","county","IE-L")
            ,("IE","IRL",372,"IE-WW","Wicklow","county","IE-L")
            ,("IE","IRL",372,"IE-WX","Wexford","county","IE-L")
            ,("IL","ISR",376,"IL-D","HaDarom","district",NULL)
            ,("IL","ISR",376,"IL-HA","H̱efa","district",NULL)
            ,("IL","ISR",376,"IL-JM","Yerushalayim","district",NULL)
            ,("IL","ISR",376,"IL-M","HaMerkaz","district",NULL)
            ,("IL","ISR",376,"IL-TA","Tel Aviv","district",NULL)
            ,("IL","ISR",376,"IL-Z","HaTsafon","district",NULL)
            ,("IM","IMN",833,"IM-??","Isle of Man","country",NULL)
            ,("IN","IND",356,"IN-AN",
                "Andaman and Nicobar Islands","union_territory",NULL)
            ,("IN","IND",356,"IN-AP","Andhra Pradesh","state",NULL)
            ,("IN","IND",356,"IN-AR","Arunāchal Pradesh","state",NULL)
            ,("IN","IND",356,"IN-AS","Assam","state",NULL)
            ,("IN","IND",356,"IN-BR","Bihār","state",NULL)
            ,("IN","IND",356,"IN-CH","Chandīgarh","union_territory",NULL)
            ,("IN","IND",356,"IN-CT","Chhattīsgarh","state",NULL)
            ,("IN","IND",356,"IN-DH",
                "Dādra and Nagar Haveli and Damān and Diu",
                "union_territory",NULL)
            ,("IN","IND",356,"IN-DL","Delhi","union_territory",NULL)
            ,("IN","IND",356,"IN-GA","Goa","state",NULL)
            ,("IN","IND",356,"IN-GJ","Gujarāt","state",NULL)
            ,("IN","IND",356,"IN-HP","Himāchal Pradesh","state",NULL)
            ,("IN","IND",356,"IN-HR","Haryāna","state",NULL)
            ,("IN","IND",356,"IN-JH","Jhārkhand","state",NULL)
            ,("IN","IND",356,"IN-JK",
                "Jammu and Kashmīr","union_territory",NULL)
            ,("IN","IND",356,"IN-KA","Karnātaka","state",NULL)
            ,("IN","IND",356,"IN-KL","Kerala","state",NULL)
            ,("IN","IND",356,"IN-LA","Ladākh","union_territory",NULL)
            ,("IN","IND",356,"IN-LD","Lakshadweep","union_territory",NULL)
            ,("IN","IND",356,"IN-MH","Mahārāshtra","state",NULL)
            ,("IN","IND",356,"IN-ML","Meghālaya","state",NULL)
            ,("IN","IND",356,"IN-MN","Manipur","state",NULL)
            ,("IN","IND",356,"IN-MP","Madhya Pradesh","state",NULL)
            ,("IN","IND",356,"IN-MZ","Mizoram","state",NULL)
            ,("IN","IND",356,"IN-NL","Nāgāland","state",NULL)
            ,("IN","IND",356,"IN-OR","Odisha","state",NULL)
            ,("IN","IND",356,"IN-PB","Punjab","state",NULL)
            ,("IN","IND",356,"IN-PY","Puducherry","union_territory",NULL)
            ,("IN","IND",356,"IN-RJ","Rājasthān","state",NULL)
            ,("IN","IND",356,"IN-SK","Sikkim","state",NULL)
            ,("IN","IND",356,"IN-TG","Telangāna","state",NULL)
            ,("IN","IND",356,"IN-TN","Tamil Nādu","state",NULL)
            ,("IN","IND",356,"IN-TR","Tripura","state",NULL)
            ,("IN","IND",356,"IN-UP","Uttar Pradesh","state",NULL)
            ,("IN","IND",356,"IN-UT","Uttarākhand","state",NULL)
            ,("IN","IND",356,"IN-WB","West Bengal","state",NULL)
            ,("IO","IOT",86,"IO-??",
                "British Indian Ocean Territory","country",NULL)
            ,("IQ","IRQ",368,"IQ-AN","Al Anbār","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-AR","Arbīl","governorate","IQ-KR")
            ,("IQ","IRQ",368,"IQ-BA","Al Başrah","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-BB","Bābil","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-BG","Baghdād","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-DA","Dahūk","governorate","IQ-KR")
            ,("IQ","IRQ",368,"IQ-DI","Diyālá","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-DQ","Dhī Qār","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-KA","Karbalā'","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-KI","Kirkūk","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-KR","Iqlīm Kūrdistān","region",NULL)
            ,("IQ","IRQ",368,"IQ-MA","Maysān","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-MU","Al Muthanná","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-NA","An Najaf","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-NI","Nīnawá","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-QA","Al Qādisīyah","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-SD","Şalāḩ ad Dīn","governorate",NULL)
            ,("IQ","IRQ",368,"IQ-SU","As Sulaymānīyah","governorate","IQ-KR")
            ,("IQ","IRQ",368,"IQ-WA","Wāsiţ","governorate",NULL)
            ,("IR","IRN",364,"IR-00","Markazī","province",NULL)
            ,("IR","IRN",364,"IR-01","Gīlān","province",NULL)
            ,("IR","IRN",364,"IR-02","Māzandarān","province",NULL)
            ,("IR","IRN",364,"IR-03","Āz̄ārbāyjān-e Shārqī","province",NULL)
            ,("IR","IRN",364,"IR-04","Āz̄ārbāyjān-e Ghārbī","province",NULL)
            ,("IR","IRN",364,"IR-05","Kermānshāh","province",NULL)
            ,("IR","IRN",364,"IR-06","Khūzestān","province",NULL)
            ,("IR","IRN",364,"IR-07","Fārs","province",NULL)
            ,("IR","IRN",364,"IR-08","Kermān","province",NULL)
            ,("IR","IRN",364,"IR-09","Khorāsān-e Raẕavī","province",NULL)
            ,("IR","IRN",364,"IR-10","Eşfahān","province",NULL)
            ,("IR","IRN",364,"IR-11","Sīstān va Balūchestān","province",NULL)
            ,("IR","IRN",364,"IR-12","Kordestān","province",NULL)
            ,("IR","IRN",364,"IR-13","Hamadān","province",NULL)
            ,("IR","IRN",364,"IR-14",
                "Chahār Maḩāl va Bakhtīārī","province",NULL)
            ,("IR","IRN",364,"IR-15","Lorestān","province",NULL)
            ,("IR","IRN",364,"IR-16","Īlām","province",NULL)
            ,("IR","IRN",364,"IR-17",
                "Kohgīlūyeh va Bowyer Aḩmad","province",NULL)
            ,("IR","IRN",364,"IR-18","Būshehr","province",NULL)
            ,("IR","IRN",364,"IR-19","Zanjān","province",NULL)
            ,("IR","IRN",364,"IR-20","Semnān","province",NULL)
            ,("IR","IRN",364,"IR-21","Yazd","province",NULL)
            ,("IR","IRN",364,"IR-22","Hormozgān","province",NULL)
            ,("IR","IRN",364,"IR-23","Tehrān","province",NULL)
            ,("IR","IRN",364,"IR-24","Ardabīl","province",NULL)
            ,("IR","IRN",364,"IR-25","Qom","province",NULL)
            ,("IR","IRN",364,"IR-26","Qazvīn","province",NULL)
            ,("IR","IRN",364,"IR-27","Golestān","province",NULL)
            ,("IR","IRN",364,"IR-28","Khorāsān-e Shomālī","province",NULL)
            ,("IR","IRN",364,"IR-29","Khorāsān-e Jonūbī","province",NULL)
            ,("IR","IRN",364,"IR-30","Alborz","province",NULL)
            ,("IS","ISL",352,"IS-1","Höfuðborgarsvæði","region",NULL)
            ,("IS","ISL",352,"IS-2","Suðurnes","region",NULL)
            ,("IS","ISL",352,"IS-3","Vesturland","region",NULL)
            ,("IS","ISL",352,"IS-4","Vestfirðir","region",NULL)
            ,("IS","ISL",352,"IS-5","Norðurland vestra","region",NULL)
            ,("IS","ISL",352,"IS-6","Norðurland eystra","region",NULL)
            ,("IS","ISL",352,"IS-7","Austurland","region",NULL)
            ,("IS","ISL",352,"IS-8","Suðurland","region",NULL)
            ,("IS","ISL",352,"IS-AKN","Akraneskaupstaður","municipality","IS-3")
            ,("IS","ISL",352,"IS-AKU","Akureyrarbær","municipality","IS-6")
            ,("IS","ISL",352,"IS-ARN","Árneshreppur","municipality","IS-4")
            ,("IS","ISL",352,"IS-ASA","Ásahreppur","municipality","IS-8")
            ,("IS","ISL",352,"IS-BLA","Bláskógabyggð","municipality","IS-8")
            ,("IS","ISL",352,"IS-BOG","Borgarbyggð","municipality","IS-3")
            ,("IS","ISL",352,"IS-BOL","Bolungarvíkurkaupstaður","municipality","IS-4")
            ,("IS","ISL",352,"IS-DAB","Dalabyggð","municipality","IS-3")
            ,("IS","ISL",352,"IS-DAV","Dalvíkurbyggð","municipality","IS-6")
            ,("IS","ISL",352,"IS-EOM",
                "Eyja- og Miklaholtshreppur","municipality","IS-3")
            ,("IS","ISL",352,"IS-EYF","Eyjafjarðarsveit","municipality","IS-6")
            ,("IS","ISL",352,"IS-FJD","Fjarðabyggð","municipality","IS-7")
            ,("IS","ISL",352,"IS-FJL","Fjallabyggð","municipality","IS-6")
            ,("IS","ISL",352,"IS-FLA","Flóahreppur","municipality","IS-8")
            ,("IS","ISL",352,"IS-FLR","Fljótsdalshreppur","municipality","IS-7")
            ,("IS","ISL",352,"IS-GAR","Garðabær","municipality","IS-1")
            ,("IS","ISL",352,"IS-GOG",
                "Grímsnes- og Grafningshreppur","municipality","IS-8")
            ,("IS","ISL",352,"IS-GRN","Grindavíkurbær","municipality","IS-2")
            ,("IS","ISL",352,"IS-GRU","Grundarfjarðarbær","municipality","IS-3")
            ,("IS","ISL",352,"IS-GRY","Grýtubakkahreppur","municipality","IS-6")
            ,("IS","ISL",352,"IS-HAF","Hafnarfjarðarkaupstaður","municipality","IS-1")
            ,("IS","ISL",352,"IS-HRG","Hörgársveit","municipality","IS-6")
            ,("IS","ISL",352,"IS-HRU","Hrunamannahreppur","municipality","IS-8")
            ,("IS","ISL",352,"IS-HUG","Húnabyggð","municipality","IS-5")
            ,("IS","ISL",352,"IS-HUV","Húnaþing vestra","municipality","IS-5")
            ,("IS","ISL",352,"IS-HVA","Hvalfjarðarsveit","municipality","IS-3")
            ,("IS","ISL",352,"IS-HVE","Hveragerðisbær","municipality","IS-8")
            ,("IS","ISL",352,"IS-ISA","Ísafjarðarbær","municipality","IS-4")
            ,("IS","ISL",352,"IS-KAL","Kaldrananeshreppur","municipality","IS-4")
            ,("IS","ISL",352,"IS-KJO","Kjósarhreppur","municipality","IS-1")
            ,("IS","ISL",352,"IS-KOP","Kópavogsbær","municipality","IS-1")
            ,("IS","ISL",352,"IS-LAN","Langanesbyggð","municipality","IS-6")
            ,("IS","ISL",352,"IS-MOS","Mosfellsbær","municipality","IS-1")
            ,("IS","ISL",352,"IS-MUL","Múlaþing","municipality","IS-7")
            ,("IS","ISL",352,"IS-MYR","Mýrdalshreppur","municipality","IS-8")
            ,("IS","ISL",352,"IS-NOR","Norðurþing","municipality","IS-6")
            ,("IS","ISL",352,"IS-RGE",
                "Rangárþing eystra","municipality","IS-8")
            ,("IS","ISL",352,"IS-RGY","Rangárþing ytra","municipality","IS-8")
            ,("IS","ISL",352,"IS-RHH","Reykhólahreppur","municipality","IS-4")
            ,("IS","ISL",352,"IS-RKN","Reykjanesbær","municipality","IS-2")
            ,("IS","ISL",352,"IS-RKV","Reykjavíkurborg","municipality","IS-1")
            ,("IS","ISL",352,"IS-SBT","Svalbarðsstrandarhreppur","municipality","IS-6")
            ,("IS","ISL",352,"IS-SDN","Suðurnesjabær","municipality","IS-2")
            ,("IS","ISL",352,"IS-SDV","Súðavíkurhreppur","municipality","IS-4")
            ,("IS","ISL",352,"IS-SEL","Seltjarnarnesbær","municipality","IS-1")
            ,("IS","ISL",352,"IS-SFA",
                "Sveitarfélagið Árborg","municipality","IS-8")
            ,("IS","ISL",352,"IS-SHF",
                "Sveitarfélagið Hornafjörður","municipality","IS-7")
            ,("IS","ISL",352,"IS-SKF","Skaftárhreppur","municipality","IS-8")
            ,("IS","ISL",352,"IS-SKG","Skagabyggð","municipality","IS-5")
            ,("IS","ISL",352,"IS-SKO","Skorradalshreppur","municipality","IS-3")
            ,("IS","ISL",352,"IS-SKR","Skagafjörður","municipality","IS-5")
            ,("IS","ISL",352,"IS-SNF","Snæfellsbær","municipality","IS-3")
            ,("IS","ISL",352,"IS-SOG",
                "Skeiða- og Gnúpverjahreppur","municipality","IS-8")
            ,("IS","ISL",352,"IS-SOL",
                "Sveitarfélagið Ölfus","municipality","IS-8")
            ,("IS","ISL",352,"IS-SSS",
                "Sveitarfélagið Skagaströnd","municipality","IS-5")
            ,("IS","ISL",352,"IS-STR",
                "Strandabyggð","municipality","IS-4")
            ,("IS","ISL",352,"IS-STY",
                "Stykkishólmsbær","municipality","IS-3")
            ,("IS","ISL",352,"IS-SVG",
                "Sveitarfélagið Vogar","municipality","IS-2")
            ,("IS","ISL",352,"IS-TAL","Tálknafjarðarhreppur","municipality","IS-4")
            ,("IS","ISL",352,"IS-THG","Þingeyjarsveit","municipality","IS-6")
            ,("IS","ISL",352,"IS-TJO","Tjörneshreppur","municipality","IS-6")
            ,("IS","ISL",352,"IS-VEM","Vestmannaeyjabær","municipality","IS-8")
            ,("IS","ISL",352,"IS-VER","Vesturbyggð","municipality","IS-4")
            ,("IS","ISL",352,"IS-VOP","Vopnafjarðarhreppur","municipality","IS-7")
            ,("IT","ITA",380,"IT-21","Piemonte","region",NULL)
            ,("IT","ITA",380,"IT-23","Aosta Valley","autonomous_region",NULL)
            ,("IT","ITA",380,"IT-25","Lombardia","region",NULL)
            ,("IT","ITA",380,"IT-32",
                "Trentino-South Tyrol","autonomous_region",NULL)
            ,("IT","ITA",380,"IT-34",
                "Veneto","region",NULL)
            ,("IT","ITA",380,"IT-36",
                "Friuli Venezia Giulia","autonomous_region",NULL)
            ,("IT","ITA",380,"IT-42","Liguria","region",NULL)
            ,("IT","ITA",380,"IT-45","Emilia-Romagna","region",NULL)
            ,("IT","ITA",380,"IT-52","Toscana","region",NULL)
            ,("IT","ITA",380,"IT-55","Umbria","region",NULL)
            ,("IT","ITA",380,"IT-57","Marche","region",NULL)
            ,("IT","ITA",380,"IT-62","Lazio","region",NULL)
            ,("IT","ITA",380,"IT-65","Abruzzo","region",NULL)
            ,("IT","ITA",380,"IT-67","Molise","region",NULL)
            ,("IT","ITA",380,"IT-72","Campania","region",NULL)
            ,("IT","ITA",380,"IT-75","Puglia","region",NULL)
            ,("IT","ITA",380,"IT-77","Basilicata","region",NULL)
            ,("IT","ITA",380,"IT-78","Calabria","region",NULL)
            ,("IT","ITA",380,"IT-82","Sicily","autonomous_region",NULL)
            ,("IT","ITA",380,"IT-88","Sardinia","autonomous_region",NULL)
            ,("IT","ITA",380,"IT-AG","Agrigento","free_municipal_consortia","IT-82")
            ,("IT","ITA",380,"IT-AL","Alessandria","province","IT-21")
            ,("IT","ITA",380,"IT-AN","Ancona","province","IT-57")
            ,("IT","ITA",380,"IT-AP","Ascoli Piceno","province","IT-57")
            ,("IT","ITA",380,"IT-AQ","L'Aquila","province","IT-65")
            ,("IT","ITA",380,"IT-AR","Arezzo","province","IT-52")
            ,("IT","ITA",380,"IT-AT","Asti","province","IT-21")
            ,("IT","ITA",380,"IT-AV","Avellino","province","IT-72")
            ,("IT","ITA",380,"IT-BA","Bari","metropolitan_city","IT-75")
            ,("IT","ITA",380,"IT-BG","Bergamo","province","IT-25")
            ,("IT","ITA",380,"IT-BI","Biella","province","IT-21")
            ,("IT","ITA",380,"IT-BL","Belluno","province","IT-34")
            ,("IT","ITA",380,"IT-BN","Benevento","province","IT-72")
            ,("IT","ITA",380,"IT-BO","Bologna","metropolitan_city","IT-45")
            ,("IT","ITA",380,"IT-BR","Brindisi","province","IT-75")
            ,("IT","ITA",380,"IT-BS","Brescia","province","IT-25")
            ,("IT","ITA",380,"IT-BT","Barletta-Andria-Trani","province","IT-75")
            ,("IT","ITA",380,"IT-BZ","Bolzano","autonomous_province","IT-32")
            ,("IT","ITA",380,"IT-CA","Cagliari","metropolitan_city","IT-88")
            ,("IT","ITA",380,"IT-CB","Campobasso","province","IT-67")
            ,("IT","ITA",380,"IT-CE","Caserta","province","IT-72")
            ,("IT","ITA",380,"IT-CH","Chieti","province","IT-65")
            ,("IT","ITA",380,"IT-CL","Caltanissetta","free_municipal_consortia","IT-82")
            ,("IT","ITA",380,"IT-CN","Cuneo","province","IT-21")
            ,("IT","ITA",380,"IT-CO","Como","province","IT-25")
            ,("IT","ITA",380,"IT-CR","Cremona","province","IT-25")
            ,("IT","ITA",380,"IT-CS","Cosenza","province","IT-78")
            ,("IT","ITA",380,"IT-CT","Catania","metropolitan_city","IT-82")
            ,("IT","ITA",380,"IT-CZ","Catanzaro","province","IT-78")
            ,("IT","ITA",380,"IT-EN","Enna","free_municipal_consortia","IT-82")
            ,("IT","ITA",380,"IT-FC","Forlì-Cesena","province","IT-45")
            ,("IT","ITA",380,"IT-FE","Ferrara","province","IT-45")
            ,("IT","ITA",380,"IT-FG","Foggia","province","IT-75")
            ,("IT","ITA",380,"IT-FI","Firenze","metropolitan_city","IT-52")
            ,("IT","ITA",380,"IT-FM","Fermo","province","IT-57")
            ,("IT","ITA",380,"IT-FR","Frosinone","province","IT-62")
            ,("IT","ITA",380,"IT-GE","Genova","metropolitan_city","IT-42")
            ,("IT","ITA",380,"IT-GO","Gorizia","decentralized_regional_entity","IT-36")
            ,("IT","ITA",380,"IT-GR","Grosseto","province","IT-52")
            ,("IT","ITA",380,"IT-IM","Imperia","province","IT-42")
            ,("IT","ITA",380,"IT-IS","Isernia","province","IT-67")
            ,("IT","ITA",380,"IT-KR","Crotone","province","IT-78")
            ,("IT","ITA",380,"IT-LC","Lecco","province","IT-25")
            ,("IT","ITA",380,"IT-LE","Lecce","province","IT-75")
            ,("IT","ITA",380,"IT-LI","Livorno","province","IT-52")
            ,("IT","ITA",380,"IT-LO","Lodi","province","IT-25")
            ,("IT","ITA",380,"IT-LT","Latina","province","IT-62")
            ,("IT","ITA",380,"IT-LU","Lucca","province","IT-52")
            ,("IT","ITA",380,"IT-MB","Monza e Brianza","province","IT-25")
            ,("IT","ITA",380,"IT-MC","Macerata","province","IT-57")
            ,("IT","ITA",380,"IT-ME","Messina","metropolitan_city","IT-82")
            ,("IT","ITA",380,"IT-MI","Milano","metropolitan_city","IT-25")
            ,("IT","ITA",380,"IT-MN","Mantova","province","IT-25")
            ,("IT","ITA",380,"IT-MO","Modena","province","IT-45")
            ,("IT","ITA",380,"IT-MS","Massa-Carrara","province","IT-52")
            ,("IT","ITA",380,"IT-MT","Matera","province","IT-77")
            ,("IT","ITA",380,"IT-NA","Napoli","metropolitan_city","IT-72")
            ,("IT","ITA",380,"IT-NO","Novara","province","IT-21")
            ,("IT","ITA",380,"IT-NU","Nuoro","province","IT-88")
            ,("IT","ITA",380,"IT-OR","Oristano","province","IT-88")
            ,("IT","ITA",380,"IT-PA","Palermo","metropolitan_city","IT-82")
            ,("IT","ITA",380,"IT-PC","Piacenza","province","IT-45")
            ,("IT","ITA",380,"IT-PD","Padova","province","IT-34")
            ,("IT","ITA",380,"IT-PE","Pescara","province","IT-65")
            ,("IT","ITA",380,"IT-PG","Perugia","province","IT-55")
            ,("IT","ITA",380,"IT-PI","Pisa","province","IT-52")
            ,("IT","ITA",380,"IT-PN","Pordenone","decentralized_regional_entity","IT-36")
            ,("IT","ITA",380,"IT-PO","Prato","province","IT-52")
            ,("IT","ITA",380,"IT-PR","Parma","province","IT-45")
            ,("IT","ITA",380,"IT-PT","Pistoia","province","IT-52")
            ,("IT","ITA",380,"IT-PU","Pesaro e Urbino","province","IT-57")
            ,("IT","ITA",380,"IT-PV","Pavia","province","IT-25")
            ,("IT","ITA",380,"IT-PZ","Potenza","province","IT-77")
            ,("IT","ITA",380,"IT-RA","Ravenna","province","IT-45")
            ,("IT","ITA",380,"IT-RC",
                "Reggio Calabria","metropolitan_city","IT-78")
            ,("IT","ITA",380,"IT-RE","Reggio Emilia","province","IT-45")
            ,("IT","ITA",380,"IT-RG","Ragusa","free_municipal_consortia","IT-82")
            ,("IT","ITA",380,"IT-RI","Rieti","province","IT-62")
            ,("IT","ITA",380,"IT-RM","Roma","metropolitan_city","IT-62")
            ,("IT","ITA",380,"IT-RN","Rimini","province","IT-45")
            ,("IT","ITA",380,"IT-RO","Rovigo","province","IT-34")
            ,("IT","ITA",380,"IT-SA","Salerno","province","IT-72")
            ,("IT","ITA",380,"IT-SI","Siena","province","IT-52")
            ,("IT","ITA",380,"IT-SO","Sondrio","province","IT-25")
            ,("IT","ITA",380,"IT-SP","La Spezia","province","IT-42")
            ,("IT","ITA",380,"IT-SR","Siracusa","free_municipal_consortia","IT-82")
            ,("IT","ITA",380,"IT-SS","Sassari","province","IT-88")
            ,("IT","ITA",380,"IT-SU","Sud Sardegna","province","IT-88")
            ,("IT","ITA",380,"IT-SV","Savona","province","IT-42")
            ,("IT","ITA",380,"IT-TA","Taranto","province","IT-75")
            ,("IT","ITA",380,"IT-TE","Teramo","province","IT-65")
            ,("IT","ITA",380,"IT-TN","Trento","autonomous_province","IT-32")
            ,("IT","ITA",380,"IT-TO","Torino","metropolitan_city","IT-21")
            ,("IT","ITA",380,"IT-TP","Trapani","free_municipal_consortia","IT-82")
            ,("IT","ITA",380,"IT-TR","Terni","province","IT-55")
            ,("IT","ITA",380,"IT-TS","Trieste","decentralized_regional_entity","IT-36")
            ,("IT","ITA",380,"IT-TV","Treviso","province","IT-34")
            ,("IT","ITA",380,"IT-UD","Udine","decentralized_regional_entity","IT-36")
            ,("IT","ITA",380,"IT-VA","Varese","province","IT-25")
            ,("IT","ITA",380,"IT-VB","Verbano-Cusio-Ossola","province","IT-21")
            ,("IT","ITA",380,"IT-VC","Vercelli","province","IT-21")
            ,("IT","ITA",380,"IT-VE","Venezia","metropolitan_city","IT-34")
            ,("IT","ITA",380,"IT-VI","Vicenza","province","IT-34")
            ,("IT","ITA",380,"IT-VR","Verona","province","IT-34")
            ,("IT","ITA",380,"IT-VT","Viterbo","province","IT-62")
            ,("IT","ITA",380,"IT-VV","Vibo Valentia","province","IT-78")
            ,("JE","JEY",832,"JE-??","Jersey","country",NULL)
            ,("JM","JAM",388,"JM-01","Kingston","parish",NULL)
            ,("JM","JAM",388,"JM-02","Saint Andrew","parish",NULL)
            ,("JM","JAM",388,"JM-03","Saint Thomas","parish",NULL)
            ,("JM","JAM",388,"JM-04","Portland","parish",NULL)
            ,("JM","JAM",388,"JM-05","Saint Mary","parish",NULL)
            ,("JM","JAM",388,"JM-06","Saint Ann","parish",NULL)
            ,("JM","JAM",388,"JM-07","Trelawny","parish",NULL)
            ,("JM","JAM",388,"JM-08","Saint James","parish",NULL)
            ,("JM","JAM",388,"JM-09","Hanover","parish",NULL)
            ,("JM","JAM",388,"JM-10","Westmoreland","parish",NULL)
            ,("JM","JAM",388,"JM-11","Saint Elizabeth","parish",NULL)
            ,("JM","JAM",388,"JM-12","Manchester","parish",NULL)
            ,("JM","JAM",388,"JM-13","Clarendon","parish",NULL)
            ,("JM","JAM",388,"JM-14","Saint Catherine","parish",NULL)
            ,("JO","JOR",400,"JO-AJ","'Ajlūn","governorate",NULL)
            ,("JO","JOR",400,"JO-AM","Al 'A̅şimah","governorate",NULL)
            ,("JO","JOR",400,"JO-AQ","Al 'Aqabah","governorate",NULL)
            ,("JO","JOR",400,"JO-AT","Aţ Ţafīlah","governorate",NULL)
            ,("JO","JOR",400,"JO-AZ","Az Zarqā'","governorate",NULL)
            ,("JO","JOR",400,"JO-BA","Al Balqā'","governorate",NULL)
            ,("JO","JOR",400,"JO-IR","Irbid","governorate",NULL)
            ,("JO","JOR",400,"JO-JA","Jarash","governorate",NULL)
            ,("JO","JOR",400,"JO-KA","Al Karak","governorate",NULL)
            ,("JO","JOR",400,"JO-MA","Al Mafraq","governorate",NULL)
            ,("JO","JOR",400,"JO-MD","Mādabā","governorate",NULL)
            ,("JO","JOR",400,"JO-MN","Ma'ān","governorate",NULL)
            ,("JP","JPN",392,"JP-01","Hokkaidô","prefecture",NULL)
            ,("JP","JPN",392,"JP-02","Aomori","prefecture",NULL)
            ,("JP","JPN",392,"JP-03","Iwate","prefecture",NULL)
            ,("JP","JPN",392,"JP-04","Miyagi","prefecture",NULL)
            ,("JP","JPN",392,"JP-05","Akita","prefecture",NULL)
            ,("JP","JPN",392,"JP-06","Yamagata","prefecture",NULL)
            ,("JP","JPN",392,"JP-07","Hukusima","prefecture",NULL)
            ,("JP","JPN",392,"JP-08","Ibaraki","prefecture",NULL)
            ,("JP","JPN",392,"JP-09","Totigi","prefecture",NULL)
            ,("JP","JPN",392,"JP-10","Gunma","prefecture",NULL)
            ,("JP","JPN",392,"JP-11","Saitama","prefecture",NULL)
            ,("JP","JPN",392,"JP-12","Tiba","prefecture",NULL)
            ,("JP","JPN",392,"JP-13","Tôkyô","prefecture",NULL)
            ,("JP","JPN",392,"JP-14","Kanagawa","prefecture",NULL)
            ,("JP","JPN",392,"JP-15","Niigata","prefecture",NULL)
            ,("JP","JPN",392,"JP-16","Toyama","prefecture",NULL)
            ,("JP","JPN",392,"JP-17","Isikawa","prefecture",NULL)
            ,("JP","JPN",392,"JP-18","Hukui","prefecture",NULL)
            ,("JP","JPN",392,"JP-19","Yamanasi","prefecture",NULL)
            ,("JP","JPN",392,"JP-20","Nagano","prefecture",NULL)
            ,("JP","JPN",392,"JP-21","Gihu","prefecture",NULL)
            ,("JP","JPN",392,"JP-22","Sizuoka","prefecture",NULL)
            ,("JP","JPN",392,"JP-23","Aiti","prefecture",NULL)
            ,("JP","JPN",392,"JP-24","Mie","prefecture",NULL)
            ,("JP","JPN",392,"JP-25","Siga","prefecture",NULL)
            ,("JP","JPN",392,"JP-26","Kyôto","prefecture",NULL)
            ,("JP","JPN",392,"JP-27","Ôsaka","prefecture",NULL)
            ,("JP","JPN",392,"JP-28","Hyôgo","prefecture",NULL)
            ,("JP","JPN",392,"JP-29","Nara","prefecture",NULL)
            ,("JP","JPN",392,"JP-30","Wakayama","prefecture",NULL)
            ,("JP","JPN",392,"JP-31","Tottori","prefecture",NULL)
            ,("JP","JPN",392,"JP-32","Simane","prefecture",NULL)
            ,("JP","JPN",392,"JP-33","Okayama","prefecture",NULL)
            ,("JP","JPN",392,"JP-34","Hirosima","prefecture",NULL)
            ,("JP","JPN",392,"JP-35","Yamaguti","prefecture",NULL)
            ,("JP","JPN",392,"JP-36","Tokusima","prefecture",NULL)
            ,("JP","JPN",392,"JP-37","Kagawa","prefecture",NULL)
            ,("JP","JPN",392,"JP-38","Ehime","prefecture",NULL)
            ,("JP","JPN",392,"JP-39","Kôti","prefecture",NULL)
            ,("JP","JPN",392,"JP-40","Hukuoka","prefecture",NULL)
            ,("JP","JPN",392,"JP-41","Saga","prefecture",NULL)
            ,("JP","JPN",392,"JP-42","Nagasaki","prefecture",NULL)
            ,("JP","JPN",392,"JP-43","Kumamoto","prefecture",NULL)
            ,("JP","JPN",392,"JP-44","Ôita","prefecture",NULL)
            ,("JP","JPN",392,"JP-45","Miyazaki","prefecture",NULL)
            ,("JP","JPN",392,"JP-46","Kagosima","prefecture",NULL)
            ,("JP","JPN",392,"JP-47","Okinawa","prefecture",NULL)
            ,("KE","KEN",404,"KE-01","Baringo","county",NULL)
            ,("KE","KEN",404,"KE-02","Bomet","county",NULL)
            ,("KE","KEN",404,"KE-03","Bungoma","county",NULL)
            ,("KE","KEN",404,"KE-04","Busia","county",NULL)
            ,("KE","KEN",404,"KE-05","Elgeyo/Marakwet","county",NULL)
            ,("KE","KEN",404,"KE-06","Embu","county",NULL)
            ,("KE","KEN",404,"KE-07","Garissa","county",NULL)
            ,("KE","KEN",404,"KE-08","Homa Bay","county",NULL)
            ,("KE","KEN",404,"KE-09","Isiolo","county",NULL)
            ,("KE","KEN",404,"KE-10","Kajiado","county",NULL)
            ,("KE","KEN",404,"KE-11","Kakamega","county",NULL)
            ,("KE","KEN",404,"KE-12","Kericho","county",NULL)
            ,("KE","KEN",404,"KE-13","Kiambu","county",NULL)
            ,("KE","KEN",404,"KE-14","Kilifi","county",NULL)
            ,("KE","KEN",404,"KE-15","Kirinyaga","county",NULL)
            ,("KE","KEN",404,"KE-16","Kisii","county",NULL)
            ,("KE","KEN",404,"KE-17","Kisumu","county",NULL)
            ,("KE","KEN",404,"KE-18","Kitui","county",NULL)
            ,("KE","KEN",404,"KE-19","Kwale","county",NULL)
            ,("KE","KEN",404,"KE-20","Laikipia","county",NULL)
            ,("KE","KEN",404,"KE-21","Lamu","county",NULL)
            ,("KE","KEN",404,"KE-22","Machakos","county",NULL)
            ,("KE","KEN",404,"KE-23","Makueni","county",NULL)
            ,("KE","KEN",404,"KE-24","Mandera","county",NULL)
            ,("KE","KEN",404,"KE-25","Marsabit","county",NULL)
            ,("KE","KEN",404,"KE-26","Meru","county",NULL)
            ,("KE","KEN",404,"KE-27","Migori","county",NULL)
            ,("KE","KEN",404,"KE-28","Mombasa","county",NULL)
            ,("KE","KEN",404,"KE-29","Murang'a","county",NULL)
            ,("KE","KEN",404,"KE-30","Nairobi City","county",NULL)
            ,("KE","KEN",404,"KE-31","Nakuru","county",NULL)
            ,("KE","KEN",404,"KE-32","Nandi","county",NULL)
            ,("KE","KEN",404,"KE-33","Narok","county",NULL)
            ,("KE","KEN",404,"KE-34","Nyamira","county",NULL)
            ,("KE","KEN",404,"KE-35","Nyandarua","county",NULL)
            ,("KE","KEN",404,"KE-36","Nyeri","county",NULL)
            ,("KE","KEN",404,"KE-37","Samburu","county",NULL)
            ,("KE","KEN",404,"KE-38","Siaya","county",NULL)
            ,("KE","KEN",404,"KE-39","Taita/Taveta","county",NULL)
            ,("KE","KEN",404,"KE-40","Tana River","county",NULL)
            ,("KE","KEN",404,"KE-41","Tharaka-Nithi","county",NULL)
            ,("KE","KEN",404,"KE-42","Trans Nzoia","county",NULL)
            ,("KE","KEN",404,"KE-43","Turkana","county",NULL)
            ,("KE","KEN",404,"KE-44","Uasin Gishu","county",NULL)
            ,("KE","KEN",404,"KE-45","Vihiga","county",NULL)
            ,("KE","KEN",404,"KE-46","Wajir","county",NULL)
            ,("KE","KEN",404,"KE-47","West Pokot","county",NULL)
            ,("KG","KGZ",417,"KG-B","Batken","region",NULL)
            ,("KG","KGZ",417,"KG-C","Chüy","region",NULL)
            ,("KG","KGZ",417,"KG-GB","Bishkek Shaary","city",NULL)
            ,("KG","KGZ",417,"KG-GO","Osh Shaary","city",NULL)
            ,("KG","KGZ",417,"KG-J","Jalal-Abad","region",NULL)
            ,("KG","KGZ",417,"KG-N","Naryn","region",NULL)
            ,("KG","KGZ",417,"KG-O","Osh","region",NULL)
            ,("KG","KGZ",417,"KG-T","Talas","region",NULL)
            ,("KG","KGZ",417,"KG-Y","Ysyk-Köl","region",NULL)
            ,("KH","KHM",116,"KH-1","Banteay Mean Choăy","province",NULL)
            ,("KH","KHM",116,"KH-10","Kracheh","province",NULL)
            ,("KH","KHM",116,"KH-11","Mondol Kiri","province",NULL)
            ,("KH","KHM",116,"KH-12",
                "Phnom Penh","autonomous_municipality",NULL)
            ,("KH","KHM",116,"KH-13","Preah Vihear","province",NULL)
            ,("KH","KHM",116,"KH-14","Prey Veaeng","province",NULL)
            ,("KH","KHM",116,"KH-15","Pousaat","province",NULL)
            ,("KH","KHM",116,"KH-16","Rotanak Kiri","province",NULL)
            ,("KH","KHM",116,"KH-17","Siem Reab","province",NULL)
            ,("KH","KHM",116,"KH-18","Preah Sihanouk","province",NULL)
            ,("KH","KHM",116,"KH-19","Stueng Traeng","province",NULL)
            ,("KH","KHM",116,"KH-2","Baat Dambang","province",NULL)
            ,("KH","KHM",116,"KH-20","Svaay Rieng","province",NULL)
            ,("KH","KHM",116,"KH-21","Taakaev","province",NULL)
            ,("KH","KHM",116,"KH-22","Otdar Mean Chey","province",NULL)
            ,("KH","KHM",116,"KH-23","Kaeb","province",NULL)
            ,("KH","KHM",116,"KH-24","Pailin","province",NULL)
            ,("KH","KHM",116,"KH-25","Tbong Khmum","province",NULL)
            ,("KH","KHM",116,"KH-3","Kampong Chaam","province",NULL)
            ,("KH","KHM",116,"KH-4","Kampong Chhnang","province",NULL)
            ,("KH","KHM",116,"KH-5","Kampong Spueu","province",NULL)
            ,("KH","KHM",116,"KH-6","Kampong Thum","province",NULL)
            ,("KH","KHM",116,"KH-7","Kampot","province",NULL)
            ,("KH","KHM",116,"KH-8","Kandaal","province",NULL)
            ,("KH","KHM",116,"KH-9","Kaoh Kong","province",NULL)
            ,("KI","KIR",296,"KI-G","Gilbert Islands","island_group",NULL)
            ,("KI","KIR",296,"KI-L","Line Islands","island_group",NULL)
            ,("KI","KIR",296,"KI-P","Phoenix Islands","island_group",NULL)
            ,("KM","COM",174,"KM-A","Anjouan","island",NULL)
            ,("KM","COM",174,"KM-G","Grande Comore","island",NULL)
            ,("KM","COM",174,"KM-M","Mohéli","island",NULL)
            ,("KN","KNA",659,"KN-01",
                "Christ Church Nichola Town","parish","KN-K")
            ,("KN","KNA",659,"KN-02","Saint Anne Sandy Point","parish","KN-K")
            ,("KN","KNA",659,"KN-03","Saint George Basseterre","parish","KN-K")
            ,("KN","KNA",659,"KN-04","Saint George Gingerland","parish","KN-N")
            ,("KN","KNA",659,"KN-05","Saint James Windward","parish","KN-N")
            ,("KN","KNA",659,"KN-06","Saint John Capisterre","parish","KN-K")
            ,("KN","KNA",659,"KN-07","Saint John Figtree","parish","KN-N")
            ,("KN","KNA",659,"KN-08","Saint Mary Cayon","parish","KN-K")
            ,("KN","KNA",659,"KN-09","Saint Paul Capisterre","parish","KN-K")
            ,("KN","KNA",659,"KN-10","Saint Paul Charlestown","parish","KN-N")
            ,("KN","KNA",659,"KN-11","Saint Peter Basseterre","parish","KN-K")
            ,("KN","KNA",659,"KN-12","Saint Thomas Lowland","parish","KN-N")
            ,("KN","KNA",659,"KN-13",
                "Saint Thomas Middle Island","parish","KN-K")
            ,("KN","KNA",659,"KN-15","Trinity Palmetto Point","parish","KN-K")
            ,("KN","KNA",659,"KN-K","Saint Kitts","state",NULL)
            ,("KN","KNA",659,"KN-N","Nevis","state",NULL)
            ,("KP","PRK",408,"KP-01","Pyongyang","capital_city",NULL)
            ,("KP","PRK",408,"KP-02","South Pyongan","province",NULL)
            ,("KP","PRK",408,"KP-03","North Pyongan","province",NULL)
            ,("KP","PRK",408,"KP-04","Chagang","province",NULL)
            ,("KP","PRK",408,"KP-05","South Hwanghae","province",NULL)
            ,("KP","PRK",408,"KP-06","North Hwanghae","province",NULL)
            ,("KP","PRK",408,"KP-07","Kangwon","province",NULL)
            ,("KP","PRK",408,"KP-08","South Hamgyong","province",NULL)
            ,("KP","PRK",408,"KP-09","North Hamgyong","province",NULL)
            ,("KP","PRK",408,"KP-10","Ryanggang","province",NULL)
            ,("KP","PRK",408,"KP-13","Rason","special_city",NULL)
            ,("KP","PRK",408,"KP-14","Nampo","metropolitan_city",NULL)
            ,("KP","PRK",408,"KP-15","Kaesong","metropolitan_city",NULL)
            ,("KR","KOR",410,"KR-11","Seoul","special_city",NULL)
            ,("KR","KOR",410,"KR-26","Busan","metropolitan_city",NULL)
            ,("KR","KOR",410,"KR-27","Daegu","metropolitan_city",NULL)
            ,("KR","KOR",410,"KR-28","Incheon","metropolitan_city",NULL)
            ,("KR","KOR",410,"KR-29","Gwangju","metropolitan_city",NULL)
            ,("KR","KOR",410,"KR-30","Daejeon","metropolitan_city",NULL)
            ,("KR","KOR",410,"KR-31","Ulsan","metropolitan_city",NULL)
            ,("KR","KOR",410,"KR-41","Gyeonggi","province",NULL)
            ,("KR","KOR",410,"KR-42","Gangwon","province",NULL)
            ,("KR","KOR",410,"KR-43","North Chungcheong","province",NULL)
            ,("KR","KOR",410,"KR-44","South Chungcheong","province",NULL)
            ,("KR","KOR",410,"KR-45","North Jeolla","province",NULL)
            ,("KR","KOR",410,"KR-46","South Jeolla","province",NULL)
            ,("KR","KOR",410,"KR-47","North Gyeongsang","province",NULL)
            ,("KR","KOR",410,"KR-48","South Gyeongsang","province",NULL)
            ,("KR","KOR",410,"KR-49","Jeju","special_self-governing_province",NULL)
            ,("KR","KOR",410,"KR-50","Sejong","special_self-governing_city",NULL)
            ,("KW","KWT",414,"KW-AH","Al Aḩmadī","governorate",NULL)
            ,("KW","KWT",414,"KW-FA","Al Farwānīyah","governorate",NULL)
            ,("KW","KWT",414,"KW-HA","Ḩawallī","governorate",NULL)
            ,("KW","KWT",414,"KW-JA","Al Jahrā'","governorate",NULL)
            ,("KW","KWT",414,"KW-KU","Al 'Āşimah","governorate",NULL)
            ,("KW","KWT",414,"KW-MU","Mubārak al Kabīr","governorate",NULL)
            ,("KY","CYM",136,"KY-??","Cayman Islands","country",NULL)
            ,("KZ","KAZ",398,"KZ-10","Abay oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-11","Aqmola oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-15","Aqtöbe oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-19","Almaty oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-23","Atyraū oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-27","Batys Qazaqstan oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-31","Zhambyl oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-33","Zhetisū oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-35","Qaraghandy oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-39","Qostanay oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-43","Qyzylorda oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-47","Mangghystaū oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-55","Pavlodar oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-59",
                "Soltüstik Qazaqstan oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-61","Türkistan oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-62","Ulytaū oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-63","Shyghys Qazaqstan oblysy","region",NULL)
            ,("KZ","KAZ",398,"KZ-71","Astana","city",NULL)
            ,("KZ","KAZ",398,"KZ-75","Almaty","city",NULL)
            ,("KZ","KAZ",398,"KZ-79","Shymkent","city",NULL)
            ,("LA","LAO",418,"LA-AT","Attapu","province",NULL)
            ,("LA","LAO",418,"LA-BK","Bokèo","province",NULL)
            ,("LA","LAO",418,"LA-BL","Bolikhamxai","province",NULL)
            ,("LA","LAO",418,"LA-CH","Champasak","province",NULL)
            ,("LA","LAO",418,"LA-HO","Houaphan","province",NULL)
            ,("LA","LAO",418,"LA-KH","Khammouan","province",NULL)
            ,("LA","LAO",418,"LA-LM","Louang Namtha","province",NULL)
            ,("LA","LAO",418,"LA-LP","Louangphabang","province",NULL)
            ,("LA","LAO",418,"LA-OU","Oudômxai","province",NULL)
            ,("LA","LAO",418,"LA-PH","Phôngsali","province",NULL)
            ,("LA","LAO",418,"LA-SL","Salavan","province",NULL)
            ,("LA","LAO",418,"LA-SV","Savannakhét","province",NULL)
            ,("LA","LAO",418,"LA-VI","Viangchan","province",NULL)
            ,("LA","LAO",418,"LA-VT","Viangchan","prefecture",NULL)
            ,("LA","LAO",418,"LA-XA","Xaignabouli","province",NULL)
            ,("LA","LAO",418,"LA-XE","Xékong","province",NULL)
            ,("LA","LAO",418,"LA-XI","Xiangkhouang","province",NULL)
            ,("LA","LAO",418,"LA-XS","Xaisômboun","province",NULL)
            ,("LB","LBN",422,"LB-AK","Aakkâr","governorate",NULL)
            ,("LB","LBN",422,"LB-AS","Liban-Nord","governorate",NULL)
            ,("LB","LBN",422,"LB-BA","Beyrouth","governorate",NULL)
            ,("LB","LBN",422,"LB-BH","Baalbek-Hermel","governorate",NULL)
            ,("LB","LBN",422,"LB-BI","Béqaa","governorate",NULL)
            ,("LB","LBN",422,"LB-JA","Liban-Sud","governorate",NULL)
            ,("LB","LBN",422,"LB-JL","Mont-Liban","governorate",NULL)
            ,("LB","LBN",422,"LB-NA","Nabatîyé","governorate",NULL)
            ,("LC","LCA",662,"LC-01","Anse la Raye","district",NULL)
            ,("LC","LCA",662,"LC-02","Castries","district",NULL)
            ,("LC","LCA",662,"LC-03","Choiseul","district",NULL)
            ,("LC","LCA",662,"LC-05","Dennery","district",NULL)
            ,("LC","LCA",662,"LC-06","Gros Islet","district",NULL)
            ,("LC","LCA",662,"LC-07","Laborie","district",NULL)
            ,("LC","LCA",662,"LC-08","Micoud","district",NULL)
            ,("LC","LCA",662,"LC-10","Soufrière","district",NULL)
            ,("LC","LCA",662,"LC-11","Vieux Fort","district",NULL)
            ,("LC","LCA",662,"LC-12","Canaries","district",NULL)
            ,("LI","LIE",438,"LI-01","Balzers","commune",NULL)
            ,("LI","LIE",438,"LI-02","Eschen","commune",NULL)
            ,("LI","LIE",438,"LI-03","Gamprin","commune",NULL)
            ,("LI","LIE",438,"LI-04","Mauren","commune",NULL)
            ,("LI","LIE",438,"LI-05","Planken","commune",NULL)
            ,("LI","LIE",438,"LI-06","Ruggell","commune",NULL)
            ,("LI","LIE",438,"LI-07","Schaan","commune",NULL)
            ,("LI","LIE",438,"LI-08","Schellenberg","commune",NULL)
            ,("LI","LIE",438,"LI-09","Triesen","commune",NULL)
            ,("LI","LIE",438,"LI-10","Triesenberg","commune",NULL)
            ,("LI","LIE",438,"LI-11","Vaduz","commune",NULL)
            ,("LK","LKA",144,"LK-1","Western Province","province",NULL)
            ,("LK","LKA",144,"LK-11","Colombo","district","LK-1")
            ,("LK","LKA",144,"LK-12","Gampaha","district","LK-1")
            ,("LK","LKA",144,"LK-13","Kalutara","district","LK-1")
            ,("LK","LKA",144,"LK-2","Central Province","province",NULL)
            ,("LK","LKA",144,"LK-21","Kandy","district","LK-2")
            ,("LK","LKA",144,"LK-22","Matale","district","LK-2")
            ,("LK","LKA",144,"LK-23","Nuwara Eliya","district","LK-2")
            ,("LK","LKA",144,"LK-3","Southern Province","province",NULL)
            ,("LK","LKA",144,"LK-31","Galle","district","LK-3")
            ,("LK","LKA",144,"LK-32","Matara","district","LK-3")
            ,("LK","LKA",144,"LK-33","Hambantota","district","LK-3")
            ,("LK","LKA",144,"LK-4","Northern Province","province",NULL)
            ,("LK","LKA",144,"LK-41","Jaffna","district","LK-4")
            ,("LK","LKA",144,"LK-42","Kilinochchi","district","LK-4")
            ,("LK","LKA",144,"LK-43","Mannar","district","LK-4")
            ,("LK","LKA",144,"LK-44","Vavuniya","district","LK-4")
            ,("LK","LKA",144,"LK-45","Mullaittivu","district","LK-4")
            ,("LK","LKA",144,"LK-5","Eastern Province","province",NULL)
            ,("LK","LKA",144,"LK-51","Batticaloa","district","LK-5")
            ,("LK","LKA",144,"LK-52","Ampara","district","LK-5")
            ,("LK","LKA",144,"LK-53","Trincomalee","district","LK-5")
            ,("LK","LKA",144,"LK-6","North Western Province","province",NULL)
            ,("LK","LKA",144,"LK-61","Kurunegala","district","LK-6")
            ,("LK","LKA",144,"LK-62","Puttalam","district","LK-6")
            ,("LK","LKA",144,"LK-7","North Central Province","province",NULL)
            ,("LK","LKA",144,"LK-71","Anuradhapura","district","LK-7")
            ,("LK","LKA",144,"LK-72","Polonnaruwa","district","LK-7")
            ,("LK","LKA",144,"LK-8","Uva Province","province",NULL)
            ,("LK","LKA",144,"LK-81","Badulla","district","LK-8")
            ,("LK","LKA",144,"LK-82","Monaragala","district","LK-8")
            ,("LK","LKA",144,"LK-9","Sabaragamuwa Province","province",NULL)
            ,("LK","LKA",144,"LK-91","Ratnapura","district","LK-9")
            ,("LK","LKA",144,"LK-92","Kegalla","district","LK-9")
            ,("LR","LBR",430,"LR-BG","Bong","county",NULL)
            ,("LR","LBR",430,"LR-BM","Bomi","county",NULL)
            ,("LR","LBR",430,"LR-CM","Grand Cape Mount","county",NULL)
            ,("LR","LBR",430,"LR-GB","Grand Bassa","county",NULL)
            ,("LR","LBR",430,"LR-GG","Grand Gedeh","county",NULL)
            ,("LR","LBR",430,"LR-GK","Grand Kru","county",NULL)
            ,("LR","LBR",430,"LR-GP","Gbarpolu","county",NULL)
            ,("LR","LBR",430,"LR-LO","Lofa","county",NULL)
            ,("LR","LBR",430,"LR-MG","Margibi","county",NULL)
            ,("LR","LBR",430,"LR-MO","Montserrado","county",NULL)
            ,("LR","LBR",430,"LR-MY","Maryland","county",NULL)
            ,("LR","LBR",430,"LR-NI","Nimba","county",NULL)
            ,("LR","LBR",430,"LR-RG","River Gee","county",NULL)
            ,("LR","LBR",430,"LR-RI","River Cess","county",NULL)
            ,("LR","LBR",430,"LR-SI","Sinoe","county",NULL)
            ,("LS","LSO",426,"LS-A","Maseru","district",NULL)
            ,("LS","LSO",426,"LS-B","Botha-Bothe","district",NULL)
            ,("LS","LSO",426,"LS-C","Leribe","district",NULL)
            ,("LS","LSO",426,"LS-D","Berea","district",NULL)
            ,("LS","LSO",426,"LS-E","Mafeteng","district",NULL)
            ,("LS","LSO",426,"LS-F","Mohale's Hoek","district",NULL)
            ,("LS","LSO",426,"LS-G","Quthing","district",NULL)
            ,("LS","LSO",426,"LS-H","Qacha's Nek","district",NULL)
            ,("LS","LSO",426,"LS-J","Mokhotlong","district",NULL)
            ,("LS","LSO",426,"LS-K","Thaba-Tseka","district",NULL)
            ,("LT","LTU",440,"LT-01","Akmenė","district_municipality","SA")
            ,("LT","LTU",440,"LT-02",
                "Alytaus miestas","city_municipality","AL")
            ,("LT","LTU",440,"LT-03","Alytus","district_municipality","AL")
            ,("LT","LTU",440,"LT-04","Anykščiai","district_municipality","UT")
            ,("LT","LTU",440,"LT-05","Birštonas","municipality","KU")
            ,("LT","LTU",440,"LT-06","Biržai","district_municipality","PN")
            ,("LT","LTU",440,"LT-07","Druskininkai","municipality","AL")
            ,("LT","LTU",440,"LT-08","Elektrėnai","municipality","VL")
            ,("LT","LTU",440,"LT-09","Ignalina","district_municipality","UT")
            ,("LT","LTU",440,"LT-10","Jonava","district_municipality","KU")
            ,("LT","LTU",440,"LT-11","Joniškis","district_municipality","SA")
            ,("LT","LTU",440,"LT-12","Jurbarkas","district_municipality","TA")
            ,("LT","LTU",440,"LT-13","Kaišiadorys","district_municipality","KU")
            ,("LT","LTU",440,"LT-14","Kalvarija","municipality","MR")
            ,("LT","LTU",440,"LT-15","Kauno miestas","city_municipality","KU")
            ,("LT","LTU",440,"LT-16","Kaunas","district_municipality","KU")
            ,("LT","LTU",440,"LT-17","Kazlų Rūdos","municipality","MR")
            ,("LT","LTU",440,"LT-18","Kėdainiai","district_municipality","KU")
            ,("LT","LTU",440,"LT-19","Kelmė","district_municipality","SA")
            ,("LT","LTU",440,"LT-20",
                "Klaipėdos miestas","city_municipality","KL")
            ,("LT","LTU",440,"LT-21","Klaipėda","district_municipality","KL")
            ,("LT","LTU",440,"LT-22","Kretinga","district_municipality","KL")
            ,("LT","LTU",440,"LT-23","Kupiškis","district_municipality","PN")
            ,("LT","LTU",440,"LT-24","Lazdijai","district_municipality","AL")
            ,("LT","LTU",440,"LT-25","Marijampolė","district_municipality","MR")
            ,("LT","LTU",440,"LT-26","Mažeikiai","district_municipality","TE")
            ,("LT","LTU",440,"LT-27","Molėtai","district_municipality","UT")
            ,("LT","LTU",440,"LT-28","Neringa","municipality","KL")
            ,("LT","LTU",440,"LT-29","Pagėgiai","municipality","TA")
            ,("LT","LTU",440,"LT-30","Pakruojis","district_municipality","SA")
            ,("LT","LTU",440,"LT-31",
                "Palangos miestas","city_municipality","KL")
            ,("LT","LTU",440,"LT-32",
                "Panevėžio miestas","city_municipality","PN")
            ,("LT","LTU",440,"LT-33","Panevėžys","district_municipality","PN")
            ,("LT","LTU",440,"LT-34","Pasvalys","district_municipality","PN")
            ,("LT","LTU",440,"LT-35","Plungė","district_municipality","TE")
            ,("LT","LTU",440,"LT-36","Prienai","district_municipality","KU")
            ,("LT","LTU",440,"LT-37","Radviliškis","district_municipality","SA")
            ,("LT","LTU",440,"LT-38","Raseiniai","district_municipality","KU")
            ,("LT","LTU",440,"LT-39","Rietavas","municipality","TE")
            ,("LT","LTU",440,"LT-40","Rokiškis","district_municipality","PN")
            ,("LT","LTU",440,"LT-41","Šakiai","district_municipality","MR")
            ,("LT","LTU",440,"LT-42","Šalčininkai","district_municipality","VL")
            ,("LT","LTU",440,"LT-43",
                "Šiaulių miestas","city_municipality","SA")
            ,("LT","LTU",440,"LT-44","Šiauliai","district_municipality","SA")
            ,("LT","LTU",440,"LT-45","Šilalė","district_municipality","TA")
            ,("LT","LTU",440,"LT-46","Šilutė","district_municipality","KL")
            ,("LT","LTU",440,"LT-47","Širvintos","district_municipality","VL")
            ,("LT","LTU",440,"LT-48","Skuodas","district_municipality","KL")
            ,("LT","LTU",440,"LT-49","Švenčionys","district_municipality","VL")
            ,("LT","LTU",440,"LT-50","Tauragė","district_municipality","TA")
            ,("LT","LTU",440,"LT-51","Telšiai","district_municipality","TE")
            ,("LT","LTU",440,"LT-52","Trakai","district_municipality","VL")
            ,("LT","LTU",440,"LT-53","Ukmergė","district_municipality","VL")
            ,("LT","LTU",440,"LT-54","Utena","district_municipality","UT")
            ,("LT","LTU",440,"LT-55","Varėna","district_municipality","AL")
            ,("LT","LTU",440,"LT-56","Vilkaviškis","district_municipality","MR")
            ,("LT","LTU",440,"LT-57",
                "Vilniaus miestas","city_municipality","VL")
            ,("LT","LTU",440,"LT-58","Vilnius","district_municipality","VL")
            ,("LT","LTU",440,"LT-59","Visaginas","municipality","UT")
            ,("LT","LTU",440,"LT-60","Zarasai","district_municipality","UT")
            ,("LT","LTU",440,"LT-AL","Alytaus apskritis","county",NULL)
            ,("LT","LTU",440,"LT-KL","Klaipėdos apskritis","county",NULL)
            ,("LT","LTU",440,"LT-KU","Kauno apskritis","county",NULL)
            ,("LT","LTU",440,"LT-MR","Marijampolės apskritis","county",NULL)
            ,("LT","LTU",440,"LT-PN","Panevėžio apskritis","county",NULL)
            ,("LT","LTU",440,"LT-SA","Šiaulių apskritis","county",NULL)
            ,("LT","LTU",440,"LT-TA","Tauragės apskritis","county",NULL)
            ,("LT","LTU",440,"LT-TE","Telšių apskritis","county",NULL)
            ,("LT","LTU",440,"LT-UT","Utenos apskritis","county",NULL)
            ,("LT","LTU",440,"LT-VL","Vilniaus apskritis","county",NULL)
            ,("LU","LUX",442,"LU-CA","Capellen","canton",NULL)
            ,("LU","LUX",442,"LU-CL","Clerf","canton",NULL)
            ,("LU","LUX",442,"LU-DI","Diekirch","canton",NULL)
            ,("LU","LUX",442,"LU-EC","Echternach","canton",NULL)
            ,("LU","LUX",442,"LU-ES","Esch an der Alzette","canton",NULL)
            ,("LU","LUX",442,"LU-GR","Grevenmacher","canton",NULL)
            ,("LU","LUX",442,"LU-LU","Luxemburg","canton",NULL)
            ,("LU","LUX",442,"LU-ME","Mersch","canton",NULL)
            ,("LU","LUX",442,"LU-RD","Redingen","canton",NULL)
            ,("LU","LUX",442,"LU-RM","Remich","canton",NULL)
            ,("LU","LUX",442,"LU-VD","Vianden","canton",NULL)
            ,("LU","LUX",442,"LU-WI","Wiltz","canton",NULL)
            ,("LV","LVA",428,"LV-002","Aizkraukles novads","municipality",NULL)
            ,("LV","LVA",428,"LV-007","Alūksnes novads","municipality",NULL)
            ,("LV","LVA",428,"LV-011","Ādažu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-015","Balvu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-016","Bauskas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-022","Cēsu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-026","Dobeles novads","municipality",NULL)
            ,("LV","LVA",428,"LV-033","Gulbenes novads","municipality",NULL)
            ,("LV","LVA",428,"LV-041","Jelgavas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-042","Jēkabpils novads","municipality",NULL)
            ,("LV","LVA",428,"LV-047","Krāslavas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-050","Kuldīgas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-052","Ķekavas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-054","Limbažu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-056","Līvānu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-058","Ludzas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-059","Madonas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-062","Mārupes novads","municipality",NULL)
            ,("LV","LVA",428,"LV-067","Ogres novads","municipality",NULL)
            ,("LV","LVA",428,"LV-068","Olaines novads","municipality",NULL)
            ,("LV","LVA",428,"LV-073","Preiļu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-077","Rēzeknes novads","municipality",NULL)
            ,("LV","LVA",428,"LV-080","Ropažu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-087","Salaspils novads","municipality",NULL)
            ,("LV","LVA",428,"LV-088","Saldus novads","municipality",NULL)
            ,("LV","LVA",428,"LV-089","Saulkrastu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-091","Siguldas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-094","Smiltenes novads","municipality",NULL)
            ,("LV","LVA",428,"LV-097","Talsu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-099","Tukuma novads","municipality",NULL)
            ,("LV","LVA",428,"LV-101","Valkas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-102","Varakļānu novads","municipality",NULL)
            ,("LV","LVA",428,"LV-106","Ventspils novads","municipality",NULL)
            ,("LV","LVA",428,"LV-111",
                "Augšdaugavas novads","municipality",NULL)
            ,("LV","LVA",428,"LV-112",
                "Dienvidkurzemes Novads","municipality",NULL)
            ,("LV","LVA",428,"LV-113","Valmieras Novads","municipality",NULL)
            ,("LV","LVA",428,"LV-DGV","Daugavpils","state_city",NULL)
            ,("LV","LVA",428,"LV-JEL","Jelgava","state_city",NULL)
            ,("LV","LVA",428,"LV-JUR","Jūrmala","state_city",NULL)
            ,("LV","LVA",428,"LV-LPX","Liepāja","state_city",NULL)
            ,("LV","LVA",428,"LV-REZ","Rēzekne","state_city",NULL)
            ,("LV","LVA",428,"LV-RIX","Rīga","state_city",NULL)
            ,("LV","LVA",428,"LV-VEN","Ventspils","state_city",NULL)
            ,("LY","LBY",434,"LY-BA","Banghāzī","popularate",NULL)
            ,("LY","LBY",434,"LY-BU","Al Buţnān","popularate",NULL)
            ,("LY","LBY",434,"LY-DR","Darnah","popularate",NULL)
            ,("LY","LBY",434,"LY-GT","Ghāt","popularate",NULL)
            ,("LY","LBY",434,"LY-JA","Al Jabal al Akhḑar","popularate",NULL)
            ,("LY","LBY",434,"LY-JG","Al Jabal al Gharbī","popularate",NULL)
            ,("LY","LBY",434,"LY-JI","Al Jafārah","popularate",NULL)
            ,("LY","LBY",434,"LY-JU","Al Jufrah","popularate",NULL)
            ,("LY","LBY",434,"LY-KF","Al Kufrah","popularate",NULL)
            ,("LY","LBY",434,"LY-MB","Al Marqab","popularate",NULL)
            ,("LY","LBY",434,"LY-MI","Mişrātah","popularate",NULL)
            ,("LY","LBY",434,"LY-MJ","Al Marj","popularate",NULL)
            ,("LY","LBY",434,"LY-MQ","Murzuq","popularate",NULL)
            ,("LY","LBY",434,"LY-NL","Nālūt","popularate",NULL)
            ,("LY","LBY",434,"LY-NQ","An Nuqāţ al Khams","popularate",NULL)
            ,("LY","LBY",434,"LY-SB","Sabhā","popularate",NULL)
            ,("LY","LBY",434,"LY-SR","Surt","popularate",NULL)
            ,("LY","LBY",434,"LY-TB","Ţarābulus","popularate",NULL)
            ,("LY","LBY",434,"LY-WA","Al Wāḩāt","popularate",NULL)
            ,("LY","LBY",434,"LY-WD","Wādī al Ḩayāt","popularate",NULL)
            ,("LY","LBY",434,"LY-WS","Wādī ash Shāţi'","popularate",NULL)
            ,("LY","LBY",434,"LY-ZA","Az Zāwiyah","popularate",NULL)
            ,("MA","MAR",504,"MA-01","Tanger-Tétouan-Al Hoceïma","region",NULL)
            ,("MA","MAR",504,"MA-02","L'Oriental","region",NULL)
            ,("MA","MAR",504,"MA-03","Fès-Meknès","region",NULL)
            ,("MA","MAR",504,"MA-04","Rabat-Salé-Kénitra","region",NULL)
            ,("MA","MAR",504,"MA-05","Béni Mellal-Khénifra","region",NULL)
            ,("MA","MAR",504,"MA-06","Casablanca-Settat","region",NULL)
            ,("MA","MAR",504,"MA-07","Marrakech-Safi","region",NULL)
            ,("MA","MAR",504,"MA-08","Drâa-Tafilalet","region",NULL)
            ,("MA","MAR",504,"MA-09","Souss-Massa","region",NULL)
            ,("MA","MAR",504,"MA-10","Guelmim-Oued Noun","region",NULL)
            ,("MA","MAR",504,"MA-11","Laâyoune-Sakia El Hamra","region",NULL)
            ,("MA","MAR",504,"MA-12","Dakhla-Oued Ed-Dahab","region",NULL)
            ,("MA","MAR",504,"MA-AGD","Agadir-Ida-Ou-Tanane","prefecture","MA-9")
            ,("MA","MAR",504,"MA-AOU","Aousserd","province","MA-12")
            ,("MA","MAR",504,"MA-ASZ","Assa-Zag","province","MA-10")
            ,("MA","MAR",504,"MA-AZI","Azilal","province","MA-5")
            ,("MA","MAR",504,"MA-BEM","Béni Mellal","province","MA-5")
            ,("MA","MAR",504,"MA-BER","Berkane","province","MA-2")
            ,("MA","MAR",504,"MA-BES","Benslimane","province","MA-6")
            ,("MA","MAR",504,"MA-BOD","Boujdour","province","MA-11")
            ,("MA","MAR",504,"MA-BOM","Boulemane","province","MA-3")
            ,("MA","MAR",504,"MA-BRR","Berrechid","province","MA-6")
            ,("MA","MAR",504,"MA-CAS","Casablanca","prefecture","MA-6")
            ,("MA","MAR",504,"MA-CHE","Chefchaouen","province","MA-1")
            ,("MA","MAR",504,"MA-CHI","Chichaoua","province","MA-7")
            ,("MA","MAR",504,"MA-CHT","Chtouka-Ait Baha","province","MA-6")
            ,("MA","MAR",504,"MA-DRI","Driouch","province","MA-2")
            ,("MA","MAR",504,"MA-ERR","Errachidia","province","MA-8")
            ,("MA","MAR",504,"MA-ESI","Essaouira","province","MA-7")
            ,("MA","MAR",504,"MA-ESM","Es-Semara","province","MA-11")
            ,("MA","MAR",504,"MA-FAH","Fahs-Anjra","province","MA-1")
            ,("MA","MAR",504,"MA-FES","Fès","prefecture","MA-3")
            ,("MA","MAR",504,"MA-FIG","Figuig","province","MA-2")
            ,("MA","MAR",504,"MA-FQH","Fquih Ben Salah","province","MA-5")
            ,("MA","MAR",504,"MA-GUE","Guelmim","province","MA-10")
            ,("MA","MAR",504,"MA-GUF","Guercif","province","MA-2")
            ,("MA","MAR",504,"MA-HAJ","El Hajeb","province","MA-3")
            ,("MA","MAR",504,"MA-HAO","Al Haouz","province","MA-7")
            ,("MA","MAR",504,"MA-HOC","Al Hoceïma","province","MA-1")
            ,("MA","MAR",504,"MA-IFR","Ifrane","province","MA-3")
            ,("MA","MAR",504,"MA-INE",
                "Inezgane-Ait Melloul","prefecture","MA-9")
            ,("MA","MAR",504,"MA-JDI","El Jadida","province","MA-6")
            ,("MA","MAR",504,"MA-JRA","Jerada","province","MA-2")
            ,("MA","MAR",504,"MA-KEN","Kénitra","province","MA-4")
            ,("MA","MAR",504,"MA-KES","El Kelâa des Sraghna","province","MA-7")
            ,("MA","MAR",504,"MA-KHE","Khémisset","province","MA-4")
            ,("MA","MAR",504,"MA-KHN","Khénifra","province","MA-5")
            ,("MA","MAR",504,"MA-KHO","Khouribga","province","MA-5")
            ,("MA","MAR",504,"MA-LAA","Laâyoune","province","MA-11")
            ,("MA","MAR",504,"MA-LAR","Larache","province","MA-1")
            ,("MA","MAR",504,"MA-MAR","Marrakech","prefecture","MA-7")
            ,("MA","MAR",504,"MA-MDF","M'diq-Fnideq","prefecture","MA-1")
            ,("MA","MAR",504,"MA-MED","Médiouna","province","MA-6")
            ,("MA","MAR",504,"MA-MEK","Meknès","prefecture","MA-3")
            ,("MA","MAR",504,"MA-MID","Midelt","province","MA-8")
            ,("MA","MAR",504,"MA-MOH","Mohammadia","prefecture","MA-6")
            ,("MA","MAR",504,"MA-MOU","Moulay Yacoub","province","MA-3")
            ,("MA","MAR",504,"MA-NAD","Nador","province","MA-2")
            ,("MA","MAR",504,"MA-NOU","Nouaceur","province","MA-4")
            ,("MA","MAR",504,"MA-OUA","Ouarzazate","province","MA-8")
            ,("MA","MAR",504,"MA-OUD","Oued Ed-Dahab","province","MA-12")
            ,("MA","MAR",504,"MA-OUJ","Oujda-Angad","prefecture","MA-2")
            ,("MA","MAR",504,"MA-OUZ","Ouezzane","province","MA-1")
            ,("MA","MAR",504,"MA-RAB","Rabat","prefecture","MA-4")
            ,("MA","MAR",504,"MA-REH","Rehamna","province","MA-7")
            ,("MA","MAR",504,"MA-SAF","Safi","province","MA-7")
            ,("MA","MAR",504,"MA-SAL","Salé","prefecture","MA-4")
            ,("MA","MAR",504,"MA-SEF","Sefrou","province","MA-3")
            ,("MA","MAR",504,"MA-SET","Settat","province","MA-6")
            ,("MA","MAR",504,"MA-SIB","Sidi Bennour","province","MA-6")
            ,("MA","MAR",504,"MA-SIF","Sidi Ifni","province","MA-10")
            ,("MA","MAR",504,"MA-SIK","Sidi Kacem","province","MA-4")
            ,("MA","MAR",504,"MA-SIL","Sidi Slimane","province","MA-4")
            ,("MA","MAR",504,"MA-SKH","Skhirate-Témara","prefecture","MA-4")
            ,("MA","MAR",504,"MA-TAF","Tarfaya","province","MA-11")
            ,("MA","MAR",504,"MA-TAI","Taourirt","province","MA-2")
            ,("MA","MAR",504,"MA-TAO","Taounate","province","MA-3")
            ,("MA","MAR",504,"MA-TAR","Taroudannt","province","MA-9")
            ,("MA","MAR",504,"MA-TAT","Tata","province","MA-9")
            ,("MA","MAR",504,"MA-TAZ","Taza","province","MA-3")
            ,("MA","MAR",504,"MA-TET","Tétouan","province","MA-1")
            ,("MA","MAR",504,"MA-TIN","Tinghir","province","MA-8")
            ,("MA","MAR",504,"MA-TIZ","Tiznit","province","MA-9")
            ,("MA","MAR",504,"MA-TNG","Tanger-Assilah","prefecture","MA-1")
            ,("MA","MAR",504,"MA-TNT","Tan-Tan","province","MA-10")
            ,("MA","MAR",504,"MA-YUS","Youssoufia","province","MA-7")
            ,("MA","MAR",504,"MA-ZAG","Zagora","province","MA-8")
            ,("MC","MCO",492,"MC-CL","La Colle","quarter",NULL)
            ,("MC","MCO",492,"MC-CO","La Condamine","quarter",NULL)
            ,("MC","MCO",492,"MC-FO","Fontvieille","quarter",NULL)
            ,("MC","MCO",492,"MC-GA","La Gare","quarter",NULL)
            ,("MC","MCO",492,"MC-JE","Jardin Exotique","quarter",NULL)
            ,("MC","MCO",492,"MC-LA","Larvotto","quarter",NULL)
            ,("MC","MCO",492,"MC-MA","Malbousquet","quarter",NULL)
            ,("MC","MCO",492,"MC-MC","Monte-Carlo","quarter",NULL)
            ,("MC","MCO",492,"MC-MG","Moneghetti","quarter",NULL)
            ,("MC","MCO",492,"MC-MO","Monaco-Ville","quarter",NULL)
            ,("MC","MCO",492,"MC-MU","Moulins","quarter",NULL)
            ,("MC","MCO",492,"MC-PH","Port-Hercule","quarter",NULL)
            ,("MC","MCO",492,"MC-SD","Sainte-Dévote","quarter",NULL)
            ,("MC","MCO",492,"MC-SO","La Source","quarter",NULL)
            ,("MC","MCO",492,"MC-SP","Spélugues","quarter",NULL)
            ,("MC","MCO",492,"MC-SR","Saint-Roman","quarter",NULL)
            ,("MC","MCO",492,"MC-VR","Vallon de la Rousse","quarter",NULL)
            ,("MD","MDA",498,"MD-AN","Anenii Noi","district",NULL)
            ,("MD","MDA",498,"MD-BA","Bălți","city",NULL)
            ,("MD","MDA",498,"MD-BD","Bender","city",NULL)
            ,("MD","MDA",498,"MD-BR","Briceni","district",NULL)
            ,("MD","MDA",498,"MD-BS","Basarabeasca","district",NULL)
            ,("MD","MDA",498,"MD-CA","Cahul","district",NULL)
            ,("MD","MDA",498,"MD-CL","Călărași","district",NULL)
            ,("MD","MDA",498,"MD-CM","Cimișlia","district",NULL)
            ,("MD","MDA",498,"MD-CR","Criuleni","district",NULL)
            ,("MD","MDA",498,"MD-CS","Căușeni","district",NULL)
            ,("MD","MDA",498,"MD-CT","Cantemir","district",NULL)
            ,("MD","MDA",498,"MD-CU","Chișinău","city",NULL)
            ,("MD","MDA",498,"MD-DO","Dondușeni","district",NULL)
            ,("MD","MDA",498,"MD-DR","Drochia","district",NULL)
            ,("MD","MDA",498,"MD-DU","Dubăsari","district",NULL)
            ,("MD","MDA",498,"MD-ED","Edineț","district",NULL)
            ,("MD","MDA",498,"MD-FA","Fălești","district",NULL)
            ,("MD","MDA",498,"MD-FL","Florești","district",NULL)
            ,("MD","MDA",498,"MD-GA",
                "Găgăuzia, Unitatea teritorială autonomă",
                "autonomous_territorial_unit",NULL)
            ,("MD","MDA",498,"MD-GL","Glodeni","district",NULL)
            ,("MD","MDA",498,"MD-HI","Hîncești","district",NULL)
            ,("MD","MDA",498,"MD-IA","Ialoveni","district",NULL)
            ,("MD","MDA",498,"MD-LE","Leova","district",NULL)
            ,("MD","MDA",498,"MD-NI","Nisporeni","district",NULL)
            ,("MD","MDA",498,"MD-OC","Ocnița","district",NULL)
            ,("MD","MDA",498,"MD-OR","Orhei","district",NULL)
            ,("MD","MDA",498,"MD-RE","Rezina","district",NULL)
            ,("MD","MDA",498,"MD-RI","Rîșcani","district",NULL)
            ,("MD","MDA",498,"MD-SD","Șoldănești","district",NULL)
            ,("MD","MDA",498,"MD-SI","Sîngerei","district",NULL)
            ,("MD","MDA",498,"MD-SN",
                "Stînga Nistrului, unitatea teritorială din",
                "territorial_unit",NULL)
            ,("MD","MDA",498,"MD-SO","Soroca","district",NULL)
            ,("MD","MDA",498,"MD-ST","Strășeni","district",NULL)
            ,("MD","MDA",498,"MD-SV","Ștefan Vodă","district",NULL)
            ,("MD","MDA",498,"MD-TA","Taraclia","district",NULL)
            ,("MD","MDA",498,"MD-TE","Telenești","district",NULL)
            ,("MD","MDA",498,"MD-UN","Ungheni","district",NULL)
            ,("ME","MNE",499,"ME-01","Andrijevica","municipality",NULL)
            ,("ME","MNE",499,"ME-02","Bar","municipality",NULL)
            ,("ME","MNE",499,"ME-03","Berane","municipality",NULL)
            ,("ME","MNE",499,"ME-04","Bijelo Polje","municipality",NULL)
            ,("ME","MNE",499,"ME-05","Budva","municipality",NULL)
            ,("ME","MNE",499,"ME-06","Cetinje","municipality",NULL)
            ,("ME","MNE",499,"ME-07","Danilovgrad","municipality",NULL)
            ,("ME","MNE",499,"ME-08","Herceg-Novi","municipality",NULL)
            ,("ME","MNE",499,"ME-09","Kolašin","municipality",NULL)
            ,("ME","MNE",499,"ME-10","Kotor","municipality",NULL)
            ,("ME","MNE",499,"ME-11","Mojkovac","municipality",NULL)
            ,("ME","MNE",499,"ME-12","Nikšić","municipality",NULL)
            ,("ME","MNE",499,"ME-13","Plav","municipality",NULL)
            ,("ME","MNE",499,"ME-14","Pljevlja","municipality",NULL)
            ,("ME","MNE",499,"ME-15","Plužine","municipality",NULL)
            ,("ME","MNE",499,"ME-16","Podgorica","municipality",NULL)
            ,("ME","MNE",499,"ME-17","Rožaje","municipality",NULL)
            ,("ME","MNE",499,"ME-18","Šavnik","municipality",NULL)
            ,("ME","MNE",499,"ME-19","Tivat","municipality",NULL)
            ,("ME","MNE",499,"ME-20","Ulcinj","municipality",NULL)
            ,("ME","MNE",499,"ME-21","Žabljak","municipality",NULL)
            ,("ME","MNE",499,"ME-22","Gusinje","municipality",NULL)
            ,("ME","MNE",499,"ME-23","Petnjica","municipality",NULL)
            ,("ME","MNE",499,"ME-24","Tuzi","municipality",NULL)
            ,("MF","MAF",663,"MF-??","Saint Martin","country",NULL)
            ,("MG","MDG",450,"MG-A","Toamasina","province",NULL)
            ,("MG","MDG",450,"MG-D","Antsiranana","province",NULL)
            ,("MG","MDG",450,"MG-F","Fianarantsoa","province",NULL)
            ,("MG","MDG",450,"MG-M","Mahajanga","province",NULL)
            ,("MG","MDG",450,"MG-T","Antananarivo","province",NULL)
            ,("MG","MDG",450,"MG-U","Toliara","province",NULL)
            ,("MH","MHL",584,"MH-ALK","Ailuk","municipality","MH-T")
            ,("MH","MHL",584,"MH-ALL","Ailinglaplap","municipality","MH-L")
            ,("MH","MHL",584,"MH-ARN","Arno","municipality","MH-T")
            ,("MH","MHL",584,"MH-AUR","Aur","municipality","MH-T")
            ,("MH","MHL",584,"MH-EBO","Ebon","municipality","MH-L")
            ,("MH","MHL",584,"MH-ENI",
                "Enewetak & Ujelang","municipality","MH-L")
            ,("MH","MHL",584,"MH-JAB","Jabat","municipality","MH-L")
            ,("MH","MHL",584,"MH-JAL","Jaluit","municipality","MH-L")
            ,("MH","MHL",584,"MH-KIL","Bikini & Kili","municipality","MH-L")
            ,("MH","MHL",584,"MH-KWA","Kwajalein","municipality","MH-L")
            ,("MH","MHL",584,"MH-L","Ralik chain","island_chain",NULL)
            ,("MH","MHL",584,"MH-LAE","Lae","municipality","MH-L")
            ,("MH","MHL",584,"MH-LIB","Lib","municipality","MH-L")
            ,("MH","MHL",584,"MH-LIK","Likiep","municipality","MH-T")
            ,("MH","MHL",584,"MH-MAJ","Majuro","municipality","MH-T")
            ,("MH","MHL",584,"MH-MAL","Maloelap","municipality","MH-T")
            ,("MH","MHL",584,"MH-MEJ","Mejit","municipality","MH-T")
            ,("MH","MHL",584,"MH-MIL","Mili","municipality","MH-T")
            ,("MH","MHL",584,"MH-NMK","Namdrik","municipality","MH-L")
            ,("MH","MHL",584,"MH-NMU","Namu","municipality","MH-L")
            ,("MH","MHL",584,"MH-RON","Rongelap","municipality","MH-L")
            ,("MH","MHL",584,"MH-T","Ratak chain","island_chain",NULL)
            ,("MH","MHL",584,"MH-UJA","Ujae","municipality","MH-L")
            ,("MH","MHL",584,"MH-UTI","Utrik","municipality","MH-T")
            ,("MH","MHL",584,"MH-WTH","Wotho","municipality","MH-L")
            ,("MH","MHL",584,"MH-WTJ","Wotje","municipality","MH-T")
            ,("MK","MKD",807,"MK-101","Veles","municipality",NULL)
            ,("MK","MKD",807,"MK-102","Gradsko","municipality",NULL)
            ,("MK","MKD",807,"MK-103","Demir Kapija","municipality",NULL)
            ,("MK","MKD",807,"MK-104","Kavadarci","municipality",NULL)
            ,("MK","MKD",807,"MK-105","Lozovo","municipality",NULL)
            ,("MK","MKD",807,"MK-106","Negotino","municipality",NULL)
            ,("MK","MKD",807,"MK-107","Rosoman","municipality",NULL)
            ,("MK","MKD",807,"MK-108","Sveti Nikole","municipality",NULL)
            ,("MK","MKD",807,"MK-109","Čaška","municipality",NULL)
            ,("MK","MKD",807,"MK-201","Berovo","municipality",NULL)
            ,("MK","MKD",807,"MK-202","Vinica","municipality",NULL)
            ,("MK","MKD",807,"MK-203","Delčevo","municipality",NULL)
            ,("MK","MKD",807,"MK-204","Zrnovci","municipality",NULL)
            ,("MK","MKD",807,"MK-205","Karbinci","municipality",NULL)
            ,("MK","MKD",807,"MK-206","Kočani","municipality",NULL)
            ,("MK","MKD",807,"MK-207",
                "Makedonska Kamenica","municipality",NULL)
            ,("MK","MKD",807,"MK-208","Pehčevo","municipality",NULL)
            ,("MK","MKD",807,"MK-209","Probištip","municipality",NULL)
            ,("MK","MKD",807,"MK-210","Češinovo-Obleševo","municipality",NULL)
            ,("MK","MKD",807,"MK-211","Štip","municipality",NULL)
            ,("MK","MKD",807,"MK-301","Vevčani","municipality",NULL)
            ,("MK","MKD",807,"MK-303","Debar","municipality",NULL)
            ,("MK","MKD",807,"MK-304","Debrca","municipality",NULL)
            ,("MK","MKD",807,"MK-307","Kičevo","municipality",NULL)
            ,("MK","MKD",807,"MK-308","Makedonski Brod","municipality",NULL)
            ,("MK","MKD",807,"MK-310","Ohrid","municipality",NULL)
            ,("MK","MKD",807,"MK-311","Plasnica","municipality",NULL)
            ,("MK","MKD",807,"MK-312","Struga","municipality",NULL)
            ,("MK","MKD",807,"MK-313","Centar Župa","municipality",NULL)
            ,("MK","MKD",807,"MK-401","Bogdanci","municipality",NULL)
            ,("MK","MKD",807,"MK-402","Bosilovo","municipality",NULL)
            ,("MK","MKD",807,"MK-403","Valandovo","municipality",NULL)
            ,("MK","MKD",807,"MK-404","Vasilevo","municipality",NULL)
            ,("MK","MKD",807,"MK-405","Gevgelija","municipality",NULL)
            ,("MK","MKD",807,"MK-406","Dojran","municipality",NULL)
            ,("MK","MKD",807,"MK-407","Konče","municipality",NULL)
            ,("MK","MKD",807,"MK-408","Novo Selo","municipality",NULL)
            ,("MK","MKD",807,"MK-409","Radoviš","municipality",NULL)
            ,("MK","MKD",807,"MK-410","Strumica","municipality",NULL)
            ,("MK","MKD",807,"MK-501","Bitola","municipality",NULL)
            ,("MK","MKD",807,"MK-502","Demir Hisar","municipality",NULL)
            ,("MK","MKD",807,"MK-503","Dolneni","municipality",NULL)
            ,("MK","MKD",807,"MK-504","Krivogaštani","municipality",NULL)
            ,("MK","MKD",807,"MK-505","Kruševo","municipality",NULL)
            ,("MK","MKD",807,"MK-506","Mogila","municipality",NULL)
            ,("MK","MKD",807,"MK-507","Novaci","municipality",NULL)
            ,("MK","MKD",807,"MK-508","Prilep","municipality",NULL)
            ,("MK","MKD",807,"MK-509","Resen","municipality",NULL)
            ,("MK","MKD",807,"MK-601","Bogovinje","municipality",NULL)
            ,("MK","MKD",807,"MK-602","Brvenica","municipality",NULL)
            ,("MK","MKD",807,"MK-603","Vrapčište","municipality",NULL)
            ,("MK","MKD",807,"MK-604","Gostivar","municipality",NULL)
            ,("MK","MKD",807,"MK-605","Želino","municipality",NULL)
            ,("MK","MKD",807,"MK-606","Jegunovce","municipality",NULL)
            ,("MK","MKD",807,"MK-607","Mavrovo i Rostuše","municipality",NULL)
            ,("MK","MKD",807,"MK-608","Tearce","municipality",NULL)
            ,("MK","MKD",807,"MK-609","Tetovo","municipality",NULL)
            ,("MK","MKD",807,"MK-701","Kratovo","municipality",NULL)
            ,("MK","MKD",807,"MK-702","Kriva Palanka","municipality",NULL)
            ,("MK","MKD",807,"MK-703","Kumanovo","municipality",NULL)
            ,("MK","MKD",807,"MK-704","Lipkovo","municipality",NULL)
            ,("MK","MKD",807,"MK-705","Rankovce","municipality",NULL)
            ,("MK","MKD",807,"MK-706","Staro Nagoričane","municipality",NULL)
            ,("MK","MKD",807,"MK-801","Aerodrom","municipality",NULL)
            ,("MK","MKD",807,"MK-802","Aračinovo","municipality",NULL)
            ,("MK","MKD",807,"MK-803","Butel","municipality",NULL)
            ,("MK","MKD",807,"MK-804","Gazi Baba","municipality",NULL)
            ,("MK","MKD",807,"MK-805","Gjorče Petrov","municipality",NULL)
            ,("MK","MKD",807,"MK-806","Zelenikovo","municipality",NULL)
            ,("MK","MKD",807,"MK-807","Ilinden","municipality",NULL)
            ,("MK","MKD",807,"MK-808","Karpoš","municipality",NULL)
            ,("MK","MKD",807,"MK-809","Kisela Voda","municipality",NULL)
            ,("MK","MKD",807,"MK-810","Petrovec","municipality",NULL)
            ,("MK","MKD",807,"MK-811","Saraj","municipality",NULL)
            ,("MK","MKD",807,"MK-812","Sopište","municipality",NULL)
            ,("MK","MKD",807,"MK-813","Studeničani","municipality",NULL)
            ,("MK","MKD",807,"MK-814","Centar","municipality",NULL)
            ,("MK","MKD",807,"MK-815","Čair","municipality",NULL)
            ,("MK","MKD",807,"MK-816","Čučer-Sandevo","municipality",NULL)
            ,("MK","MKD",807,"MK-817","Šuto Orizari","municipality",NULL)
            ,("ML","MLI",466,"ML-1","Kayes","region",NULL)
            ,("ML","MLI",466,"ML-10","Taoudénit","region",NULL)
            ,("ML","MLI",466,"ML-2","Koulikoro","region",NULL)
            ,("ML","MLI",466,"ML-3","Sikasso","region",NULL)
            ,("ML","MLI",466,"ML-4","Ségou","region",NULL)
            ,("ML","MLI",466,"ML-5","Mopti","region",NULL)
            ,("ML","MLI",466,"ML-6","Tombouctou","region",NULL)
            ,("ML","MLI",466,"ML-7","Gao","region",NULL)
            ,("ML","MLI",466,"ML-8","Kidal","region",NULL)
            ,("ML","MLI",466,"ML-9","Ménaka","region",NULL)
            ,("ML","MLI",466,"ML-BKO","Bamako","district",NULL)
            ,("MM","MMR",104,"MM-01","Sagaing","region",NULL)
            ,("MM","MMR",104,"MM-02","Bago","region",NULL)
            ,("MM","MMR",104,"MM-03","Magway","region",NULL)
            ,("MM","MMR",104,"MM-04","Mandalay","region",NULL)
            ,("MM","MMR",104,"MM-05","Tanintharyi","region",NULL)
            ,("MM","MMR",104,"MM-06","Yangon","region",NULL)
            ,("MM","MMR",104,"MM-07","Ayeyarwady","region",NULL)
            ,("MM","MMR",104,"MM-11","Kachin","state",NULL)
            ,("MM","MMR",104,"MM-12","Kayah","state",NULL)
            ,("MM","MMR",104,"MM-13","Kayin","state",NULL)
            ,("MM","MMR",104,"MM-14","Chin","state",NULL)
            ,("MM","MMR",104,"MM-15","Mon","state",NULL)
            ,("MM","MMR",104,"MM-16","Rakhine","state",NULL)
            ,("MM","MMR",104,"MM-17","Shan","state",NULL)
            ,("MM","MMR",104,"MM-18","Nay Pyi Taw","union_territory",NULL)
            ,("MN","MNG",496,"MN-035","Orhon","province",NULL)
            ,("MN","MNG",496,"MN-037","Darhan uul","province",NULL)
            ,("MN","MNG",496,"MN-039","Hentiy","province",NULL)
            ,("MN","MNG",496,"MN-041","Hövsgöl","province",NULL)
            ,("MN","MNG",496,"MN-043","Hovd","province",NULL)
            ,("MN","MNG",496,"MN-046","Uvs","province",NULL)
            ,("MN","MNG",496,"MN-047","Töv","province",NULL)
            ,("MN","MNG",496,"MN-049","Selenge","province",NULL)
            ,("MN","MNG",496,"MN-051","Sühbaatar","province",NULL)
            ,("MN","MNG",496,"MN-053","Ömnögovĭ","province",NULL)
            ,("MN","MNG",496,"MN-055","Övörhangay","province",NULL)
            ,("MN","MNG",496,"MN-057","Dzavhan","province",NULL)
            ,("MN","MNG",496,"MN-059","Dundgovĭ","province",NULL)
            ,("MN","MNG",496,"MN-061","Dornod","province",NULL)
            ,("MN","MNG",496,"MN-063","Dornogovĭ","province",NULL)
            ,("MN","MNG",496,"MN-064","Govĭ-Sümber","province",NULL)
            ,("MN","MNG",496,"MN-065","Govĭ-Altay","province",NULL)
            ,("MN","MNG",496,"MN-067","Bulgan","province",NULL)
            ,("MN","MNG",496,"MN-069","Bayanhongor","province",NULL)
            ,("MN","MNG",496,"MN-071","Bayan-Ölgiy","province",NULL)
            ,("MN","MNG",496,"MN-073","Arhangay","province",NULL)
            ,("MN","MNG",496,"MN-1","Ulaanbaatar","capital_city",NULL)
            ,("MO","MAC",446,"MO-??","Macao","special_administrative_region",NULL)
            ,("MP","MNP",580,"MP-??","Northern Mariana Islands","country",NULL)
            ,("MQ","MTQ",474,"MQ-??","Martinique","country",NULL)
            ,("MR","MRT",478,"MR-01","Hodh ech Chargui","region",NULL)
            ,("MR","MRT",478,"MR-02","Hodh el Gharbi","region",NULL)
            ,("MR","MRT",478,"MR-03","Assaba","region",NULL)
            ,("MR","MRT",478,"MR-04","Gorgol","region",NULL)
            ,("MR","MRT",478,"MR-05","Brakna","region",NULL)
            ,("MR","MRT",478,"MR-06","Trarza","region",NULL)
            ,("MR","MRT",478,"MR-07","Adrar","region",NULL)
            ,("MR","MRT",478,"MR-08","Dakhlet Nouâdhibou","region",NULL)
            ,("MR","MRT",478,"MR-09","Tagant","region",NULL)
            ,("MR","MRT",478,"MR-10","Guidimaka","region",NULL)
            ,("MR","MRT",478,"MR-11","Tiris Zemmour","region",NULL)
            ,("MR","MRT",478,"MR-12","Inchiri","region",NULL)
            ,("MR","MRT",478,"MR-13","Nuwākshūţ al Gharbīyah","region",NULL)
            ,("MR","MRT",478,"MR-14","Nuwākshūţ ash Shamālīyah","region",NULL)
            ,("MR","MRT",478,"MR-15","Nuwākshūţ al Janūbīyah","region",NULL)
            ,("MS","MSR",500,"MS-??","Montserrat","country",NULL)
            ,("MT","MLT",470,"MT-01","Attard","council",NULL)
            ,("MT","MLT",470,"MT-02","Balzan","council",NULL)
            ,("MT","MLT",470,"MT-03","Birgu","council",NULL)
            ,("MT","MLT",470,"MT-04","Birkirkara","council",NULL)
            ,("MT","MLT",470,"MT-05","Birżebbuġa","council",NULL)
            ,("MT","MLT",470,"MT-06","Bormla","council",NULL)
            ,("MT","MLT",470,"MT-07","Dingli","council",NULL)
            ,("MT","MLT",470,"MT-08","Fgura","council",NULL)
            ,("MT","MLT",470,"MT-09","Floriana","council",NULL)
            ,("MT","MLT",470,"MT-10","Fontana","council",NULL)
            ,("MT","MLT",470,"MT-11","Gudja","council",NULL)
            ,("MT","MLT",470,"MT-12","Gżira","council",NULL)
            ,("MT","MLT",470,"MT-13","Għajnsielem","council",NULL)
            ,("MT","MLT",470,"MT-14","Għarb","council",NULL)
            ,("MT","MLT",470,"MT-15","Għargħur","council",NULL)
            ,("MT","MLT",470,"MT-16","Għasri","council",NULL)
            ,("MT","MLT",470,"MT-17","Għaxaq","council",NULL)
            ,("MT","MLT",470,"MT-18","Ħamrun","council",NULL)
            ,("MT","MLT",470,"MT-19","Iklin","council",NULL)
            ,("MT","MLT",470,"MT-20","Isla","council",NULL)
            ,("MT","MLT",470,"MT-21","Kalkara","council",NULL)
            ,("MT","MLT",470,"MT-22","Kerċem","council",NULL)
            ,("MT","MLT",470,"MT-23","Kirkop","council",NULL)
            ,("MT","MLT",470,"MT-24","Lija","council",NULL)
            ,("MT","MLT",470,"MT-25","Luqa","council",NULL)
            ,("MT","MLT",470,"MT-26","Marsa","council",NULL)
            ,("MT","MLT",470,"MT-27","Marsaskala","council",NULL)
            ,("MT","MLT",470,"MT-28","Marsaxlokk","council",NULL)
            ,("MT","MLT",470,"MT-29","Mdina","council",NULL)
            ,("MT","MLT",470,"MT-30","Mellieħa","council",NULL)
            ,("MT","MLT",470,"MT-31","Mġarr","council",NULL)
            ,("MT","MLT",470,"MT-32","Mosta","council",NULL)
            ,("MT","MLT",470,"MT-33","Mqabba","council",NULL)
            ,("MT","MLT",470,"MT-34","Msida","council",NULL)
            ,("MT","MLT",470,"MT-35","Mtarfa","council",NULL)
            ,("MT","MLT",470,"MT-36","Munxar","council",NULL)
            ,("MT","MLT",470,"MT-37","Nadur","council",NULL)
            ,("MT","MLT",470,"MT-38","Naxxar","council",NULL)
            ,("MT","MLT",470,"MT-39","Paola","council",NULL)
            ,("MT","MLT",470,"MT-40","Pembroke","council",NULL)
            ,("MT","MLT",470,"MT-41","Pietà","council",NULL)
            ,("MT","MLT",470,"MT-42","Qala","council",NULL)
            ,("MT","MLT",470,"MT-43","Qormi","council",NULL)
            ,("MT","MLT",470,"MT-44","Qrendi","council",NULL)
            ,("MT","MLT",470,"MT-45","Rabat Gozo","council",NULL)
            ,("MT","MLT",470,"MT-46","Rabat Malta","council",NULL)
            ,("MT","MLT",470,"MT-47","Safi","council",NULL)
            ,("MT","MLT",470,"MT-48","Saint Julian's","council",NULL)
            ,("MT","MLT",470,"MT-49","Saint John","council",NULL)
            ,("MT","MLT",470,"MT-50","Saint Lawrence","council",NULL)
            ,("MT","MLT",470,"MT-51","Saint Paul's Bay","council",NULL)
            ,("MT","MLT",470,"MT-52","Sannat","council",NULL)
            ,("MT","MLT",470,"MT-53","Saint Lucia's","council",NULL)
            ,("MT","MLT",470,"MT-54","Santa Venera","council",NULL)
            ,("MT","MLT",470,"MT-55","Siġġiewi","council",NULL)
            ,("MT","MLT",470,"MT-56","Sliema","council",NULL)
            ,("MT","MLT",470,"MT-57","Swieqi","council",NULL)
            ,("MT","MLT",470,"MT-58","Ta' Xbiex","council",NULL)
            ,("MT","MLT",470,"MT-59","Tarxien","council",NULL)
            ,("MT","MLT",470,"MT-60","Valletta","council",NULL)
            ,("MT","MLT",470,"MT-61","Xagħra","council",NULL)
            ,("MT","MLT",470,"MT-62","Xewkija","council",NULL)
            ,("MT","MLT",470,"MT-63","Xgħajra","council",NULL)
            ,("MT","MLT",470,"MT-64","Żabbar","council",NULL)
            ,("MT","MLT",470,"MT-65","Żebbuġ Gozo","council",NULL)
            ,("MT","MLT",470,"MT-66","Żebbuġ Malta","council",NULL)
            ,("MT","MLT",470,"MT-67","Żejtun","council",NULL)
            ,("MT","MLT",470,"MT-68","Żurrieq","council",NULL)
            ,("MU","MUS",480,"MU-AG","Agalega Islands","dependency",NULL)
            ,("MU","MUS",480,"MU-BL","Black River","district",NULL)
            ,("MU","MUS",480,"MU-CC",
                "Cargados Carajos Shoals","dependency",NULL)
            ,("MU","MUS",480,"MU-FL","Flacq","district",NULL)
            ,("MU","MUS",480,"MU-GP","Grand Port","district",NULL)
            ,("MU","MUS",480,"MU-MO","Moka","district",NULL)
            ,("MU","MUS",480,"MU-PA","Pamplemousses","district",NULL)
            ,("MU","MUS",480,"MU-PL","Port Louis","district",NULL)
            ,("MU","MUS",480,"MU-PW","Plaines Wilhems","district",NULL)
            ,("MU","MUS",480,"MU-RO","Rodrigues Island","dependency",NULL)
            ,("MU","MUS",480,"MU-RR","Rivière du Rempart","district",NULL)
            ,("MU","MUS",480,"MU-SA","Savanne","district",NULL)
            ,("MV","MDV",462,"MV-00",
                "South Ari Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-01",
                "Addu City","city",NULL)
            ,("MV","MDV",462,"MV-02",
                "North Ari Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-03",
                "Faadhippolhu","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-04",
                "Felidhu Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-05",
                "Hahdhunmathi","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-07",
                "North Thiladhunmathi","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-08",
                "Kolhumadulu","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-12",
                "Mulaku Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-13",
                "North Maalhosmadulu","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-14",
                "North Nilandhe Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-17",
                "South Nilandhe Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-20",
                "South Maalhosmadulu","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-23",
                "South Thiladhunmathi","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-24",
                "North Miladhunmadulu","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-25",
                "South Miladhunmadulu","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-26",
                "Male Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-27",
                "North Huvadhu Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-28",
                "South Huvadhu Atoll","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-29","Fuvammulah","administrative_atoll",NULL)
            ,("MV","MDV",462,"MV-MLE","Male","city",NULL)
            ,("MW","MWI",454,"MW-BA","Balaka","district","MW-S")
            ,("MW","MWI",454,"MW-BL","Blantyre","district","MW-S")
            ,("MW","MWI",454,"MW-C","Central Region","region",NULL)
            ,("MW","MWI",454,"MW-CK","Chikwawa","district","MW-S")
            ,("MW","MWI",454,"MW-CR","Chiradzulu","district","MW-S")
            ,("MW","MWI",454,"MW-CT","Chitipa","district","MW-N")
            ,("MW","MWI",454,"MW-DE","Dedza","district","MW-C")
            ,("MW","MWI",454,"MW-DO","Dowa","district","MW-C")
            ,("MW","MWI",454,"MW-KR","Karonga","district","MW-N")
            ,("MW","MWI",454,"MW-KS","Kasungu","district","MW-C")
            ,("MW","MWI",454,"MW-LI","Lilongwe","district","MW-C")
            ,("MW","MWI",454,"MW-LK","Likoma","district","MW-N")
            ,("MW","MWI",454,"MW-MC","Mchinji","district","MW-C")
            ,("MW","MWI",454,"MW-MG","Mangochi","district","MW-S")
            ,("MW","MWI",454,"MW-MH","Machinga","district","MW-S")
            ,("MW","MWI",454,"MW-MU","Mulanje","district","MW-S")
            ,("MW","MWI",454,"MW-MW","Mwanza","district","MW-S")
            ,("MW","MWI",454,"MW-MZ","Mzimba","district","MW-N")
            ,("MW","MWI",454,"MW-N","Northern Region","region",NULL)
            ,("MW","MWI",454,"MW-NB","Nkhata Bay","district","MW-N")
            ,("MW","MWI",454,"MW-NE","Neno","district","MW-S")
            ,("MW","MWI",454,"MW-NI","Ntchisi","district","MW-C")
            ,("MW","MWI",454,"MW-NK","Nkhotakota","district","MW-C")
            ,("MW","MWI",454,"MW-NS","Nsanje","district","MW-S")
            ,("MW","MWI",454,"MW-NU","Ntcheu","district","MW-C")
            ,("MW","MWI",454,"MW-PH","Phalombe","district","MW-S")
            ,("MW","MWI",454,"MW-RU","Rumphi","district","MW-N")
            ,("MW","MWI",454,"MW-S","Southern Region","region",NULL)
            ,("MW","MWI",454,"MW-SA","Salima","district","MW-C")
            ,("MW","MWI",454,"MW-TH","Thyolo","district","MW-S")
            ,("MW","MWI",454,"MW-ZO","Zomba","district","MW-S")
            ,("MX","MEX",484,"MX-AGU","Aguascalientes","state",NULL)
            ,("MX","MEX",484,"MX-BCN","Baja California","state",NULL)
            ,("MX","MEX",484,"MX-BCS","Baja California Sur","state",NULL)
            ,("MX","MEX",484,"MX-CAM","Campeche","state",NULL)
            ,("MX","MEX",484,"MX-CHH","Chihuahua","state",NULL)
            ,("MX","MEX",484,"MX-CHP","Chiapas","state",NULL)
            ,("MX","MEX",484,"MX-CMX","Ciudad de México","federal_entity",NULL)
            ,("MX","MEX",484,"MX-COA","Coahuila de Zaragoza","state",NULL)
            ,("MX","MEX",484,"MX-COL","Colima","state",NULL)
            ,("MX","MEX",484,"MX-DUR","Durango","state",NULL)
            ,("MX","MEX",484,"MX-GRO","Guerrero","state",NULL)
            ,("MX","MEX",484,"MX-GUA","Guanajuato","state",NULL)
            ,("MX","MEX",484,"MX-HID","Hidalgo","state",NULL)
            ,("MX","MEX",484,"MX-JAL","Jalisco","state",NULL)
            ,("MX","MEX",484,"MX-MEX","México","state",NULL)
            ,("MX","MEX",484,"MX-MIC","Michoacán de Ocampo","state",NULL)
            ,("MX","MEX",484,"MX-MOR","Morelos","state",NULL)
            ,("MX","MEX",484,"MX-NAY","Nayarit","state",NULL)
            ,("MX","MEX",484,"MX-NLE","Nuevo León","state",NULL)
            ,("MX","MEX",484,"MX-OAX","Oaxaca","state",NULL)
            ,("MX","MEX",484,"MX-PUE","Puebla","state",NULL)
            ,("MX","MEX",484,"MX-QUE","Querétaro","state",NULL)
            ,("MX","MEX",484,"MX-ROO","Quintana Roo","state",NULL)
            ,("MX","MEX",484,"MX-SIN","Sinaloa","state",NULL)
            ,("MX","MEX",484,"MX-SLP","San Luis Potosí","state",NULL)
            ,("MX","MEX",484,"MX-SON","Sonora","state",NULL)
            ,("MX","MEX",484,"MX-TAB","Tabasco","state",NULL)
            ,("MX","MEX",484,"MX-TAM","Tamaulipas","state",NULL)
            ,("MX","MEX",484,"MX-TLA","Tlaxcala","state",NULL)
            ,("MX","MEX",484,"MX-VER",
                "Veracruz de Ignacio de la Llave","state",NULL)
            ,("MX","MEX",484,"MX-YUC","Yucatán","state",NULL)
            ,("MX","MEX",484,"MX-ZAC","Zacatecas","state",NULL)
            ,("MY","MYS",458,"MY-01","Johor","state",NULL)
            ,("MY","MYS",458,"MY-02","Kedah","state",NULL)
            ,("MY","MYS",458,"MY-03","Kelantan","state",NULL)
            ,("MY","MYS",458,"MY-04","Melaka","state",NULL)
            ,("MY","MYS",458,"MY-05","Negeri Sembilan","state",NULL)
            ,("MY","MYS",458,"MY-06","Pahang","state",NULL)
            ,("MY","MYS",458,"MY-07","Pulau Pinang","state",NULL)
            ,("MY","MYS",458,"MY-08","Perak","state",NULL)
            ,("MY","MYS",458,"MY-09","Perlis","state",NULL)
            ,("MY","MYS",458,"MY-10","Selangor","state",NULL)
            ,("MY","MYS",458,"MY-11","Terengganu","state",NULL)
            ,("MY","MYS",458,"MY-12","Sabah","state",NULL)
            ,("MY","MYS",458,"MY-13","Sarawak","state",NULL)
            ,("MY","MYS",458,"MY-14",
                "Wilayah Persekutuan Kuala Lumpur","federal_territory",NULL)
            ,("MY","MYS",458,"MY-15",
                "Wilayah Persekutuan Labuan","federal_territory",NULL)
            ,("MY","MYS",458,"MY-16",
                "Wilayah Persekutuan Putrajaya","federal_territory",NULL)
            ,("MZ","MOZ",508,"MZ-A","Niassa","province",NULL)
            ,("MZ","MOZ",508,"MZ-B","Manica","province",NULL)
            ,("MZ","MOZ",508,"MZ-G","Gaza","province",NULL)
            ,("MZ","MOZ",508,"MZ-I","Inhambane","province",NULL)
            ,("MZ","MOZ",508,"MZ-L","Maputo","province",NULL)
            ,("MZ","MOZ",508,"MZ-MPM","Maputo","city",NULL)
            ,("MZ","MOZ",508,"MZ-N","Nampula","province",NULL)
            ,("MZ","MOZ",508,"MZ-P","Cabo Delgado","province",NULL)
            ,("MZ","MOZ",508,"MZ-Q","Zambézia","province",NULL)
            ,("MZ","MOZ",508,"MZ-S","Sofala","province",NULL)
            ,("MZ","MOZ",508,"MZ-T","Tete","province",NULL)
            ,("NA","NAM",516,"NA-CA","Zambezi","region",NULL)
            ,("NA","NAM",516,"NA-ER","Erongo","region",NULL)
            ,("NA","NAM",516,"NA-HA","Hardap","region",NULL)
            ,("NA","NAM",516,"NA-KA","Karas","region",NULL)
            ,("NA","NAM",516,"NA-KE","Kavango East","region",NULL)
            ,("NA","NAM",516,"NA-KH","Khomas","region",NULL)
            ,("NA","NAM",516,"NA-KU","Kunene","region",NULL)
            ,("NA","NAM",516,"NA-KW","Kavango West","region",NULL)
            ,("NA","NAM",516,"NA-OD","Otjozondjupa","region",NULL)
            ,("NA","NAM",516,"NA-OH","Omaheke","region",NULL)
            ,("NA","NAM",516,"NA-ON","Oshana","region",NULL)
            ,("NA","NAM",516,"NA-OS","Omusati","region",NULL)
            ,("NA","NAM",516,"NA-OT","Oshikoto","region",NULL)
            ,("NA","NAM",516,"NA-OW","Ohangwena","region",NULL)
            ,("NC","NCL",540,"NC-??","New Caledonia","country",NULL)
            ,("NE","NER",562,"NE-1","Agadez","region",NULL)
            ,("NE","NER",562,"NE-2","Diffa","region",NULL)
            ,("NE","NER",562,"NE-3","Dosso","region",NULL)
            ,("NE","NER",562,"NE-4","Maradi","region",NULL)
            ,("NE","NER",562,"NE-5","Tahoua","region",NULL)
            ,("NE","NER",562,"NE-6","Tillabéri","region",NULL)
            ,("NE","NER",562,"NE-7","Zinder","region",NULL)
            ,("NE","NER",562,"NE-8","Niamey","urban_community",NULL)
            ,("NF","NFK",574,"NF-??","Norfolk Island","country",NULL)
            ,("NG","NGA",566,"NG-AB","Abia","state",NULL)
            ,("NG","NGA",566,"NG-AD","Adamawa","state",NULL)
            ,("NG","NGA",566,"NG-AK","Akwa Ibom","state",NULL)
            ,("NG","NGA",566,"NG-AN","Anambra","state",NULL)
            ,("NG","NGA",566,"NG-BA","Bauchi","state",NULL)
            ,("NG","NGA",566,"NG-BE","Benue","state",NULL)
            ,("NG","NGA",566,"NG-BO","Borno","state",NULL)
            ,("NG","NGA",566,"NG-BY","Bayelsa","state",NULL)
            ,("NG","NGA",566,"NG-CR","Cross River","state",NULL)
            ,("NG","NGA",566,"NG-DE","Delta","state",NULL)
            ,("NG","NGA",566,"NG-EB","Ebonyi","state",NULL)
            ,("NG","NGA",566,"NG-ED","Edo","state",NULL)
            ,("NG","NGA",566,"NG-EK","Ekiti","state",NULL)
            ,("NG","NGA",566,"NG-EN","Enugu","state",NULL)
            ,("NG","NGA",566,"NG-FC",
                "Abuja Federal Capital Territory","capital_territory",NULL)
            ,("NG","NGA",566,"NG-GO","Gombe","state",NULL)
            ,("NG","NGA",566,"NG-IM","Imo","state",NULL)
            ,("NG","NGA",566,"NG-JI","Jigawa","state",NULL)
            ,("NG","NGA",566,"NG-KD","Kaduna","state",NULL)
            ,("NG","NGA",566,"NG-KE","Kebbi","state",NULL)
            ,("NG","NGA",566,"NG-KN","Kano","state",NULL)
            ,("NG","NGA",566,"NG-KO","Kogi","state",NULL)
            ,("NG","NGA",566,"NG-KT","Katsina","state",NULL)
            ,("NG","NGA",566,"NG-KW","Kwara","state",NULL)
            ,("NG","NGA",566,"NG-LA","Lagos","state",NULL)
            ,("NG","NGA",566,"NG-NA","Nasarawa","state",NULL)
            ,("NG","NGA",566,"NG-NI","Niger","state",NULL)
            ,("NG","NGA",566,"NG-OG","Ogun","state",NULL)
            ,("NG","NGA",566,"NG-ON","Ondo","state",NULL)
            ,("NG","NGA",566,"NG-OS","Osun","state",NULL)
            ,("NG","NGA",566,"NG-OY","Oyo","state",NULL)
            ,("NG","NGA",566,"NG-PL","Plateau","state",NULL)
            ,("NG","NGA",566,"NG-RI","Rivers","state",NULL)
            ,("NG","NGA",566,"NG-SO","Sokoto","state",NULL)
            ,("NG","NGA",566,"NG-TA","Taraba","state",NULL)
            ,("NG","NGA",566,"NG-YO","Yobe","state",NULL)
            ,("NG","NGA",566,"NG-ZA","Zamfara","state",NULL)
            ,("NI","NIC",558,"NI-AN",
                "Costa Caribe Norte","autonomous_region",NULL)
            ,("NI","NIC",558,"NI-AS",
                "Costa Caribe Sur","autonomous_region",NULL)
            ,("NI","NIC",558,"NI-BO","Boaco","department",NULL)
            ,("NI","NIC",558,"NI-CA","Carazo","department",NULL)
            ,("NI","NIC",558,"NI-CI","Chinandega","department",NULL)
            ,("NI","NIC",558,"NI-CO","Chontales","department",NULL)
            ,("NI","NIC",558,"NI-ES","Estelí","department",NULL)
            ,("NI","NIC",558,"NI-GR","Granada","department",NULL)
            ,("NI","NIC",558,"NI-JI","Jinotega","department",NULL)
            ,("NI","NIC",558,"NI-LE","León","department",NULL)
            ,("NI","NIC",558,"NI-MD","Madriz","department",NULL)
            ,("NI","NIC",558,"NI-MN","Managua","department",NULL)
            ,("NI","NIC",558,"NI-MS","Masaya","department",NULL)
            ,("NI","NIC",558,"NI-MT","Matagalpa","department",NULL)
            ,("NI","NIC",558,"NI-NS","Nueva Segovia","department",NULL)
            ,("NI","NIC",558,"NI-RI","Rivas","department",NULL)
            ,("NI","NIC",558,"NI-SJ","Río San Juan","department",NULL)
            ,("NL","NLD",528,"NL-AW","Aruba","country",NULL)
            ,("NL","NLD",528,"NL-BQ1","Bonaire","special_municipality",NULL)
            ,("NL","NLD",528,"NL-BQ2","Saba","special_municipality",NULL)
            ,("NL","NLD",528,"NL-BQ3",
                "Sint Eustatius","special_municipality",NULL)
            ,("NL","NLD",528,"NL-CW","Curaçao","country",NULL)
            ,("NL","NLD",528,"NL-DR","Drenthe","province",NULL)
            ,("NL","NLD",528,"NL-FL","Flevoland","province",NULL)
            ,("NL","NLD",528,"NL-FR","Fryslân","province",NULL)
            ,("NL","NLD",528,"NL-GE","Gelderland","province",NULL)
            ,("NL","NLD",528,"NL-GR","Groningen","province",NULL)
            ,("NL","NLD",528,"NL-LI","Limburg","province",NULL)
            ,("NL","NLD",528,"NL-NB","Noord-Brabant","province",NULL)
            ,("NL","NLD",528,"NL-NH","Noord-Holland","province",NULL)
            ,("NL","NLD",528,"NL-OV","Overijssel","province",NULL)
            ,("NL","NLD",528,"NL-SX","Sint Maarten","country",NULL)
            ,("NL","NLD",528,"NL-UT","Utrecht","province",NULL)
            ,("NL","NLD",528,"NL-ZE","Zeeland","province",NULL)
            ,("NL","NLD",528,"NL-ZH","Zuid-Holland","province",NULL)
            ,("NO","NOR",578,"NO-03","Oslo","county",NULL)
            ,("NO","NOR",578,"NO-11","Rogaland","county",NULL)
            ,("NO","NOR",578,"NO-15","Møre og Romsdal","county",NULL)
            ,("NO","NOR",578,"NO-18","Nordland","county",NULL)
            ,("NO","NOR",578,"NO-21","Svalbard","arctic_region",NULL)
            ,("NO","NOR",578,"NO-22","Jan Mayen","arctic_region",NULL)
            ,("NO","NOR",578,"NO-30","Viken","county",NULL)
            ,("NO","NOR",578,"NO-34","Innlandet","county",NULL)
            ,("NO","NOR",578,"NO-38","Vestfold og Telemark","county",NULL)
            ,("NO","NOR",578,"NO-42","Agder","county",NULL)
            ,("NO","NOR",578,"NO-46","Vestland","county",NULL)
            ,("NO","NOR",578,"NO-50","Trøndelag","county",NULL)
            ,("NO","NOR",578,"NO-54","Troms og Finnmark","county",NULL)
            ,("NP","NPL",524,"NP-P1","Pradesh 1","province",NULL)
            ,("NP","NPL",524,"NP-P2","Madhesh","province",NULL)
            ,("NP","NPL",524,"NP-P3","Bāgmatī","province",NULL)
            ,("NP","NPL",524,"NP-P4","Gaṇḍakī","province",NULL)
            ,("NP","NPL",524,"NP-P5","Lumbinī","province",NULL)
            ,("NP","NPL",524,"NP-P6","Karṇālī","province",NULL)
            ,("NP","NPL",524,"NP-P7","Sudūrpashchim","province",NULL)
            ,("NR","NRU",520,"NR-01","Aiwo","district",NULL)
            ,("NR","NRU",520,"NR-02","Anabar","district",NULL)
            ,("NR","NRU",520,"NR-03","Anetan","district",NULL)
            ,("NR","NRU",520,"NR-04","Anibare","district",NULL)
            ,("NR","NRU",520,"NR-05","Baitsi","district",NULL)
            ,("NR","NRU",520,"NR-06","Boe","district",NULL)
            ,("NR","NRU",520,"NR-07","Buada","district",NULL)
            ,("NR","NRU",520,"NR-08","Denigomodu","district",NULL)
            ,("NR","NRU",520,"NR-09","Ewa","district",NULL)
            ,("NR","NRU",520,"NR-10","Ijuw","district",NULL)
            ,("NR","NRU",520,"NR-11","Meneng","district",NULL)
            ,("NR","NRU",520,"NR-12","Nibok","district",NULL)
            ,("NR","NRU",520,"NR-13","Uaboe","district",NULL)
            ,("NR","NRU",520,"NR-14","Yaren","district",NULL)
            ,("NU","NIU",570,"NU-??","Niue","country",NULL)
            ,("NZ","NZL",554,"NZ-AUK","Auckland","region",NULL)
            ,("NZ","NZL",554,"NZ-BOP","Bay of Plenty","region",NULL)
            ,("NZ","NZL",554,"NZ-CAN","Canterbury","region",NULL)
            ,("NZ","NZL",554,"NZ-CIT",
                "Chatham Islands Territory","special_island_authority",NULL)
            ,("NZ","NZL",554,"NZ-GIS","Gisborne","region",NULL)
            ,("NZ","NZL",554,"NZ-HKB","Hawke's Bay","region",NULL)
            ,("NZ","NZL",554,"NZ-MBH","Marlborough","region",NULL)
            ,("NZ","NZL",554,"NZ-MWT","Manawatū-Whanganui","region",NULL)
            ,("NZ","NZL",554,"NZ-NSN","Nelson","region",NULL)
            ,("NZ","NZL",554,"NZ-NTL","Northland","region",NULL)
            ,("NZ","NZL",554,"NZ-OTA","Otago","region",NULL)
            ,("NZ","NZL",554,"NZ-STL","Southland","region",NULL)
            ,("NZ","NZL",554,"NZ-TAS","Tasman","region",NULL)
            ,("NZ","NZL",554,"NZ-TKI","Taranaki","region",NULL)
            ,("NZ","NZL",554,"NZ-WGN","Greater Wellington","region",NULL)
            ,("NZ","NZL",554,"NZ-WKO","Waikato","region",NULL)
            ,("NZ","NZL",554,"NZ-WTC","West Coast","region",NULL)
            ,("OM","OMN",512,"OM-BJ","Janūb al Bāţinah","governorate",NULL)
            ,("OM","OMN",512,"OM-BS","Shamāl al Bāţinah","governorate",NULL)
            ,("OM","OMN",512,"OM-BU","Al Buraymī","governorate",NULL)
            ,("OM","OMN",512,"OM-DA","Ad Dākhilīyah","governorate",NULL)
            ,("OM","OMN",512,"OM-MA","Masqaţ","governorate",NULL)
            ,("OM","OMN",512,"OM-MU","Musandam","governorate",NULL)
            ,("OM","OMN",512,"OM-SJ","Janūb ash Sharqīyah","governorate",NULL)
            ,("OM","OMN",512,"OM-SS","Shamāl ash Sharqīyah","governorate",NULL)
            ,("OM","OMN",512,"OM-WU","Al Wusţá","governorate",NULL)
            ,("OM","OMN",512,"OM-ZA","Az̧ Z̧āhirah","governorate",NULL)
            ,("OM","OMN",512,"OM-ZU","Z̧ufār","governorate",NULL)
            ,("PA","PAN",591,"PA-1","Bocas del Toro","province",NULL)
            ,("PA","PAN",591,"PA-10","Panamá Oeste","province",NULL)
            ,("PA","PAN",591,"PA-2","Coclé","province",NULL)
            ,("PA","PAN",591,"PA-3","Colón","province",NULL)
            ,("PA","PAN",591,"PA-4","Chiriquí","province",NULL)
            ,("PA","PAN",591,"PA-5","Darién","province",NULL)
            ,("PA","PAN",591,"PA-6","Herrera","province",NULL)
            ,("PA","PAN",591,"PA-7","Los Santos","province",NULL)
            ,("PA","PAN",591,"PA-8","Panamá","province",NULL)
            ,("PA","PAN",591,"PA-9","Veraguas","province",NULL)
            ,("PA","PAN",591,"PA-EM","Emberá","indigenous_region",NULL)
            ,("PA","PAN",591,"PA-KY","Guna Yala","indigenous_region",NULL)
            ,("PA","PAN",591,"PA-NB","Ngäbe-Buglé","indigenous_region",NULL)
            ,("PA","PAN",591,"PA-NT","Naso Tjër Di","indigenous_region",NULL)
            ,("PE","PER",604,"PE-AMA","Amazonas","region",NULL)
            ,("PE","PER",604,"PE-ANC","Ancash","region",NULL)
            ,("PE","PER",604,"PE-APU","Apurímac","region",NULL)
            ,("PE","PER",604,"PE-ARE","Arequipa","region",NULL)
            ,("PE","PER",604,"PE-AYA","Ayacucho","region",NULL)
            ,("PE","PER",604,"PE-CAJ","Cajamarca","region",NULL)
            ,("PE","PER",604,"PE-CAL","El Callao","region",NULL)
            ,("PE","PER",604,"PE-CUS","Cusco","region",NULL)
            ,("PE","PER",604,"PE-HUC","Huánuco","region",NULL)
            ,("PE","PER",604,"PE-HUV","Huancavelica","region",NULL)
            ,("PE","PER",604,"PE-ICA","Ica","region",NULL)
            ,("PE","PER",604,"PE-JUN","Junín","region",NULL)
            ,("PE","PER",604,"PE-LAL","La Libertad","region",NULL)
            ,("PE","PER",604,"PE-LAM","Lambayeque","region",NULL)
            ,("PE","PER",604,"PE-LIM","Lima","region",NULL)
            ,("PE","PER",604,"PE-LMA",
                "Municipalidad Metropolitana de Lima","municipality",NULL)
            ,("PE","PER",604,"PE-LOR","Loreto","region",NULL)
            ,("PE","PER",604,"PE-MDD","Madre de Dios","region",NULL)
            ,("PE","PER",604,"PE-MOQ","Moquegua","region",NULL)
            ,("PE","PER",604,"PE-PAS","Pasco","region",NULL)
            ,("PE","PER",604,"PE-PIU","Piura","region",NULL)
            ,("PE","PER",604,"PE-PUN","Puno","region",NULL)
            ,("PE","PER",604,"PE-SAM","San Martín","region",NULL)
            ,("PE","PER",604,"PE-TAC","Tacna","region",NULL)
            ,("PE","PER",604,"PE-TUM","Tumbes","region",NULL)
            ,("PE","PER",604,"PE-UCA","Ucayali","region",NULL)
            ,("PF","PYF",258,"PF-??","French Polynesia","country",NULL)
            ,("PG","PNG",598,"PG-CPK","Simbu Province Chimbu","province",NULL)
            ,("PG","PNG",598,"PG-CPM",
                "Central Province Central","province",NULL)
            ,("PG","PNG",598,"PG-EBR",
                "East New Britain Province East New Britain","province",NULL)
            ,("PG","PNG",598,"PG-EHG",
                "Eastern Highlands Province Eastern Highlands","province",NULL)
            ,("PG","PNG",598,"PG-EPW","Enga Province Enga","province",NULL)
            ,("PG","PNG",598,"PG-ESW",
                "East Sepik Province East Sepik","province",NULL)
            ,("PG","PNG",598,"PG-GPK","Gulf Province Gulf","province",NULL)
            ,("PG","PNG",598,"PG-HLA","Hela Province Hela","province",NULL)
            ,("PG","PNG",598,"PG-JWK","Jiwaka Province Jiwaka","province",NULL)
            ,("PG","PNG",598,"PG-MBA",
                "Milne Bay Province Milne Bay","province",NULL)
            ,("PG","PNG",598,"PG-MPL","Morobe Province Morobe","province",NULL)
            ,("PG","PNG",598,"PG-MPM","Madang Province Madang","province",NULL)
            ,("PG","PNG",598,"PG-MRL","Manus Province Manus","province",NULL)
            ,("PG","PNG",598,"PG-NCD",
                "National Capital District","district",NULL)
            ,("PG","PNG",598,"PG-NIK",
                "New Ireland Province New Ireland","province",NULL)
            ,("PG","PNG",598,"PG-NPP",
                "Oro Province Northern","province",NULL)
            ,("PG","PNG",598,"PG-NSB",
                "Bougainville Bougainville","autonomous_region",NULL)
            ,("PG","PNG",598,"PG-SAN",
                "Sandaun Province West Sepik","province",NULL)
            ,("PG","PNG",598,"PG-SHM",
                "Southern Highlands Province Southern Highlands",
                "province",NULL)
            ,("PG","PNG",598,"PG-WBK",
                "West New Britain Province West New Britain","province",NULL)
            ,("PG","PNG",598,"PG-WHM",
                "Western Highlands Province Western Highlands","province",NULL)
            ,("PG","PNG",598,"PG-WPD",
                "Fly River Province Western","province",NULL)
            ,("PH","PHL",608,"PH-00","National Capital Region","region",NULL)
            ,("PH","PHL",608,"PH-01","Ilocos","region",NULL)
            ,("PH","PHL",608,"PH-02","Cagayan Valley","region",NULL)
            ,("PH","PHL",608,"PH-03","Central Luzon","region",NULL)
            ,("PH","PHL",608,"PH-05","Bicol","region",NULL)
            ,("PH","PHL",608,"PH-06","Western Visayas","region",NULL)
            ,("PH","PHL",608,"PH-07","Central Visayas","region",NULL)
            ,("PH","PHL",608,"PH-08","Eastern Visayas","region",NULL)
            ,("PH","PHL",608,"PH-09","Zamboanga Peninsula","region",NULL)
            ,("PH","PHL",608,"PH-10","Northern Mindanao","region",NULL)
            ,("PH","PHL",608,"PH-11","Davao","region",NULL)
            ,("PH","PHL",608,"PH-12","Soccsksargen","region",NULL)
            ,("PH","PHL",608,"PH-13","Caraga","region",NULL)
            ,("PH","PHL",608,"PH-14",
                "Autonomous Region in Muslim Mindanao","region",NULL)
            ,("PH","PHL",608,"PH-15",
                "Cordillera Administrative Region","region",NULL)
            ,("PH","PHL",608,"PH-40","Calabarzon","region",NULL)
            ,("PH","PHL",608,"PH-41","Mimaropa","region",NULL)
            ,("PH","PHL",608,"PH-ABR","Abra","province","PH-15")
            ,("PH","PHL",608,"PH-AGN","Agusan del Norte","province","PH-13")
            ,("PH","PHL",608,"PH-AGS","Agusan del Sur","province","PH-13")
            ,("PH","PHL",608,"PH-AKL","Aklan","province","PH-06")
            ,("PH","PHL",608,"PH-ALB","Albay","province","PH-05")
            ,("PH","PHL",608,"PH-ANT","Antique","province","PH-06")
            ,("PH","PHL",608,"PH-APA","Apayao","province","PH-15")
            ,("PH","PHL",608,"PH-AUR","Aurora","province","PH-03")
            ,("PH","PHL",608,"PH-BAN","Bataan","province","PH-03")
            ,("PH","PHL",608,"PH-BAS","Basilan","province","PH-09")
            ,("PH","PHL",608,"PH-BEN","Benguet","province","PH-15")
            ,("PH","PHL",608,"PH-BIL","Biliran","province","PH-08")
            ,("PH","PHL",608,"PH-BOH","Bohol","province","PH-07")
            ,("PH","PHL",608,"PH-BTG","Batangas","province","PH-40")
            ,("PH","PHL",608,"PH-BTN","Batanes","province","PH-02")
            ,("PH","PHL",608,"PH-BUK","Bukidnon","province","PH-10")
            ,("PH","PHL",608,"PH-BUL","Bulacan","province","PH-03")
            ,("PH","PHL",608,"PH-CAG","Cagayan","province","PH-02")
            ,("PH","PHL",608,"PH-CAM","Camiguin","province","PH-10")
            ,("PH","PHL",608,"PH-CAN","Camarines Norte","province","PH-05")
            ,("PH","PHL",608,"PH-CAP","Capiz","province","PH-06")
            ,("PH","PHL",608,"PH-CAS","Camarines Sur","province","PH-05")
            ,("PH","PHL",608,"PH-CAT","Catanduanes","province","PH-05")
            ,("PH","PHL",608,"PH-CAV","Cavite","province","PH-40")
            ,("PH","PHL",608,"PH-CEB","Cebu","province","PH-07")
            ,("PH","PHL",608,"PH-COM","Davao de Oro","province","PH-11")
            ,("PH","PHL",608,"PH-DAO","Davao Oriental","province","PH-11")
            ,("PH","PHL",608,"PH-DAS","Davao del Sur","province","PH-11")
            ,("PH","PHL",608,"PH-DAV","Davao del Norte","province","PH-11")
            ,("PH","PHL",608,"PH-DIN","Dinagat Islands","province","PH-13")
            ,("PH","PHL",608,"PH-DVO","Davao Occidental","province","PH-11")
            ,("PH","PHL",608,"PH-EAS","Eastern Samar","province","PH-08")
            ,("PH","PHL",608,"PH-GUI","Guimaras","province","PH-06")
            ,("PH","PHL",608,"PH-IFU","Ifugao","province","PH-15")
            ,("PH","PHL",608,"PH-ILI","Iloilo","province","PH-06")
            ,("PH","PHL",608,"PH-ILN","Ilocos Norte","province","PH-01")
            ,("PH","PHL",608,"PH-ILS","Ilocos Sur","province","PH-01")
            ,("PH","PHL",608,"PH-ISA","Isabela","province","PH-02")
            ,("PH","PHL",608,"PH-KAL","Kalinga","province","PH-15")
            ,("PH","PHL",608,"PH-LAG","Laguna","province","PH-40")
            ,("PH","PHL",608,"PH-LAN","Lanao del Norte","province","PH-12")
            ,("PH","PHL",608,"PH-LAS","Lanao del Sur","province","PH-14")
            ,("PH","PHL",608,"PH-LEY","Leyte","province","PH-08")
            ,("PH","PHL",608,"PH-LUN","La Union","province","PH-01")
            ,("PH","PHL",608,"PH-MAD","Marinduque","province","PH-41")
            ,("PH","PHL",608,"PH-MAG","Maguindanao","province","PH-14")
            ,("PH","PHL",608,"PH-MAS","Masbate","province","PH-05")
            ,("PH","PHL",608,"PH-MDC","Mindoro Occidental","province","PH-41")
            ,("PH","PHL",608,"PH-MDR","Mindoro Oriental","province","PH-41")
            ,("PH","PHL",608,"PH-MOU","Mountain Province","province","PH-15")
            ,("PH","PHL",608,"PH-MSC","Misamis Occidental","province","PH-10")
            ,("PH","PHL",608,"PH-MSR","Misamis Oriental","province","PH-10")
            ,("PH","PHL",608,"PH-NCO","Cotabato","province","PH-12")
            ,("PH","PHL",608,"PH-NEC","Negros Occidental","province","PH-06")
            ,("PH","PHL",608,"PH-NER","Negros Oriental","province","PH-07")
            ,("PH","PHL",608,"PH-NSA","Northern Samar","province","PH-08")
            ,("PH","PHL",608,"PH-NUE","Nueva Ecija","province","PH-03")
            ,("PH","PHL",608,"PH-NUV","Nueva Vizcaya","province","PH-02")
            ,("PH","PHL",608,"PH-PAM","Pampanga","province","PH-03")
            ,("PH","PHL",608,"PH-PAN","Pangasinan","province","PH-01")
            ,("PH","PHL",608,"PH-PLW","Palawan","province","PH-41")
            ,("PH","PHL",608,"PH-QUE","Quezon","province","PH-40")
            ,("PH","PHL",608,"PH-QUI","Quirino","province","PH-02")
            ,("PH","PHL",608,"PH-RIZ","Rizal","province","PH-40")
            ,("PH","PHL",608,"PH-ROM","Romblon","province","PH-41")
            ,("PH","PHL",608,"PH-SAR","Sarangani","province","PH-11")
            ,("PH","PHL",608,"PH-SCO","South Cotabato","province","PH-11")
            ,("PH","PHL",608,"PH-SIG","Siquijor","province","PH-07")
            ,("PH","PHL",608,"PH-SLE","Southern Leyte","province","PH-08")
            ,("PH","PHL",608,"PH-SLU","Sulu","province","PH-14")
            ,("PH","PHL",608,"PH-SOR","Sorsogon","province","PH-05")
            ,("PH","PHL",608,"PH-SUK","Sultan Kudarat","province","PH-12")
            ,("PH","PHL",608,"PH-SUN","Surigao del Norte","province","PH-13")
            ,("PH","PHL",608,"PH-SUR","Surigao del Sur","province","PH-13")
            ,("PH","PHL",608,"PH-TAR","Tarlac","province","PH-03")
            ,("PH","PHL",608,"PH-TAW","Tawi-Tawi","province","PH-14")
            ,("PH","PHL",608,"PH-WSA","Samar","province","PH-08")
            ,("PH","PHL",608,"PH-ZAN","Zamboanga del Norte","province","PH-09")
            ,("PH","PHL",608,"PH-ZAS","Zamboanga del Sur","province","PH-09")
            ,("PH","PHL",608,"PH-ZMB","Zambales","province","PH-03")
            ,("PH","PHL",608,"PH-ZSI","Zamboanga Sibugay","province","PH-09")
            ,("PK","PAK",586,"PK-BA","Balochistan","province",NULL)
            ,("PK","PAK",586,"PK-GB","Gilgit-Baltistan","pakistan_administered_area",NULL)
            ,("PK","PAK",586,"PK-IS","Islamabad","federal_capital_territory",NULL)
            ,("PK","PAK",586,"PK-JK",
                "Azad Jammu and Kashmir","pakistan_administered_area",NULL)
            ,("PK","PAK",586,"PK-KP","Khyber Pakhtunkhwa","province",NULL)
            ,("PK","PAK",586,"PK-PB","Punjab","province",NULL)
            ,("PK","PAK",586,"PK-SD","Sindh","province",NULL)
            ,("PL","POL",616,"PL-02","Dolnośląskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-04","Kujawsko-pomorskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-06","Lubelskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-08","Lubuskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-10","Łódzkie","voivodeship",NULL)
            ,("PL","POL",616,"PL-12","Małopolskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-14","Mazowieckie","voivodeship",NULL)
            ,("PL","POL",616,"PL-16","Opolskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-18","Podkarpackie","voivodeship",NULL)
            ,("PL","POL",616,"PL-20","Podlaskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-22","Pomorskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-24","Śląskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-26","Świętokrzyskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-28","Warmińsko-mazurskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-30","Wielkopolskie","voivodeship",NULL)
            ,("PL","POL",616,"PL-32","Zachodniopomorskie","voivodeship",NULL)
            ,("PM","SPM",666,"PM-??",
                "Saint Pierre and Miquelon","country",NULL)
            ,("PN","PCN",612,"PN-??","Pitcairn Islands","country",NULL)
            ,("PR","PRI",630,"PR-??","Puerto Rico","country",NULL)
            ,("PS","PSE",275,"PS-BTH","Bethlehem","governorate",NULL)
            ,("PS","PSE",275,"PS-DEB","Deir El Balah","governorate",NULL)
            ,("PS","PSE",275,"PS-GZA","Gaza","governorate",NULL)
            ,("PS","PSE",275,"PS-HBN","Hebron","governorate",NULL)
            ,("PS","PSE",275,"PS-JEM","Jerusalem","governorate",NULL)
            ,("PS","PSE",275,"PS-JEN","Jenin","governorate",NULL)
            ,("PS","PSE",275,"PS-JRH",
                "Jericho and Al Aghwar","governorate",NULL)
            ,("PS","PSE",275,"PS-KYS","Khan Yunis","governorate",NULL)
            ,("PS","PSE",275,"PS-NBS","Nablus","governorate",NULL)
            ,("PS","PSE",275,"PS-NGZ","North Gaza","governorate",NULL)
            ,("PS","PSE",275,"PS-QQA","Qalqilya","governorate",NULL)
            ,("PS","PSE",275,"PS-RBH","Ramallah","governorate",NULL)
            ,("PS","PSE",275,"PS-RFH","Rafah","governorate",NULL)
            ,("PS","PSE",275,"PS-SLT","Salfit","governorate",NULL)
            ,("PS","PSE",275,"PS-TBS","Tubas","governorate",NULL)
            ,("PS","PSE",275,"PS-TKM","Tulkarm","governorate",NULL)
            ,("PT","PRT",620,"PT-01","Aveiro","district",NULL)
            ,("PT","PRT",620,"PT-02","Beja","district",NULL)
            ,("PT","PRT",620,"PT-03","Braga","district",NULL)
            ,("PT","PRT",620,"PT-04","Bragança","district",NULL)
            ,("PT","PRT",620,"PT-05","Castelo Branco","district",NULL)
            ,("PT","PRT",620,"PT-06","Coimbra","district",NULL)
            ,("PT","PRT",620,"PT-07","Évora","district",NULL)
            ,("PT","PRT",620,"PT-08","Faro","district",NULL)
            ,("PT","PRT",620,"PT-09","Guarda","district",NULL)
            ,("PT","PRT",620,"PT-10","Leiria","district",NULL)
            ,("PT","PRT",620,"PT-11","Lisboa","district",NULL)
            ,("PT","PRT",620,"PT-12","Portalegre","district",NULL)
            ,("PT","PRT",620,"PT-13","Porto","district",NULL)
            ,("PT","PRT",620,"PT-14","Santarém","district",NULL)
            ,("PT","PRT",620,"PT-15","Setúbal","district",NULL)
            ,("PT","PRT",620,"PT-16","Viana do Castelo","district",NULL)
            ,("PT","PRT",620,"PT-17","Vila Real","district",NULL)
            ,("PT","PRT",620,"PT-18","Viseu","district",NULL)
            ,("PT","PRT",620,"PT-20",
                "Região Autónoma dos Açores","autonomous_region",NULL)
            ,("PT","PRT",620,"PT-30",
                "Região Autónoma da Madeira","autonomous_region",NULL)
            ,("PW","PLW",585,"PW-002","Aimeliik","state",NULL)
            ,("PW","PLW",585,"PW-004","Airai","state",NULL)
            ,("PW","PLW",585,"PW-010","Angaur","state",NULL)
            ,("PW","PLW",585,"PW-050","Hatohobei","state",NULL)
            ,("PW","PLW",585,"PW-100","Kayangel","state",NULL)
            ,("PW","PLW",585,"PW-150","Koror","state",NULL)
            ,("PW","PLW",585,"PW-212","Melekeok","state",NULL)
            ,("PW","PLW",585,"PW-214","Ngaraard","state",NULL)
            ,("PW","PLW",585,"PW-218","Ngarchelong","state",NULL)
            ,("PW","PLW",585,"PW-222","Ngardmau","state",NULL)
            ,("PW","PLW",585,"PW-224","Ngatpang","state",NULL)
            ,("PW","PLW",585,"PW-226","Ngchesar","state",NULL)
            ,("PW","PLW",585,"PW-227","Ngeremlengui","state",NULL)
            ,("PW","PLW",585,"PW-228","Ngiwal","state",NULL)
            ,("PW","PLW",585,"PW-350","Peleliu","state",NULL)
            ,("PW","PLW",585,"PW-370","Sonsorol","state",NULL)
            ,("PY","PRY",600,"PY-1",
                "Departamento de Concepción Concepción","department",NULL)
            ,("PY","PRY",600,"PY-10",
                "Departamento de Alto Paraná Alto Paraná","department",NULL)
            ,("PY","PRY",600,"PY-11",
                "Departamento Central Central","department",NULL)
            ,("PY","PRY",600,"PY-12",
                "Departamento de Ñeembucú Ñeembucú","department",NULL)
            ,("PY","PRY",600,"PY-13",
                "Departamento de Amambay Amambay","department",NULL)
            ,("PY","PRY",600,"PY-14",
                "Departamento de Canindeyú Canindeyú","department",NULL)
            ,("PY","PRY",600,"PY-15",
                "Departamento de Presidente Hayes Presidente Hayes",
                "department",NULL)
            ,("PY","PRY",600,"PY-16",
                "Departamento de Alto Paraguay Alto Paraguay",
                "department",NULL)
            ,("PY","PRY",600,"PY-19",
                "Departamento de Boquerón Boquerón","department",NULL)
            ,("PY","PRY",600,"PY-2",
                "Departamento de San Pedro San Pedro","department",NULL)
            ,("PY","PRY",600,"PY-3",
                "Departamento de Cordillera Cordillera","department",NULL)
            ,("PY","PRY",600,"PY-4",
                "Departamento de Guairá Guairá","department",NULL)
            ,("PY","PRY",600,"PY-5",
                "Departamento de Caaguazú Caaguazú","department",NULL)
            ,("PY","PRY",600,"PY-6",
                "Departamento de Caazapá Caazapá","department",NULL)
            ,("PY","PRY",600,"PY-7",
                "Departamento de Itapúa Itapúa","department",NULL)
            ,("PY","PRY",600,"PY-8",
                "Departamento de Misiones Misiones","department",NULL)
            ,("PY","PRY",600,"PY-9",
                "Departamento de Paraguarí Paraguarí","department",NULL)
            ,("PY","PRY",600,"PY-ASU","Asunción Asunción","capital",NULL)
            ,("QA","QAT",634,"QA-DA","Ad Dawḩah","municipality",NULL)
            ,("QA","QAT",634,"QA-KH",
                "Al Khawr wa adh Dhakhīrah","municipality",NULL)
            ,("QA","QAT",634,"QA-MS","Ash Shamāl","municipality",NULL)
            ,("QA","QAT",634,"QA-RA","Ar Rayyān","municipality",NULL)
            ,("QA","QAT",634,"QA-SH","Ash Shīḩānīyah","municipality",NULL)
            ,("QA","QAT",634,"QA-US","Umm Şalāl","municipality",NULL)
            ,("QA","QAT",634,"QA-WA","Al Wakrah","municipality",NULL)
            ,("QA","QAT",634,"QA-ZA","Az̧ Z̧a'āyin","municipality",NULL)
            ,("RE","REU",638,"RE-??","Réunion","country",NULL)
            ,("RO","ROU",642,"RO-AB","Alba","department",NULL)
            ,("RO","ROU",642,"RO-AG","Argeș","department",NULL)
            ,("RO","ROU",642,"RO-AR","Arad","department",NULL)
            ,("RO","ROU",642,"RO-B","București","municipality",NULL)
            ,("RO","ROU",642,"RO-BC","Bacău","department",NULL)
            ,("RO","ROU",642,"RO-BH","Bihor","department",NULL)
            ,("RO","ROU",642,"RO-BN","Bistrița-Năsăud","department",NULL)
            ,("RO","ROU",642,"RO-BR","Brăila","department",NULL)
            ,("RO","ROU",642,"RO-BT","Botoșani","department",NULL)
            ,("RO","ROU",642,"RO-BV","Brașov","department",NULL)
            ,("RO","ROU",642,"RO-BZ","Buzău","department",NULL)
            ,("RO","ROU",642,"RO-CJ","Cluj","department",NULL)
            ,("RO","ROU",642,"RO-CL","Călărași","department",NULL)
            ,("RO","ROU",642,"RO-CS","Caraș-Severin","department",NULL)
            ,("RO","ROU",642,"RO-CT","Constanța","department",NULL)
            ,("RO","ROU",642,"RO-CV","Covasna","department",NULL)
            ,("RO","ROU",642,"RO-DB","Dâmbovița","department",NULL)
            ,("RO","ROU",642,"RO-DJ","Dolj","department",NULL)
            ,("RO","ROU",642,"RO-GJ","Gorj","department",NULL)
            ,("RO","ROU",642,"RO-GL","Galați","department",NULL)
            ,("RO","ROU",642,"RO-GR","Giurgiu","department",NULL)
            ,("RO","ROU",642,"RO-HD","Hunedoara","department",NULL)
            ,("RO","ROU",642,"RO-HR","Harghita","department",NULL)
            ,("RO","ROU",642,"RO-IF","Ilfov","department",NULL)
            ,("RO","ROU",642,"RO-IL","Ialomița","department",NULL)
            ,("RO","ROU",642,"RO-IS","Iași","department",NULL)
            ,("RO","ROU",642,"RO-MH","Mehedinți","department",NULL)
            ,("RO","ROU",642,"RO-MM","Maramureș","department",NULL)
            ,("RO","ROU",642,"RO-MS","Mureș","department",NULL)
            ,("RO","ROU",642,"RO-NT","Neamț","department",NULL)
            ,("RO","ROU",642,"RO-OT","Olt","department",NULL)
            ,("RO","ROU",642,"RO-PH","Prahova","department",NULL)
            ,("RO","ROU",642,"RO-SB","Sibiu","department",NULL)
            ,("RO","ROU",642,"RO-SJ","Sălaj","department",NULL)
            ,("RO","ROU",642,"RO-SM","Satu Mare","department",NULL)
            ,("RO","ROU",642,"RO-SV","Suceava","department",NULL)
            ,("RO","ROU",642,"RO-TL","Tulcea","department",NULL)
            ,("RO","ROU",642,"RO-TM","Timiș","department",NULL)
            ,("RO","ROU",642,"RO-TR","Teleorman","department",NULL)
            ,("RO","ROU",642,"RO-VL","Vâlcea","department",NULL)
            ,("RO","ROU",642,"RO-VN","Vrancea","department",NULL)
            ,("RO","ROU",642,"RO-VS","Vaslui","department",NULL)
            ,("RS","SRB",688,"RS-00","Beograd","city",NULL)
            ,("RS","SRB",688,"RS-01","Severnobački okrug","district","RS-VO")
            ,("RS","SRB",688,"RS-02",
                "Srednjebanatski okrug","district","RS-VO")
            ,("RS","SRB",688,"RS-03",
                "Severnobanatski okrug","district","RS-VO")
            ,("RS","SRB",688,"RS-04",
                "Južnobanatski okrug","district","RS-VO")
            ,("RS","SRB",688,"RS-05","Zapadnobački okrug","district","RS-VO")
            ,("RS","SRB",688,"RS-06","Južnobački okrug","district","RS-VO")
            ,("RS","SRB",688,"RS-07","Sremski okrug","district","RS-VO")
            ,("RS","SRB",688,"RS-08","Mačvanski okrug","district",NULL)
            ,("RS","SRB",688,"RS-09","Kolubarski okrug","district",NULL)
            ,("RS","SRB",688,"RS-10","Podunavski okrug","district",NULL)
            ,("RS","SRB",688,"RS-11","Braničevski okrug","district",NULL)
            ,("RS","SRB",688,"RS-12","Šumadijski okrug","district",NULL)
            ,("RS","SRB",688,"RS-13","Pomoravski okrug","district",NULL)
            ,("RS","SRB",688,"RS-14","Borski okrug","district",NULL)
            ,("RS","SRB",688,"RS-15","Zaječarski okrug","district",NULL)
            ,("RS","SRB",688,"RS-16","Zlatiborski okrug","district",NULL)
            ,("RS","SRB",688,"RS-17","Moravički okrug","district",NULL)
            ,("RS","SRB",688,"RS-18","Raški okrug","district",NULL)
            ,("RS","SRB",688,"RS-19","Rasinski okrug","district",NULL)
            ,("RS","SRB",688,"RS-20","Nišavski okrug","district",NULL)
            ,("RS","SRB",688,"RS-21","Toplički okrug","district",NULL)
            ,("RS","SRB",688,"RS-22","Pirotski okrug","district",NULL)
            ,("RS","SRB",688,"RS-23","Jablanički okrug","district",NULL)
            ,("RS","SRB",688,"RS-24","Pčinjski okrug","district",NULL)
            ,("RS","SRB",688,"RS-25","Kosovski okrug","district","RS-KM")
            ,("RS","SRB",688,"RS-26","Pećki okrug","district","RS-KM")
            ,("RS","SRB",688,"RS-27","Prizrenski okrug","district","RS-KM")
            ,("RS","SRB",688,"RS-28",
                "Kosovsko-Mitrovački okrug","district","RS-KM")
            ,("RS","SRB",688,"RS-29",
                "Kosovsko-Pomoravski okrug","district","RS-KM")
            ,("RS","SRB",688,"RS-KM",
                "Kosovo-Metohija","autonomous_province",NULL)
            ,("RS","SRB",688,"RS-VO",
                "Vojvodina","autonomous_province",NULL)
            ,("RU","RUS",643,"RU-AD",
                "Adygeya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-AL",
                "Altay, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-ALT",
                "Altayskiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-AMU",
                "Amurskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-ARK",
                "Arkhangel'skaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-AST",
                "Astrakhanskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-BA",
                "Bashkortostan, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-BEL",
                "Belgorodskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-BRY",
                "Bryanskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-BU","Buryatiya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-CE","Chechenskaya Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-CHE",
                "Chelyabinskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-CHU",
                "Chukotskiy avtonomnyy okrug","autonomous_district",NULL)
            ,("RU","RUS",643,"RU-CU","Chuvashskaya Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-DA","Dagestan, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-IN","Ingushetiya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-IRK",
                "Irkutskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-IVA",
                "Ivanovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KAM",
                "Kamchatskiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-KB",
                "Kabardino-Balkarskaya Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-KC",
                "Karachayevo-Cherkesskaya Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-KDA",
                "Krasnodarskiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-KEM",
                "Kemerovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KGD",
                "Kaliningradskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KGN",
                "Kurganskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KHA",
                "Khabarovskiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-KHM",
                "Khanty-Mansiyskiy avtonomnyy okrug",
                "autonomous_district",NULL)
            ,("RU","RUS",643,"RU-KIR",
                "Kirovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KK","Khakasiya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-KL","Kalmykiya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-KLU",
                "Kaluzhskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KO","Komi, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-KOS",
                "Kostromskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KR","Kareliya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-KRS",
                "Kurskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-KYA",
                "Krasnoyarskiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-LEN",
                "Leningradskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-LIP",
                "Lipetskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-MAG",
                "Magadanskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-ME","Mariy El, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-MO","Mordoviya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-MOS",
                "Moskovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-MOW",
                "Moskva","autonomous_city",NULL)
            ,("RU","RUS",643,"RU-MUR",
                "Murmanskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-NEN",
                "Nenetskiy avtonomnyy okrug","autonomous_district",NULL)
            ,("RU","RUS",643,"RU-NGR",
                "Novgorodskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-NIZ",
                "Nizhegorodskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-NVS",
                "Novosibirskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-OMS",
                "Omskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-ORE",
                "Orenburgskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-ORL",
                "Orlovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-PER",
                "Permskiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-PNZ",
                "Penzenskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-PRI",
                "Primorskiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-PSK",
                "Pskovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-ROS",
                "Rostovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-RYA",
                "Ryazanskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-SA","Saha, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-SAK",
                "Sakhalinskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-SAM",
                "Samarskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-SAR",
                "Saratovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-SE",
                "Severnaya Osetiya, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-SMO",
                "Smolenskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-SPE",
                "Sankt-Peterburg","autonomous_city",NULL)
            ,("RU","RUS",643,"RU-STA",
                "Stavropol'skiy kray","administrative_territory",NULL)
            ,("RU","RUS",643,"RU-SVE",
                "Sverdlovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-TA","Tatarstan, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-TAM",
                "Tambovskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-TOM",
                "Tomskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-TUL",
                "Tul'skaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-TVE",
                "Tverskaya oblast","administrative_region",NULL)
            ,("RU","RUS",643,"RU-TY","Tyva, Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-TYU",
                "Tyumenskaya oblast'","administrative_region",NULL)
            ,("RU","RUS",643,"RU-UD","Udmurtskaya Respublika","republic",NULL)
            ,("RU","RUS",643,"RU-ULY",
                "Ul'yanovskaya oblast'","administrative_region",NULL)
            ,("RU","RUS",643,"RU-VGG",
                "Volgogradskaya oblast'","administrative_region",NULL)
            ,("RU","RUS",643,"RU-VLA",
                "Vladimirskaya oblast'","administrative_region",NULL)
            ,("RU","RUS",643,"RU-VLG",
                "Vologodskaya oblast'","administrative_region",NULL)
            ,("RU","RUS",643,"RU-VOR",
                "Voronezhskaya oblast'","administrative_region",NULL)
            ,("RU","RUS",643,"RU-YAN",
                "Yamalo-Nenetskiy avtonomnyy okrug","autonomous_district",NULL)
            ,("RU","RUS",643,"RU-YAR",
                "Yaroslavskaya oblast'","administrative_region",NULL)
            ,("RU","RUS",643,"RU-YEV",
                "Yevreyskaya avtonomnaya oblast'","autonomous_region",NULL)
            ,("RU","RUS",643,"RU-ZAB",
                "Zabaykal'skiy kray","administrative_territory",NULL)
            ,("RW","RWA",646,"RW-01","City of Kigali","city",NULL)
            ,("RW","RWA",646,"RW-02","Eastern","province",NULL)
            ,("RW","RWA",646,"RW-03","Northern","province",NULL)
            ,("RW","RWA",646,"RW-04","Western","province",NULL)
            ,("RW","RWA",646,"RW-05","Southern","province",NULL)
            ,("SA","SAU",682,"SA-01","Ar Riyāḑ","region",NULL)
            ,("SA","SAU",682,"SA-02","Makkah al Mukarramah","region",NULL)
            ,("SA","SAU",682,"SA-03","Al Madīnah al Munawwarah","region",NULL)
            ,("SA","SAU",682,"SA-04","Ash Sharqīyah","region",NULL)
            ,("SA","SAU",682,"SA-05","Al Qaşīm","region",NULL)
            ,("SA","SAU",682,"SA-06","Ḩā'il","region",NULL)
            ,("SA","SAU",682,"SA-07","Tabūk","region",NULL)
            ,("SA","SAU",682,"SA-08","Al Ḩudūd ash Shamālīyah","region",NULL)
            ,("SA","SAU",682,"SA-09","Jāzān","region",NULL)
            ,("SA","SAU",682,"SA-10","Najrān","region",NULL)
            ,("SA","SAU",682,"SA-11","Al Bāḩah","region",NULL)
            ,("SA","SAU",682,"SA-12","Al Jawf","region",NULL)
            ,("SA","SAU",682,"SA-14","'Asīr","region",NULL)
            ,("SB","SLB",90,"SB-CE","Central","province",NULL)
            ,("SB","SLB",90,"SB-CH","Choiseul","province",NULL)
            ,("SB","SLB",90,"SB-CT",
                "Capital Territory","capital_territory",NULL)
            ,("SB","SLB",90,"SB-GU","Guadalcanal","province",NULL)
            ,("SB","SLB",90,"SB-IS","Isabel","province",NULL)
            ,("SB","SLB",90,"SB-MK","Makira-Ulawa","province",NULL)
            ,("SB","SLB",90,"SB-ML","Malaita","province",NULL)
            ,("SB","SLB",90,"SB-RB","Rennell and Bellona","province",NULL)
            ,("SB","SLB",90,"SB-TE","Temotu","province",NULL)
            ,("SB","SLB",90,"SB-WE","Western","province",NULL)
            ,("SC","SYC",690,"SC-01","Anse aux Pins","district",NULL)
            ,("SC","SYC",690,"SC-02","Anse Boileau","district",NULL)
            ,("SC","SYC",690,"SC-03","Anse Etoile","district",NULL)
            ,("SC","SYC",690,"SC-04","Au Cap","district",NULL)
            ,("SC","SYC",690,"SC-05","Anse Royale","district",NULL)
            ,("SC","SYC",690,"SC-06","Baie Lazare","district",NULL)
            ,("SC","SYC",690,"SC-07","Baie Sainte Anne","district",NULL)
            ,("SC","SYC",690,"SC-08","Beau Vallon","district",NULL)
            ,("SC","SYC",690,"SC-09","Bel Air","district",NULL)
            ,("SC","SYC",690,"SC-10","Bel Ombre","district",NULL)
            ,("SC","SYC",690,"SC-11","Cascade","district",NULL)
            ,("SC","SYC",690,"SC-12","Glacis","district",NULL)
            ,("SC","SYC",690,"SC-13","Grand Anse Mahe","district",NULL)
            ,("SC","SYC",690,"SC-14","Grand Anse Praslin","district",NULL)
            ,("SC","SYC",690,"SC-15","La Digue","district",NULL)
            ,("SC","SYC",690,"SC-16","English River","district",NULL)
            ,("SC","SYC",690,"SC-17","Mont Buxton","district",NULL)
            ,("SC","SYC",690,"SC-18","Mont Fleuri","district",NULL)
            ,("SC","SYC",690,"SC-19","Plaisance","district",NULL)
            ,("SC","SYC",690,"SC-20","Pointe Larue","district",NULL)
            ,("SC","SYC",690,"SC-21","Port Glaud","district",NULL)
            ,("SC","SYC",690,"SC-22","Saint Louis","district",NULL)
            ,("SC","SYC",690,"SC-23","Takamaka","district",NULL)
            ,("SC","SYC",690,"SC-24","Les Mamelles","district",NULL)
            ,("SC","SYC",690,"SC-25","Roche Caiman","district",NULL)
            ,("SC","SYC",690,"SC-26","Ile Perseverance I","district",NULL)
            ,("SC","SYC",690,"SC-27","Ile Perseverance II","district",NULL)
            ,("SD","SDN",729,"SD-DC","Wasaţ Dārfūr","state",NULL)
            ,("SD","SDN",729,"SD-DE","Sharq Dārfūr","state",NULL)
            ,("SD","SDN",729,"SD-DN","Shamāl Dārfūr","state",NULL)
            ,("SD","SDN",729,"SD-DS","Janūb Dārfūr","state",NULL)
            ,("SD","SDN",729,"SD-DW","Gharb Dārfūr","state",NULL)
            ,("SD","SDN",729,"SD-GD","Al Qaḑārif","state",NULL)
            ,("SD","SDN",729,"SD-GK","Gharb Kurdufān","state",NULL)
            ,("SD","SDN",729,"SD-GZ","Al Jazīrah","state",NULL)
            ,("SD","SDN",729,"SD-KA","Kassalā","state",NULL)
            ,("SD","SDN",729,"SD-KH","Al Kharţūm","state",NULL)
            ,("SD","SDN",729,"SD-KN","Shamāl Kurdufān","state",NULL)
            ,("SD","SDN",729,"SD-KS","Janūb Kurdufān","state",NULL)
            ,("SD","SDN",729,"SD-NB","An Nīl al Azraq","state",NULL)
            ,("SD","SDN",729,"SD-NO","Ash Shamālīyah","state",NULL)
            ,("SD","SDN",729,"SD-NR","Nahr an Nīl","state",NULL)
            ,("SD","SDN",729,"SD-NW","An Nīl al Abyaḑ","state",NULL)
            ,("SD","SDN",729,"SD-RS","Al Baḩr al Aḩmar","state",NULL)
            ,("SD","SDN",729,"SD-SI","Sinnār","state",NULL)
            ,("SE","SWE",752,"SE-AB","Stockholms län","county",NULL)
            ,("SE","SWE",752,"SE-AC","Västerbottens län","county",NULL)
            ,("SE","SWE",752,"SE-BD","Norrbottens län","county",NULL)
            ,("SE","SWE",752,"SE-C","Uppsala län","county",NULL)
            ,("SE","SWE",752,"SE-D","Södermanlands län","county",NULL)
            ,("SE","SWE",752,"SE-E","Östergötlands län","county",NULL)
            ,("SE","SWE",752,"SE-F","Jönköpings län","county",NULL)
            ,("SE","SWE",752,"SE-G","Kronobergs län","county",NULL)
            ,("SE","SWE",752,"SE-H","Kalmar län","county",NULL)
            ,("SE","SWE",752,"SE-I","Gotlands län","county",NULL)
            ,("SE","SWE",752,"SE-K","Blekinge län","county",NULL)
            ,("SE","SWE",752,"SE-M","Skåne län","county",NULL)
            ,("SE","SWE",752,"SE-N","Hallands län","county",NULL)
            ,("SE","SWE",752,"SE-O","Västra Götalands län","county",NULL)
            ,("SE","SWE",752,"SE-S","Värmlands län","county",NULL)
            ,("SE","SWE",752,"SE-T","Örebro län","county",NULL)
            ,("SE","SWE",752,"SE-U","Västmanlands län","county",NULL)
            ,("SE","SWE",752,"SE-W","Dalarnas län","county",NULL)
            ,("SE","SWE",752,"SE-X","Gävleborgs län","county",NULL)
            ,("SE","SWE",752,"SE-Y","Västernorrlands län","county",NULL)
            ,("SE","SWE",752,"SE-Z","Jämtlands län","county",NULL)
            ,("SG","SGP",702,"SG-01","Central Singapore","district",NULL)
            ,("SG","SGP",702,"SG-02","North East","district",NULL)
            ,("SG","SGP",702,"SG-03","North West","district",NULL)
            ,("SG","SGP",702,"SG-04","South East","district",NULL)
            ,("SG","SGP",702,"SG-05","South West","district",NULL)
            ,("SH","SHN",654,"SH-AC","Ascension","territory",NULL)
            ,("SH","SHN",654,"SH-HL","Saint Helena","territory",NULL)
            ,("SH","SHN",654,"SH-TA","Tristan da Cunha","territory",NULL)
            ,("SI","SVN",705,"SI-001","Ajdovščina","municipality",NULL)
            ,("SI","SVN",705,"SI-002","Beltinci","municipality",NULL)
            ,("SI","SVN",705,"SI-003","Bled","municipality",NULL)
            ,("SI","SVN",705,"SI-004","Bohinj","municipality",NULL)
            ,("SI","SVN",705,"SI-005","Borovnica","municipality",NULL)
            ,("SI","SVN",705,"SI-006","Bovec","municipality",NULL)
            ,("SI","SVN",705,"SI-007","Brda","municipality",NULL)
            ,("SI","SVN",705,"SI-008","Brezovica","municipality",NULL)
            ,("SI","SVN",705,"SI-009","Brežice","municipality",NULL)
            ,("SI","SVN",705,"SI-010","Tišina","municipality",NULL)
            ,("SI","SVN",705,"SI-011","Celje","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-012",
                "Cerklje na Gorenjskem","municipality",NULL)
            ,("SI","SVN",705,"SI-013","Cerknica","municipality",NULL)
            ,("SI","SVN",705,"SI-014","Cerkno","municipality",NULL)
            ,("SI","SVN",705,"SI-015","Črenšovci","municipality",NULL)
            ,("SI","SVN",705,"SI-016","Črna na Koroškem","municipality",NULL)
            ,("SI","SVN",705,"SI-017","Črnomelj","municipality",NULL)
            ,("SI","SVN",705,"SI-018","Destrnik","municipality",NULL)
            ,("SI","SVN",705,"SI-019","Divača","municipality",NULL)
            ,("SI","SVN",705,"SI-020","Dobrepolje","municipality",NULL)
            ,("SI","SVN",705,"SI-021",
                "Dobrova-Polhov Gradec","municipality",NULL)
            ,("SI","SVN",705,"SI-022","Dol pri Ljubljani","municipality",NULL)
            ,("SI","SVN",705,"SI-023","Domžale","municipality",NULL)
            ,("SI","SVN",705,"SI-024","Dornava","municipality",NULL)
            ,("SI","SVN",705,"SI-025","Dravograd","municipality",NULL)
            ,("SI","SVN",705,"SI-026","Duplek","municipality",NULL)
            ,("SI","SVN",705,"SI-027",
                "Gorenja vas-Poljane","municipality",NULL)
            ,("SI","SVN",705,"SI-028","Gorišnica","municipality",NULL)
            ,("SI","SVN",705,"SI-029","Gornja Radgona","municipality",NULL)
            ,("SI","SVN",705,"SI-030","Gornji Grad","municipality",NULL)
            ,("SI","SVN",705,"SI-031","Gornji Petrovci","municipality",NULL)
            ,("SI","SVN",705,"SI-032","Grosuplje","municipality",NULL)
            ,("SI","SVN",705,"SI-033","Šalovci","municipality",NULL)
            ,("SI","SVN",705,"SI-034","Hrastnik","municipality",NULL)
            ,("SI","SVN",705,"SI-035","Hrpelje-Kozina","municipality",NULL)
            ,("SI","SVN",705,"SI-036","Idrija","municipality",NULL)
            ,("SI","SVN",705,"SI-037","Ig","municipality",NULL)
            ,("SI","SVN",705,"SI-038","Ilirska Bistrica","municipality",NULL)
            ,("SI","SVN",705,"SI-039","Ivančna Gorica","municipality",NULL)
            ,("SI","SVN",705,"SI-040","Izola","municipality",NULL)
            ,("SI","SVN",705,"SI-041","Jesenice","municipality",NULL)
            ,("SI","SVN",705,"SI-042","Juršinci","municipality",NULL)
            ,("SI","SVN",705,"SI-043","Kamnik","municipality",NULL)
            ,("SI","SVN",705,"SI-044","Kanal ob Soči","municipality",NULL)
            ,("SI","SVN",705,"SI-045","Kidričevo","municipality",NULL)
            ,("SI","SVN",705,"SI-046","Kobarid","municipality",NULL)
            ,("SI","SVN",705,"SI-047","Kobilje","municipality",NULL)
            ,("SI","SVN",705,"SI-048","Kočevje","municipality",NULL)
            ,("SI","SVN",705,"SI-049","Komen","municipality",NULL)
            ,("SI","SVN",705,"SI-050","Koper","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-051","Kozje","municipality",NULL)
            ,("SI","SVN",705,"SI-052","Kranj","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-053","Kranjska Gora","municipality",NULL)
            ,("SI","SVN",705,"SI-054","Krško","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-055","Kungota","municipality",NULL)
            ,("SI","SVN",705,"SI-056","Kuzma","municipality",NULL)
            ,("SI","SVN",705,"SI-057","Laško","municipality",NULL)
            ,("SI","SVN",705,"SI-058","Lenart","municipality",NULL)
            ,("SI","SVN",705,"SI-059","Lendava","municipality",NULL)
            ,("SI","SVN",705,"SI-060","Litija","municipality",NULL)
            ,("SI","SVN",705,"SI-061","Ljubljana","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-062","Ljubno","municipality",NULL)
            ,("SI","SVN",705,"SI-063","Ljutomer","municipality",NULL)
            ,("SI","SVN",705,"SI-064","Logatec","municipality",NULL)
            ,("SI","SVN",705,"SI-065","Loška dolina","municipality",NULL)
            ,("SI","SVN",705,"SI-066","Loški Potok","municipality",NULL)
            ,("SI","SVN",705,"SI-067","Luče","municipality",NULL)
            ,("SI","SVN",705,"SI-068","Lukovica","municipality",NULL)
            ,("SI","SVN",705,"SI-069","Majšperk","municipality",NULL)
            ,("SI","SVN",705,"SI-070","Maribor","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-071","Medvode","municipality",NULL)
            ,("SI","SVN",705,"SI-072","Mengeš","municipality",NULL)
            ,("SI","SVN",705,"SI-073","Metlika","municipality",NULL)
            ,("SI","SVN",705,"SI-074","Mežica","municipality",NULL)
            ,("SI","SVN",705,"SI-075","Miren-Kostanjevica","municipality",NULL)
            ,("SI","SVN",705,"SI-076","Mislinja","municipality",NULL)
            ,("SI","SVN",705,"SI-077","Moravče","municipality",NULL)
            ,("SI","SVN",705,"SI-078","Moravske Toplice","municipality",NULL)
            ,("SI","SVN",705,"SI-079","Mozirje","municipality",NULL)
            ,("SI","SVN",705,"SI-080",
                "Murska Sobota","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-081","Muta","municipality",NULL)
            ,("SI","SVN",705,"SI-082","Naklo","municipality",NULL)
            ,("SI","SVN",705,"SI-083","Nazarje","municipality",NULL)
            ,("SI","SVN",705,"SI-084","Nova Gorica","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-085","Novo Mesto","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-086","Odranci","municipality",NULL)
            ,("SI","SVN",705,"SI-087","Ormož","municipality",NULL)
            ,("SI","SVN",705,"SI-088","Osilnica","municipality",NULL)
            ,("SI","SVN",705,"SI-089","Pesnica","municipality",NULL)
            ,("SI","SVN",705,"SI-090","Piran","municipality",NULL)
            ,("SI","SVN",705,"SI-091","Pivka","municipality",NULL)
            ,("SI","SVN",705,"SI-092","Podčetrtek","municipality",NULL)
            ,("SI","SVN",705,"SI-093","Podvelka","municipality",NULL)
            ,("SI","SVN",705,"SI-094","Postojna","municipality",NULL)
            ,("SI","SVN",705,"SI-095","Preddvor","municipality",NULL)
            ,("SI","SVN",705,"SI-096","Ptuj","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-097","Puconci","municipality",NULL)
            ,("SI","SVN",705,"SI-098","Rače-Fram","municipality",NULL)
            ,("SI","SVN",705,"SI-099","Radeče","municipality",NULL)
            ,("SI","SVN",705,"SI-100","Radenci","municipality",NULL)
            ,("SI","SVN",705,"SI-101","Radlje ob Dravi","municipality",NULL)
            ,("SI","SVN",705,"SI-102","Radovljica","municipality",NULL)
            ,("SI","SVN",705,"SI-103","Ravne na Koroškem","municipality",NULL)
            ,("SI","SVN",705,"SI-104","Ribnica","municipality",NULL)
            ,("SI","SVN",705,"SI-105","Rogašovci","municipality",NULL)
            ,("SI","SVN",705,"SI-106","Rogaška Slatina","municipality",NULL)
            ,("SI","SVN",705,"SI-107","Rogatec","municipality",NULL)
            ,("SI","SVN",705,"SI-108","Ruše","municipality",NULL)
            ,("SI","SVN",705,"SI-109","Semič","municipality",NULL)
            ,("SI","SVN",705,"SI-110","Sevnica","municipality",NULL)
            ,("SI","SVN",705,"SI-111","Sežana","municipality",NULL)
            ,("SI","SVN",705,"SI-112",
                "Slovenj Gradec","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-113","Slovenska Bistrica","municipality",NULL)
            ,("SI","SVN",705,"SI-114","Slovenske Konjice","municipality",NULL)
            ,("SI","SVN",705,"SI-115","Starše","municipality",NULL)
            ,("SI","SVN",705,"SI-116",
                "Sveti Jurij ob Ščavnici","municipality",NULL)
            ,("SI","SVN",705,"SI-117","Šenčur","municipality",NULL)
            ,("SI","SVN",705,"SI-118","Šentilj","municipality",NULL)
            ,("SI","SVN",705,"SI-119","Šentjernej","municipality",NULL)
            ,("SI","SVN",705,"SI-120","Šentjur","municipality",NULL)
            ,("SI","SVN",705,"SI-121","Škocjan","municipality",NULL)
            ,("SI","SVN",705,"SI-122","Škofja Loka","municipality",NULL)
            ,("SI","SVN",705,"SI-123","Škofljica","municipality",NULL)
            ,("SI","SVN",705,"SI-124","Šmarje pri Jelšah","municipality",NULL)
            ,("SI","SVN",705,"SI-125","Šmartno ob Paki","municipality",NULL)
            ,("SI","SVN",705,"SI-126","Šoštanj","municipality",NULL)
            ,("SI","SVN",705,"SI-127","Štore","municipality",NULL)
            ,("SI","SVN",705,"SI-128","Tolmin","municipality",NULL)
            ,("SI","SVN",705,"SI-129","Trbovlje","municipality",NULL)
            ,("SI","SVN",705,"SI-130","Trebnje","municipality",NULL)
            ,("SI","SVN",705,"SI-131","Tržič","municipality",NULL)
            ,("SI","SVN",705,"SI-132","Turnišče","municipality",NULL)
            ,("SI","SVN",705,"SI-133","Velenje","urban_municipality",NULL)
            ,("SI","SVN",705,"SI-134","Velike Lašče","municipality",NULL)
            ,("SI","SVN",705,"SI-135","Videm","municipality",NULL)
            ,("SI","SVN",705,"SI-136","Vipava","municipality",NULL)
            ,("SI","SVN",705,"SI-137","Vitanje","municipality",NULL)
            ,("SI","SVN",705,"SI-138","Vodice","municipality",NULL)
            ,("SI","SVN",705,"SI-139","Vojnik","municipality",NULL)
            ,("SI","SVN",705,"SI-140","Vrhnika","municipality",NULL)
            ,("SI","SVN",705,"SI-141","Vuzenica","municipality",NULL)
            ,("SI","SVN",705,"SI-142","Zagorje ob Savi","municipality",NULL)
            ,("SI","SVN",705,"SI-143","Zavrč","municipality",NULL)
            ,("SI","SVN",705,"SI-144","Zreče","municipality",NULL)
            ,("SI","SVN",705,"SI-146","Železniki","municipality",NULL)
            ,("SI","SVN",705,"SI-147","Žiri","municipality",NULL)
            ,("SI","SVN",705,"SI-148","Benedikt","municipality",NULL)
            ,("SI","SVN",705,"SI-149","Bistrica ob Sotli","municipality",NULL)
            ,("SI","SVN",705,"SI-150","Bloke","municipality",NULL)
            ,("SI","SVN",705,"SI-151","Braslovče","municipality",NULL)
            ,("SI","SVN",705,"SI-152","Cankova","municipality",NULL)
            ,("SI","SVN",705,"SI-153","Cerkvenjak","municipality",NULL)
            ,("SI","SVN",705,"SI-154","Dobje","municipality",NULL)
            ,("SI","SVN",705,"SI-155","Dobrna","municipality",NULL)
            ,("SI","SVN",705,"SI-156","Dobrovnik","municipality",NULL)
            ,("SI","SVN",705,"SI-157","Dolenjske Toplice","municipality",NULL)
            ,("SI","SVN",705,"SI-158","Grad","municipality",NULL)
            ,("SI","SVN",705,"SI-159","Hajdina","municipality",NULL)
            ,("SI","SVN",705,"SI-160","Hoče-Slivnica","municipality",NULL)
            ,("SI","SVN",705,"SI-161","Hodoš","municipality",NULL)
            ,("SI","SVN",705,"SI-162","Horjul","municipality",NULL)
            ,("SI","SVN",705,"SI-163","Jezersko","municipality",NULL)
            ,("SI","SVN",705,"SI-164","Komenda","municipality",NULL)
            ,("SI","SVN",705,"SI-165","Kostel","municipality",NULL)
            ,("SI","SVN",705,"SI-166","Križevci","municipality",NULL)
            ,("SI","SVN",705,"SI-167","Lovrenc na Pohorju","municipality",NULL)
            ,("SI","SVN",705,"SI-168","Markovci","municipality",NULL)
            ,("SI","SVN",705,"SI-169",
                "Miklavž na Dravskem polju","municipality",NULL)
            ,("SI","SVN",705,"SI-170","Mirna Peč","municipality",NULL)
            ,("SI","SVN",705,"SI-171","Oplotnica","municipality",NULL)
            ,("SI","SVN",705,"SI-172","Podlehnik","municipality",NULL)
            ,("SI","SVN",705,"SI-173","Polzela","municipality",NULL)
            ,("SI","SVN",705,"SI-174","Prebold","municipality",NULL)
            ,("SI","SVN",705,"SI-175","Prevalje","municipality",NULL)
            ,("SI","SVN",705,"SI-176","Razkrižje","municipality",NULL)
            ,("SI","SVN",705,"SI-177","Ribnica na Pohorju","municipality",NULL)
            ,("SI","SVN",705,"SI-178","Selnica ob Dravi","municipality",NULL)
            ,("SI","SVN",705,"SI-179","Sodražica","municipality",NULL)
            ,("SI","SVN",705,"SI-180","Solčava","municipality",NULL)
            ,("SI","SVN",705,"SI-181","Sveta Ana","municipality",NULL)
            ,("SI","SVN",705,"SI-182",
                "Sveti Andraž v Slovenskih goricah","municipality",NULL)
            ,("SI","SVN",705,"SI-183","Šempeter-Vrtojba","municipality",NULL)
            ,("SI","SVN",705,"SI-184","Tabor","municipality",NULL)
            ,("SI","SVN",705,"SI-185","Trnovska Vas","municipality",NULL)
            ,("SI","SVN",705,"SI-186","Trzin","municipality",NULL)
            ,("SI","SVN",705,"SI-187","Velika Polana","municipality",NULL)
            ,("SI","SVN",705,"SI-188","Veržej","municipality",NULL)
            ,("SI","SVN",705,"SI-189","Vransko","municipality",NULL)
            ,("SI","SVN",705,"SI-190","Žalec","municipality",NULL)
            ,("SI","SVN",705,"SI-191","Žetale","municipality",NULL)
            ,("SI","SVN",705,"SI-192","Žirovnica","municipality",NULL)
            ,("SI","SVN",705,"SI-193","Žužemberk","municipality",NULL)
            ,("SI","SVN",705,"SI-194","Šmartno pri Litiji","municipality",NULL)
            ,("SI","SVN",705,"SI-195","Apače","municipality",NULL)
            ,("SI","SVN",705,"SI-196","Cirkulane","municipality",NULL)
            ,("SI","SVN",705,"SI-197",
                "Kostanjevica na Krki","municipality",NULL)
            ,("SI","SVN",705,"SI-198","Makole","municipality",NULL)
            ,("SI","SVN",705,"SI-199","Mokronog-Trebelno","municipality",NULL)
            ,("SI","SVN",705,"SI-200","Poljčane","municipality",NULL)
            ,("SI","SVN",705,"SI-201","Renče-Vogrsko","municipality",NULL)
            ,("SI","SVN",705,"SI-202","Središče ob Dravi","municipality",NULL)
            ,("SI","SVN",705,"SI-203","Straža","municipality",NULL)
            ,("SI","SVN",705,"SI-204",
                "Sveta Trojica v Slovenskih goricah","municipality",NULL)
            ,("SI","SVN",705,"SI-205","Sveti Tomaž","municipality",NULL)
            ,("SI","SVN",705,"SI-206","Šmarješke Toplice","municipality",NULL)
            ,("SI","SVN",705,"SI-207","Gorje","municipality",NULL)
            ,("SI","SVN",705,"SI-208","Log-Dragomer","municipality",NULL)
            ,("SI","SVN",705,"SI-209","Rečica ob Savinji","municipality",NULL)
            ,("SI","SVN",705,"SI-210",
                "Sveti Jurij v Slovenskih goricah","municipality",NULL)
            ,("SI","SVN",705,"SI-211","Šentrupert","municipality",NULL)
            ,("SI","SVN",705,"SI-212","Mirna","municipality",NULL)
            ,("SI","SVN",705,"SI-213","Ankaran","municipality",NULL)
            ,("SJ","SJM",744,"SJ-??","Svalbard and Jan Mayen","county",NULL)
            ,("SK","SVK",703,"SK-BC","Banskobystrický kraj","region",NULL)
            ,("SK","SVK",703,"SK-BL","Bratislavský kraj","region",NULL)
            ,("SK","SVK",703,"SK-KI","Košický kraj","region",NULL)
            ,("SK","SVK",703,"SK-NI","Nitriansky kraj","region",NULL)
            ,("SK","SVK",703,"SK-PV","Prešovský kraj","region",NULL)
            ,("SK","SVK",703,"SK-TA","Trnavský kraj","region",NULL)
            ,("SK","SVK",703,"SK-TC","Trenčiansky kraj","region",NULL)
            ,("SK","SVK",703,"SK-ZI","Žilinský kraj","region",NULL)
            ,("SL","SLE",694,"SL-E","Eastern","province",NULL)
            ,("SL","SLE",694,"SL-N","Northern","province",NULL)
            ,("SL","SLE",694,"SL-NW","North Western","province",NULL)
            ,("SL","SLE",694,"SL-S","Southern","province",NULL)
            ,("SL","SLE",694,"SL-W","Western Area","area",NULL)
            ,("SM","SMR",674,"SM-01","Acquaviva","municipality",NULL)
            ,("SM","SMR",674,"SM-02","Chiesanuova","municipality",NULL)
            ,("SM","SMR",674,"SM-03","Domagnano","municipality",NULL)
            ,("SM","SMR",674,"SM-04","Faetano","municipality",NULL)
            ,("SM","SMR",674,"SM-05","Fiorentino","municipality",NULL)
            ,("SM","SMR",674,"SM-06","Borgo Maggiore","municipality",NULL)
            ,("SM","SMR",674,"SM-07","Città di San Marino","municipality",NULL)
            ,("SM","SMR",674,"SM-08","Montegiardino","municipality",NULL)
            ,("SM","SMR",674,"SM-09","Serravalle","municipality",NULL)
            ,("SN","SEN",686,"SN-DB","Diourbel","region",NULL)
            ,("SN","SEN",686,"SN-DK","Dakar","region",NULL)
            ,("SN","SEN",686,"SN-FK","Fatick","region",NULL)
            ,("SN","SEN",686,"SN-KA","Kaffrine","region",NULL)
            ,("SN","SEN",686,"SN-KD","Kolda","region",NULL)
            ,("SN","SEN",686,"SN-KE","Kédougou","region",NULL)
            ,("SN","SEN",686,"SN-KL","Kaolack","region",NULL)
            ,("SN","SEN",686,"SN-LG","Louga","region",NULL)
            ,("SN","SEN",686,"SN-MT","Matam","region",NULL)
            ,("SN","SEN",686,"SN-SE","Sédhiou","region",NULL)
            ,("SN","SEN",686,"SN-SL","Saint-Louis","region",NULL)
            ,("SN","SEN",686,"SN-TC","Tambacounda","region",NULL)
            ,("SN","SEN",686,"SN-TH","Thiès","region",NULL)
            ,("SN","SEN",686,"SN-ZG","Ziguinchor","region",NULL)
            ,("SO","SOM",706,"SO-AW","Awdal","administrative_region",NULL)
            ,("SO","SOM",706,"SO-BK","Bakool","administrative_region",NULL)
            ,("SO","SOM",706,"SO-BN","Banaadir","administrative_region",NULL)
            ,("SO","SOM",706,"SO-BR","Bari","administrative_region",NULL)
            ,("SO","SOM",706,"SO-BY","Bay","administrative_region",NULL)
            ,("SO","SOM",706,"SO-GA","Galguduud","administrative_region",NULL)
            ,("SO","SOM",706,"SO-GE","Gedo","administrative_region",NULL)
            ,("SO","SOM",706,"SO-HI","Hiiraan","administrative_region",NULL)
            ,("SO","SOM",706,"SO-JD",
                "Jubbada Dhexe","administrative_region",NULL)
            ,("SO","SOM",706,"SO-JH",
                "Jubbada Hoose","administrative_region",NULL)
            ,("SO","SOM",706,"SO-MU","Mudug","administrative_region",NULL)
            ,("SO","SOM",706,"SO-NU","Nugaal","administrative_region",NULL)
            ,("SO","SOM",706,"SO-SA","Sanaag","administrative_region",NULL)
            ,("SO","SOM",706,"SO-SD",
                "Shabeellaha Dhexe","administrative_region",NULL)
            ,("SO","SOM",706,"SO-SH",
                "Shabeellaha Hoose","administrative_region",NULL)
            ,("SO","SOM",706,"SO-SO","Sool","administrative_region",NULL)
            ,("SO","SOM",706,"SO-TO","Togdheer","administrative_region",NULL)
            ,("SO","SOM",706,"SO-WO",
                "Woqooyi Galbeed","administrative_region",NULL)
            ,("SR","SUR",740,"SR-BR","Brokopondo","district",NULL)
            ,("SR","SUR",740,"SR-CM","Commewijne","district",NULL)
            ,("SR","SUR",740,"SR-CR","Coronie","district",NULL)
            ,("SR","SUR",740,"SR-MA","Marowijne","district",NULL)
            ,("SR","SUR",740,"SR-NI","Nickerie","district",NULL)
            ,("SR","SUR",740,"SR-PM","Paramaribo","district",NULL)
            ,("SR","SUR",740,"SR-PR","Para","district",NULL)
            ,("SR","SUR",740,"SR-SA","Saramacca","district",NULL)
            ,("SR","SUR",740,"SR-SI","Sipaliwini","district",NULL)
            ,("SR","SUR",740,"SR-WA","Wanica","district",NULL)
            ,("SS","SSD",728,"SS-BN","Northern Bahr el Ghazal","state",NULL)
            ,("SS","SSD",728,"SS-BW","Western Bahr el Ghazal","state",NULL)
            ,("SS","SSD",728,"SS-EC","Central Equatoria","state",NULL)
            ,("SS","SSD",728,"SS-EE","Eastern Equatoria","state",NULL)
            ,("SS","SSD",728,"SS-EW","Western Equatoria","state",NULL)
            ,("SS","SSD",728,"SS-JG","Jonglei","state",NULL)
            ,("SS","SSD",728,"SS-LK","Lakes","state",NULL)
            ,("SS","SSD",728,"SS-NU","Upper Nile","state",NULL)
            ,("SS","SSD",728,"SS-UY","Unity","state",NULL)
            ,("SS","SSD",728,"SS-WR","Warrap","state",NULL)
            ,("ST","STP",678,"ST-01","Água Grande","district",NULL)
            ,("ST","STP",678,"ST-02","Cantagalo","district",NULL)
            ,("ST","STP",678,"ST-03","Caué","district",NULL)
            ,("ST","STP",678,"ST-04","Lembá","district",NULL)
            ,("ST","STP",678,"ST-05","Lobata","district",NULL)
            ,("ST","STP",678,"ST-06","Mé-Zóchi","district",NULL)
            ,("ST","STP",678,"ST-P","Príncipe","autonomous_region",NULL)
            ,("SV","SLV",222,"SV-AH","Ahuachapán","department",NULL)
            ,("SV","SLV",222,"SV-CA","Cabañas","department",NULL)
            ,("SV","SLV",222,"SV-CH","Chalatenango","department",NULL)
            ,("SV","SLV",222,"SV-CU","Cuscatlán","department",NULL)
            ,("SV","SLV",222,"SV-LI","La Libertad","department",NULL)
            ,("SV","SLV",222,"SV-MO","Morazán","department",NULL)
            ,("SV","SLV",222,"SV-PA","La Paz","department",NULL)
            ,("SV","SLV",222,"SV-SA","Santa Ana","department",NULL)
            ,("SV","SLV",222,"SV-SM","San Miguel","department",NULL)
            ,("SV","SLV",222,"SV-SO","Sonsonate","department",NULL)
            ,("SV","SLV",222,"SV-SS","San Salvador","department",NULL)
            ,("SV","SLV",222,"SV-SV","San Vicente","department",NULL)
            ,("SV","SLV",222,"SV-UN","La Unión","department",NULL)
            ,("SV","SLV",222,"SV-US","Usulután","department",NULL)
            ,("SX","SXM",534,"SX-??","Sint Maarten","country",NULL)
            ,("SY","SYR",760,"SY-DI","Dimashq","province",NULL)
            ,("SY","SYR",760,"SY-DR","Dar'ā","province",NULL)
            ,("SY","SYR",760,"SY-DY","Dayr az Zawr","province",NULL)
            ,("SY","SYR",760,"SY-HA","Al Ḩasakah","province",NULL)
            ,("SY","SYR",760,"SY-HI","Ḩimş","province",NULL)
            ,("SY","SYR",760,"SY-HL","Ḩalab","province",NULL)
            ,("SY","SYR",760,"SY-HM","Ḩamāh","province",NULL)
            ,("SY","SYR",760,"SY-ID","Idlib","province",NULL)
            ,("SY","SYR",760,"SY-LA","Al Lādhiqīyah","province",NULL)
            ,("SY","SYR",760,"SY-QU","Al Qunayţirah","province",NULL)
            ,("SY","SYR",760,"SY-RA","Ar Raqqah","province",NULL)
            ,("SY","SYR",760,"SY-RD","Rīf Dimashq","province",NULL)
            ,("SY","SYR",760,"SY-SU","As Suwaydā'","province",NULL)
            ,("SY","SYR",760,"SY-TA","Ţarţūs","province",NULL)
            ,("SZ","SWZ",748,"SZ-HH","Hhohho","region",NULL)
            ,("SZ","SWZ",748,"SZ-LU","Lubombo","region",NULL)
            ,("SZ","SWZ",748,"SZ-MA","Manzini","region",NULL)
            ,("SZ","SWZ",748,"SZ-SH","Shiselweni","region",NULL)
            ,("TC","TCA",796,"TC-??","Turks and Caicos Islands","country",NULL)
            ,("TD","TCD",148,"TD-BA","Al Baţḩā'","province",NULL)
            ,("TD","TCD",148,"TD-BG","Baḩr al Ghazāl","province",NULL)
            ,("TD","TCD",148,"TD-BO","Būrkū","province",NULL)
            ,("TD","TCD",148,"TD-CB","Shārī Bāqirmī","province",NULL)
            ,("TD","TCD",148,"TD-EE","Inīdī ash Sharqī","province",NULL)
            ,("TD","TCD",148,"TD-EO","Inīdī al Gharbī","province",NULL)
            ,("TD","TCD",148,"TD-GR","Qīrā","province",NULL)
            ,("TD","TCD",148,"TD-HL","Ḩajjar Lamīs","province",NULL)
            ,("TD","TCD",148,"TD-KA","Kānim","province",NULL)
            ,("TD","TCD",148,"TD-LC","Al Buḩayrah","province",NULL)
            ,("TD","TCD",148,"TD-LO","Lūghūn al Gharbī","province",NULL)
            ,("TD","TCD",148,"TD-LR","Lūghūn ash Sharqī","province",NULL)
            ,("TD","TCD",148,"TD-MA","Māndūl","province",NULL)
            ,("TD","TCD",148,"TD-MC","Shārī al Awsaţ","province",NULL)
            ,("TD","TCD",148,"TD-ME","Māyū Kībbī ash Sharqī","province",NULL)
            ,("TD","TCD",148,"TD-MO","Māyū Kībbī al Gharbī","province",NULL)
            ,("TD","TCD",148,"TD-ND","Madīnat Injamīnā","province",NULL)
            ,("TD","TCD",148,"TD-OD","Waddāy","province",NULL)
            ,("TD","TCD",148,"TD-SA","Salāmāt","province",NULL)
            ,("TD","TCD",148,"TD-SI","Sīlā","province",NULL)
            ,("TD","TCD",148,"TD-TA","Tānjīlī","province",NULL)
            ,("TD","TCD",148,"TD-TI","Tibastī","province",NULL)
            ,("TD","TCD",148,"TD-WF","Wādī Fīrā'","province",NULL)
            ,("TF","ATF",260,"TF-??",
                "French Southern and Antarctic Lands","country",NULL)
            ,("TH","THA",764,"TH-10",
                "Krung Thep Maha Nakhon","metropolitan_administration",NULL)
            ,("TH","THA",764,"TH-11","Samut Prakan","province",NULL)
            ,("TH","THA",764,"TH-12","Nonthaburi","province",NULL)
            ,("TH","THA",764,"TH-13","Pathum Thani","province",NULL)
            ,("TH","THA",764,"TH-14",
                "Phra Nakhon Si Ayutthaya","province",NULL)
            ,("TH","THA",764,"TH-15","Ang Thong","province",NULL)
            ,("TH","THA",764,"TH-16","Lop Buri","province",NULL)
            ,("TH","THA",764,"TH-17","Sing Buri","province",NULL)
            ,("TH","THA",764,"TH-18","Chai Nat","province",NULL)
            ,("TH","THA",764,"TH-19","Saraburi","province",NULL)
            ,("TH","THA",764,"TH-20","Chon Buri","province",NULL)
            ,("TH","THA",764,"TH-21","Rayong","province",NULL)
            ,("TH","THA",764,"TH-22","Chanthaburi","province",NULL)
            ,("TH","THA",764,"TH-23","Trat","province",NULL)
            ,("TH","THA",764,"TH-24","Chachoengsao","province",NULL)
            ,("TH","THA",764,"TH-25","Prachin Buri","province",NULL)
            ,("TH","THA",764,"TH-26","Nakhon Nayok","province",NULL)
            ,("TH","THA",764,"TH-27","Sa Kaeo","province",NULL)
            ,("TH","THA",764,"TH-30","Nakhon Ratchasima","province",NULL)
            ,("TH","THA",764,"TH-31","Buri Ram","province",NULL)
            ,("TH","THA",764,"TH-32","Surin","province",NULL)
            ,("TH","THA",764,"TH-33","Si Sa Ket","province",NULL)
            ,("TH","THA",764,"TH-34","Ubon Ratchathani","province",NULL)
            ,("TH","THA",764,"TH-35","Yasothon","province",NULL)
            ,("TH","THA",764,"TH-36","Chaiyaphum","province",NULL)
            ,("TH","THA",764,"TH-37","Amnat Charoen","province",NULL)
            ,("TH","THA",764,"TH-38","Bueng Kan","province",NULL)
            ,("TH","THA",764,"TH-39","Nong Bua Lam Phu","province",NULL)
            ,("TH","THA",764,"TH-40","Khon Kaen","province",NULL)
            ,("TH","THA",764,"TH-41","Udon Thani","province",NULL)
            ,("TH","THA",764,"TH-42","Loei","province",NULL)
            ,("TH","THA",764,"TH-43","Nong Khai","province",NULL)
            ,("TH","THA",764,"TH-44","Maha Sarakham","province",NULL)
            ,("TH","THA",764,"TH-45","Roi Et","province",NULL)
            ,("TH","THA",764,"TH-46","Kalasin","province",NULL)
            ,("TH","THA",764,"TH-47","Sakon Nakhon","province",NULL)
            ,("TH","THA",764,"TH-48","Nakhon Phanom","province",NULL)
            ,("TH","THA",764,"TH-49","Mukdahan","province",NULL)
            ,("TH","THA",764,"TH-50","Chiang Mai","province",NULL)
            ,("TH","THA",764,"TH-51","Lamphun","province",NULL)
            ,("TH","THA",764,"TH-52","Lampang","province",NULL)
            ,("TH","THA",764,"TH-53","Uttaradit","province",NULL)
            ,("TH","THA",764,"TH-54","Phrae","province",NULL)
            ,("TH","THA",764,"TH-55","Nan","province",NULL)
            ,("TH","THA",764,"TH-56","Phayao","province",NULL)
            ,("TH","THA",764,"TH-57","Chiang Rai","province",NULL)
            ,("TH","THA",764,"TH-58","Mae Hong Son","province",NULL)
            ,("TH","THA",764,"TH-60","Nakhon Sawan","province",NULL)
            ,("TH","THA",764,"TH-61","Uthai Thani","province",NULL)
            ,("TH","THA",764,"TH-62","Kamphaeng Phet","province",NULL)
            ,("TH","THA",764,"TH-63","Tak","province",NULL)
            ,("TH","THA",764,"TH-64","Sukhothai","province",NULL)
            ,("TH","THA",764,"TH-65","Phitsanulok","province",NULL)
            ,("TH","THA",764,"TH-66","Phichit","province",NULL)
            ,("TH","THA",764,"TH-67","Phetchabun","province",NULL)
            ,("TH","THA",764,"TH-70","Ratchaburi","province",NULL)
            ,("TH","THA",764,"TH-71","Kanchanaburi","province",NULL)
            ,("TH","THA",764,"TH-72","Suphan Buri","province",NULL)
            ,("TH","THA",764,"TH-73","Nakhon Pathom","province",NULL)
            ,("TH","THA",764,"TH-74","Samut Sakhon","province",NULL)
            ,("TH","THA",764,"TH-75","Samut Songkhram","province",NULL)
            ,("TH","THA",764,"TH-76","Phetchaburi","province",NULL)
            ,("TH","THA",764,"TH-77","Prachuap Khiri Khan","province",NULL)
            ,("TH","THA",764,"TH-80","Nakhon Si Thammarat","province",NULL)
            ,("TH","THA",764,"TH-81","Krabi","province",NULL)
            ,("TH","THA",764,"TH-82","Phangnga","province",NULL)
            ,("TH","THA",764,"TH-83","Phuket","province",NULL)
            ,("TH","THA",764,"TH-84","Surat Thani","province",NULL)
            ,("TH","THA",764,"TH-85","Ranong","province",NULL)
            ,("TH","THA",764,"TH-86","Chumphon","province",NULL)
            ,("TH","THA",764,"TH-90","Songkhla","province",NULL)
            ,("TH","THA",764,"TH-91","Satun","province",NULL)
            ,("TH","THA",764,"TH-92","Trang","province",NULL)
            ,("TH","THA",764,"TH-93","Phatthalung","province",NULL)
            ,("TH","THA",764,"TH-94","Pattani","province",NULL)
            ,("TH","THA",764,"TH-95","Yala","province",NULL)
            ,("TH","THA",764,"TH-96","Narathiwat","province",NULL)
            ,("TH","THA",764,"TH-S","Phatthaya","special_administrative_city",NULL)
            ,("TJ","TJK",762,"TJ-DU","Dushanbe","capital_territory",NULL)
            ,("TJ","TJK",762,"TJ-GB",
                "Kŭhistoni Badakhshon","autonomous_region",NULL)
            ,("TJ","TJK",762,"TJ-KT","Khatlon","region",NULL)
            ,("TJ","TJK",762,"TJ-RA",
                "nohiyahoi tobei jumhurí",
                "district_under_republic_administration",NULL)
            ,("TJ","TJK",762,"TJ-SU","Sughd","region",NULL)
            ,("TK","TKL",772,"TK-??","Tokelau","country",NULL)
            ,("TL","TLS",626,"TL-AL","Aileu","municipality",NULL)
            ,("TL","TLS",626,"TL-AN","Ainaro","municipality",NULL)
            ,("TL","TLS",626,"TL-BA","Baucau","municipality",NULL)
            ,("TL","TLS",626,"TL-BO","Bobonaro","municipality",NULL)
            ,("TL","TLS",626,"TL-CO","Cova Lima","municipality",NULL)
            ,("TL","TLS",626,"TL-DI","Díli","municipality",NULL)
            ,("TL","TLS",626,"TL-ER","Ermera","municipality",NULL)
            ,("TL","TLS",626,"TL-LA","Lautém","municipality",NULL)
            ,("TL","TLS",626,"TL-LI","Liquiça","municipality",NULL)
            ,("TL","TLS",626,"TL-MF","Manufahi","municipality",NULL)
            ,("TL","TLS",626,"TL-MT","Manatuto","municipality",NULL)
            ,("TL","TLS",626,"TL-OE",
                "Oé-Cusse Ambeno","special_administrative_region",NULL)
            ,("TL","TLS",626,"TL-VI","Viqueque","municipality",NULL)
            ,("TM","TKM",795,"TM-A","Ahal","region",NULL)
            ,("TM","TKM",795,"TM-B","Balkan","region",NULL)
            ,("TM","TKM",795,"TM-D","Daşoguz","region",NULL)
            ,("TM","TKM",795,"TM-L","Lebap","region",NULL)
            ,("TM","TKM",795,"TM-M","Mary","region",NULL)
            ,("TM","TKM",795,"TM-S","Aşgabat","city",NULL)
            ,("TN","TUN",788,"TN-11","Tunis","governorate",NULL)
            ,("TN","TUN",788,"TN-12","L'Ariana","governorate",NULL)
            ,("TN","TUN",788,"TN-13","Ben Arous","governorate",NULL)
            ,("TN","TUN",788,"TN-14","La Manouba","governorate",NULL)
            ,("TN","TUN",788,"TN-21","Nabeul","governorate",NULL)
            ,("TN","TUN",788,"TN-22","Zaghouan","governorate",NULL)
            ,("TN","TUN",788,"TN-23","Bizerte","governorate",NULL)
            ,("TN","TUN",788,"TN-31","Béja","governorate",NULL)
            ,("TN","TUN",788,"TN-32","Jendouba","governorate",NULL)
            ,("TN","TUN",788,"TN-33","Le Kef","governorate",NULL)
            ,("TN","TUN",788,"TN-34","Siliana","governorate",NULL)
            ,("TN","TUN",788,"TN-41","Kairouan","governorate",NULL)
            ,("TN","TUN",788,"TN-42","Kasserine","governorate",NULL)
            ,("TN","TUN",788,"TN-43","Sidi Bouzid","governorate",NULL)
            ,("TN","TUN",788,"TN-51","Sousse","governorate",NULL)
            ,("TN","TUN",788,"TN-52","Monastir","governorate",NULL)
            ,("TN","TUN",788,"TN-53","Mahdia","governorate",NULL)
            ,("TN","TUN",788,"TN-61","Sfax","governorate",NULL)
            ,("TN","TUN",788,"TN-71","Gafsa","governorate",NULL)
            ,("TN","TUN",788,"TN-72","Tozeur","governorate",NULL)
            ,("TN","TUN",788,"TN-73","Kébili","governorate",NULL)
            ,("TN","TUN",788,"TN-81","Gabès","governorate",NULL)
            ,("TN","TUN",788,"TN-82","Médenine","governorate",NULL)
            ,("TN","TUN",788,"TN-83","Tataouine","governorate",NULL)
            ,("TO","TON",776,"TO-01","'Eua","division",NULL)
            ,("TO","TON",776,"TO-02","Ha'apai","division",NULL)
            ,("TO","TON",776,"TO-03","Niuas","division",NULL)
            ,("TO","TON",776,"TO-04","Tongatapu","division",NULL)
            ,("TO","TON",776,"TO-05","Vava'u","division",NULL)
            ,("TR","TUR",792,"TR-01","Adana","province",NULL)
            ,("TR","TUR",792,"TR-02","Adiyaman","province",NULL)
            ,("TR","TUR",792,"TR-03","Afyonkarahisar","province",NULL)
            ,("TR","TUR",792,"TR-04","Ağri","province",NULL)
            ,("TR","TUR",792,"TR-05","Amasya","province",NULL)
            ,("TR","TUR",792,"TR-06","Ankara","province",NULL)
            ,("TR","TUR",792,"TR-07","Antalya","province",NULL)
            ,("TR","TUR",792,"TR-08","Artvin","province",NULL)
            ,("TR","TUR",792,"TR-09","Aydin","province",NULL)
            ,("TR","TUR",792,"TR-10","Balikesir","province",NULL)
            ,("TR","TUR",792,"TR-11","Bilecik","province",NULL)
            ,("TR","TUR",792,"TR-12","Bingöl","province",NULL)
            ,("TR","TUR",792,"TR-13","Bitlis","province",NULL)
            ,("TR","TUR",792,"TR-14","Bolu","province",NULL)
            ,("TR","TUR",792,"TR-15","Burdur","province",NULL)
            ,("TR","TUR",792,"TR-16","Bursa","province",NULL)
            ,("TR","TUR",792,"TR-17","Çanakkale","province",NULL)
            ,("TR","TUR",792,"TR-18","Çankiri","province",NULL)
            ,("TR","TUR",792,"TR-19","Çorum","province",NULL)
            ,("TR","TUR",792,"TR-20","Denizli","province",NULL)
            ,("TR","TUR",792,"TR-21","Diyarbakir","province",NULL)
            ,("TR","TUR",792,"TR-22","Edirne","province",NULL)
            ,("TR","TUR",792,"TR-23","Elaziğ","province",NULL)
            ,("TR","TUR",792,"TR-24","Erzincan","province",NULL)
            ,("TR","TUR",792,"TR-25","Erzurum","province",NULL)
            ,("TR","TUR",792,"TR-26","Eskişehir","province",NULL)
            ,("TR","TUR",792,"TR-27","Gaziantep","province",NULL)
            ,("TR","TUR",792,"TR-28","Giresun","province",NULL)
            ,("TR","TUR",792,"TR-29","Gümüşhane","province",NULL)
            ,("TR","TUR",792,"TR-30","Hakkâri","province",NULL)
            ,("TR","TUR",792,"TR-31","Hatay","province",NULL)
            ,("TR","TUR",792,"TR-32","Isparta","province",NULL)
            ,("TR","TUR",792,"TR-33","Mersin","province",NULL)
            ,("TR","TUR",792,"TR-34","İstanbul","province",NULL)
            ,("TR","TUR",792,"TR-35","İzmir","province",NULL)
            ,("TR","TUR",792,"TR-36","Kars","province",NULL)
            ,("TR","TUR",792,"TR-37","Kastamonu","province",NULL)
            ,("TR","TUR",792,"TR-38","Kayseri","province",NULL)
            ,("TR","TUR",792,"TR-39","Kirklareli","province",NULL)
            ,("TR","TUR",792,"TR-40","Kirşehir","province",NULL)
            ,("TR","TUR",792,"TR-41","Kocaeli","province",NULL)
            ,("TR","TUR",792,"TR-42","Konya","province",NULL)
            ,("TR","TUR",792,"TR-43","Kütahya","province",NULL)
            ,("TR","TUR",792,"TR-44","Malatya","province",NULL)
            ,("TR","TUR",792,"TR-45","Manisa","province",NULL)
            ,("TR","TUR",792,"TR-46","Kahramanmaraş","province",NULL)
            ,("TR","TUR",792,"TR-47","Mardin","province",NULL)
            ,("TR","TUR",792,"TR-48","Muğla","province",NULL)
            ,("TR","TUR",792,"TR-49","Muş","province",NULL)
            ,("TR","TUR",792,"TR-50","Nevşehir","province",NULL)
            ,("TR","TUR",792,"TR-51","Niğde","province",NULL)
            ,("TR","TUR",792,"TR-52","Ordu","province",NULL)
            ,("TR","TUR",792,"TR-53","Rize","province",NULL)
            ,("TR","TUR",792,"TR-54","Sakarya","province",NULL)
            ,("TR","TUR",792,"TR-55","Samsun","province",NULL)
            ,("TR","TUR",792,"TR-56","Siirt","province",NULL)
            ,("TR","TUR",792,"TR-57","Sinop","province",NULL)
            ,("TR","TUR",792,"TR-58","Sivas","province",NULL)
            ,("TR","TUR",792,"TR-59","Tekirdağ","province",NULL)
            ,("TR","TUR",792,"TR-60","Tokat","province",NULL)
            ,("TR","TUR",792,"TR-61","Trabzon","province",NULL)
            ,("TR","TUR",792,"TR-62","Tunceli","province",NULL)
            ,("TR","TUR",792,"TR-63","Şanliurfa","province",NULL)
            ,("TR","TUR",792,"TR-64","Uşak","province",NULL)
            ,("TR","TUR",792,"TR-65","Van","province",NULL)
            ,("TR","TUR",792,"TR-66","Yozgat","province",NULL)
            ,("TR","TUR",792,"TR-67","Zonguldak","province",NULL)
            ,("TR","TUR",792,"TR-68","Aksaray","province",NULL)
            ,("TR","TUR",792,"TR-69","Bayburt","province",NULL)
            ,("TR","TUR",792,"TR-70","Karaman","province",NULL)
            ,("TR","TUR",792,"TR-71","Kirikkale","province",NULL)
            ,("TR","TUR",792,"TR-72","Batman","province",NULL)
            ,("TR","TUR",792,"TR-73","Şirnak","province",NULL)
            ,("TR","TUR",792,"TR-74","Bartin","province",NULL)
            ,("TR","TUR",792,"TR-75","Ardahan","province",NULL)
            ,("TR","TUR",792,"TR-76","Iğdir","province",NULL)
            ,("TR","TUR",792,"TR-77","Yalova","province",NULL)
            ,("TR","TUR",792,"TR-78","Karabük","province",NULL)
            ,("TR","TUR",792,"TR-79","Kilis","province",NULL)
            ,("TR","TUR",792,"TR-80","Osmaniye","province",NULL)
            ,("TR","TUR",792,"TR-81","Düzce","province",NULL)
            ,("TT","TTO",780,"TT-ARI","Arima","borough",NULL)
            ,("TT","TTO",780,"TT-CHA","Chaguanas","borough",NULL)
            ,("TT","TTO",780,"TT-CTT","Couva-Tabaquite-Talparo","region",NULL)
            ,("TT","TTO",780,"TT-DMN","Diego Martin","region",NULL)
            ,("TT","TTO",780,"TT-MRC","Mayaro-Rio Claro","region",NULL)
            ,("TT","TTO",780,"TT-PED","Penal-Debe","region",NULL)
            ,("TT","TTO",780,"TT-POS","Port of Spain","city",NULL)
            ,("TT","TTO",780,"TT-PRT","Princes Town","region",NULL)
            ,("TT","TTO",780,"TT-PTF","Point Fortin","borough",NULL)
            ,("TT","TTO",780,"TT-SFO","San Fernando","city",NULL)
            ,("TT","TTO",780,"TT-SGE","Sangre Grande","region",NULL)
            ,("TT","TTO",780,"TT-SIP","Siparia","region",NULL)
            ,("TT","TTO",780,"TT-SJL","San Juan-Laventille","region",NULL)
            ,("TT","TTO",780,"TT-TOB","Tobago","ward",NULL)
            ,("TT","TTO",780,"TT-TUP","Tunapuna-Piarco","region",NULL)
            ,("TV","TUV",798,"TV-FUN","Funafuti","town_council",NULL)
            ,("TV","TUV",798,"TV-NIT","Niutao","island_council",NULL)
            ,("TV","TUV",798,"TV-NKF","Nukufetau","island_council",NULL)
            ,("TV","TUV",798,"TV-NKL","Nukulaelae","island_council",NULL)
            ,("TV","TUV",798,"TV-NMA","Nanumea","island_council",NULL)
            ,("TV","TUV",798,"TV-NMG","Nanumaga","island_council",NULL)
            ,("TV","TUV",798,"TV-NUI","Nui","island_council",NULL)
            ,("TV","TUV",798,"TV-VAI","Vaitupu","island_council",NULL)
            ,("TW","TWN",158,"TW-CHA","Changhua","county",NULL)
            ,("TW","TWN",158,"TW-CYI","Chiayi","city",NULL)
            ,("TW","TWN",158,"TW-CYQ","Chiayi","county",NULL)
            ,("TW","TWN",158,"TW-HSQ","Hsinchu","county",NULL)
            ,("TW","TWN",158,"TW-HSZ","Hsinchu","city",NULL)
            ,("TW","TWN",158,"TW-HUA","Hualien","county",NULL)
            ,("TW","TWN",158,"TW-ILA","Yilan","county",NULL)
            ,("TW","TWN",158,"TW-KEE","Keelung","city",NULL)
            ,("TW","TWN",158,"TW-KHH","Kaohsiung","special_municipality",NULL)
            ,("TW","TWN",158,"TW-KIN","Kinmen","county",NULL)
            ,("TW","TWN",158,"TW-LIE","Lienchiang","county",NULL)
            ,("TW","TWN",158,"TW-MIA","Miaoli","county",NULL)
            ,("TW","TWN",158,"TW-NAN","Nantou","county",NULL)
            ,("TW","TWN",158,"TW-NWT","New Taipei","special_municipality",NULL)
            ,("TW","TWN",158,"TW-PEN","Penghu","county",NULL)
            ,("TW","TWN",158,"TW-PIF","Pingtung","county",NULL)
            ,("TW","TWN",158,"TW-TAO","Taoyuan","special_municipality",NULL)
            ,("TW","TWN",158,"TW-TNN","Tainan","special_municipality",NULL)
            ,("TW","TWN",158,"TW-TPE","Taipei","special_municipality",NULL)
            ,("TW","TWN",158,"TW-TTT","Taitung","county",NULL)
            ,("TW","TWN",158,"TW-TXG","Taichung","special_municipality",NULL)
            ,("TW","TWN",158,"TW-YUN","Yunlin","county",NULL)
            ,("TZ","TZA",834,"TZ-01","Arusha","region",NULL)
            ,("TZ","TZA",834,"TZ-02","Dar es Salaam","region",NULL)
            ,("TZ","TZA",834,"TZ-03","Dodoma","region",NULL)
            ,("TZ","TZA",834,"TZ-04","Iringa","region",NULL)
            ,("TZ","TZA",834,"TZ-05","Kagera","region",NULL)
            ,("TZ","TZA",834,"TZ-06","Kaskazini Pemba","region",NULL)
            ,("TZ","TZA",834,"TZ-07","Kaskazini Unguja","region",NULL)
            ,("TZ","TZA",834,"TZ-08","Kigoma","region",NULL)
            ,("TZ","TZA",834,"TZ-09","Kilimanjaro","region",NULL)
            ,("TZ","TZA",834,"TZ-10","Kusini Pemba","region",NULL)
            ,("TZ","TZA",834,"TZ-11","Kusini Unguja","region",NULL)
            ,("TZ","TZA",834,"TZ-12","Lindi","region",NULL)
            ,("TZ","TZA",834,"TZ-13","Mara","region",NULL)
            ,("TZ","TZA",834,"TZ-14","Mbeya","region",NULL)
            ,("TZ","TZA",834,"TZ-15","Mjini Magharibi","region",NULL)
            ,("TZ","TZA",834,"TZ-16","Morogoro","region",NULL)
            ,("TZ","TZA",834,"TZ-17","Mtwara","region",NULL)
            ,("TZ","TZA",834,"TZ-18","Mwanza","region",NULL)
            ,("TZ","TZA",834,"TZ-19","Pwani","region",NULL)
            ,("TZ","TZA",834,"TZ-20","Rukwa","region",NULL)
            ,("TZ","TZA",834,"TZ-21","Ruvuma","region",NULL)
            ,("TZ","TZA",834,"TZ-22","Shinyanga","region",NULL)
            ,("TZ","TZA",834,"TZ-23","Singida","region",NULL)
            ,("TZ","TZA",834,"TZ-24","Tabora","region",NULL)
            ,("TZ","TZA",834,"TZ-25","Tanga","region",NULL)
            ,("TZ","TZA",834,"TZ-26","Manyara","region",NULL)
            ,("TZ","TZA",834,"TZ-27","Geita","region",NULL)
            ,("TZ","TZA",834,"TZ-28","Katavi","region",NULL)
            ,("TZ","TZA",834,"TZ-29","Njombe","region",NULL)
            ,("TZ","TZA",834,"TZ-30","Simiyu","region",NULL)
            ,("TZ","TZA",834,"TZ-31","Songwe","region",NULL)
            ,("UA","UKR",804,"UA-05","Vinnytska oblast","region",NULL)
            ,("UA","UKR",804,"UA-07","Volynska oblast","region",NULL)
            ,("UA","UKR",804,"UA-09","Luhanska oblast","region",NULL)
            ,("UA","UKR",804,"UA-12","Dnipropetrovska oblast","region",NULL)
            ,("UA","UKR",804,"UA-14","Donetska oblast","region",NULL)
            ,("UA","UKR",804,"UA-18","Zhytomyrska oblast","region",NULL)
            ,("UA","UKR",804,"UA-21","Zakarpatska oblast","region",NULL)
            ,("UA","UKR",804,"UA-23","Zaporizka oblast","region",NULL)
            ,("UA","UKR",804,"UA-26","Ivano-Frankivska oblast","region",NULL)
            ,("UA","UKR",804,"UA-30","Kyiv","city",NULL)
            ,("UA","UKR",804,"UA-32","Kyivska oblast","region",NULL)
            ,("UA","UKR",804,"UA-35","Kirovohradska oblast","region",NULL)
            ,("UA","UKR",804,"UA-40","Sevastopol","city",NULL)
            ,("UA","UKR",804,"UA-43",
                "Avtonomna Respublika Krym","republic",NULL)
            ,("UA","UKR",804,"UA-46","Lvivska oblast","region",NULL)
            ,("UA","UKR",804,"UA-48","Mykolaivska oblast","region",NULL)
            ,("UA","UKR",804,"UA-51","Odeska oblast","region",NULL)
            ,("UA","UKR",804,"UA-53","Poltavska oblast","region",NULL)
            ,("UA","UKR",804,"UA-56","Rivnenska oblast","region",NULL)
            ,("UA","UKR",804,"UA-59","Sumska oblast","region",NULL)
            ,("UA","UKR",804,"UA-61","Ternopilska oblast","region",NULL)
            ,("UA","UKR",804,"UA-63","Kharkivska oblast","region",NULL)
            ,("UA","UKR",804,"UA-65","Khersonska oblast","region",NULL)
            ,("UA","UKR",804,"UA-68","Khmelnytska oblast","region",NULL)
            ,("UA","UKR",804,"UA-71","Cherkaska oblast","region",NULL)
            ,("UA","UKR",804,"UA-74","Chernihivska oblast","region",NULL)
            ,("UA","UKR",804,"UA-77","Chernivetska oblast","region",NULL)
            ,("UG","UGA",800,"UG-101","Kalangala","district","UG-C")
            ,("UG","UGA",800,"UG-102","Kampala","city","UG-C")
            ,("UG","UGA",800,"UG-103","Kiboga","district","UG-C")
            ,("UG","UGA",800,"UG-104","Luwero","district","UG-C")
            ,("UG","UGA",800,"UG-105","Masaka","district","UG-C")
            ,("UG","UGA",800,"UG-106","Mpigi","district","UG-C")
            ,("UG","UGA",800,"UG-107","Mubende","district","UG-C")
            ,("UG","UGA",800,"UG-108","Mukono","district","UG-C")
            ,("UG","UGA",800,"UG-109","Nakasongola","district","UG-C")
            ,("UG","UGA",800,"UG-110","Rakai","district","UG-C")
            ,("UG","UGA",800,"UG-111","Sembabule","district","UG-C")
            ,("UG","UGA",800,"UG-112","Kayunga","district","UG-C")
            ,("UG","UGA",800,"UG-113","Wakiso","district","UG-C")
            ,("UG","UGA",800,"UG-114","Lyantonde","district","UG-C")
            ,("UG","UGA",800,"UG-115","Mityana","district","UG-C")
            ,("UG","UGA",800,"UG-116","Nakaseke","district","UG-C")
            ,("UG","UGA",800,"UG-117","Buikwe","district","UG-C")
            ,("UG","UGA",800,"UG-118","Bukomansibi","district","UG-C")
            ,("UG","UGA",800,"UG-119","Butambala","district","UG-C")
            ,("UG","UGA",800,"UG-120","Buvuma","district","UG-C")
            ,("UG","UGA",800,"UG-121","Gomba","district","UG-C")
            ,("UG","UGA",800,"UG-122","Kalungu","district","UG-C")
            ,("UG","UGA",800,"UG-123","Kyankwanzi","district","UG-C")
            ,("UG","UGA",800,"UG-124","Lwengo","district","UG-C")
            ,("UG","UGA",800,"UG-125","Kyotera","district","UG-C")
            ,("UG","UGA",800,"UG-126","Kasanda","district","UG-C")
            ,("UG","UGA",800,"UG-201","Bugiri","district","UG-E")
            ,("UG","UGA",800,"UG-202","Busia","district","UG-E")
            ,("UG","UGA",800,"UG-203","Iganga","district","UG-E")
            ,("UG","UGA",800,"UG-204","Jinja","district","UG-E")
            ,("UG","UGA",800,"UG-205","Kamuli","district","UG-E")
            ,("UG","UGA",800,"UG-206","Kapchorwa","district","UG-E")
            ,("UG","UGA",800,"UG-207","Katakwi","district","UG-E")
            ,("UG","UGA",800,"UG-208","Kumi","district","UG-E")
            ,("UG","UGA",800,"UG-209","Mbale","district","UG-E")
            ,("UG","UGA",800,"UG-210","Pallisa","district","UG-E")
            ,("UG","UGA",800,"UG-211","Soroti","district","UG-E")
            ,("UG","UGA",800,"UG-212","Tororo","district","UG-E")
            ,("UG","UGA",800,"UG-213","Kaberamaido","district","UG-E")
            ,("UG","UGA",800,"UG-214","Mayuge","district","UG-E")
            ,("UG","UGA",800,"UG-215","Sironko","district","UG-E")
            ,("UG","UGA",800,"UG-216","Amuria","district","UG-E")
            ,("UG","UGA",800,"UG-217","Budaka","district","UG-E")
            ,("UG","UGA",800,"UG-218","Bududa","district","UG-E")
            ,("UG","UGA",800,"UG-219","Bukedea","district","UG-E")
            ,("UG","UGA",800,"UG-220","Bukwo","district","UG-E")
            ,("UG","UGA",800,"UG-221","Butaleja","district","UG-E")
            ,("UG","UGA",800,"UG-222","Kaliro","district","UG-E")
            ,("UG","UGA",800,"UG-223","Manafwa","district","UG-E")
            ,("UG","UGA",800,"UG-224","Namutumba","district","UG-E")
            ,("UG","UGA",800,"UG-225","Bulambuli","district","UG-E")
            ,("UG","UGA",800,"UG-226","Buyende","district","UG-E")
            ,("UG","UGA",800,"UG-227","Kibuku","district","UG-E")
            ,("UG","UGA",800,"UG-228","Kween","district","UG-E")
            ,("UG","UGA",800,"UG-229","Luuka","district","UG-E")
            ,("UG","UGA",800,"UG-230","Namayingo","district","UG-E")
            ,("UG","UGA",800,"UG-231","Ngora","district","UG-E")
            ,("UG","UGA",800,"UG-232","Serere","district","UG-E")
            ,("UG","UGA",800,"UG-233","Butebo","district","UG-E")
            ,("UG","UGA",800,"UG-234","Namisindwa","district","UG-E")
            ,("UG","UGA",800,"UG-235","Bugweri","district","UG-E")
            ,("UG","UGA",800,"UG-236","Kapelebyong","district","UG-E")
            ,("UG","UGA",800,"UG-237","Kalaki","district","UG-E")
            ,("UG","UGA",800,"UG-301","Adjumani","district","UG-N")
            ,("UG","UGA",800,"UG-302","Apac","district","UG-N")
            ,("UG","UGA",800,"UG-303","Arua","district","UG-N")
            ,("UG","UGA",800,"UG-304","Gulu","district","UG-N")
            ,("UG","UGA",800,"UG-305","Kitgum","district","UG-N")
            ,("UG","UGA",800,"UG-306","Kotido","district","UG-N")
            ,("UG","UGA",800,"UG-307","Lira","district","UG-N")
            ,("UG","UGA",800,"UG-308","Moroto","district","UG-N")
            ,("UG","UGA",800,"UG-309","Moyo","district","UG-N")
            ,("UG","UGA",800,"UG-310","Nebbi","district","UG-N")
            ,("UG","UGA",800,"UG-311","Nakapiripirit","district","UG-N")
            ,("UG","UGA",800,"UG-312","Pader","district","UG-N")
            ,("UG","UGA",800,"UG-313","Yumbe","district","UG-N")
            ,("UG","UGA",800,"UG-314","Abim","district","UG-N")
            ,("UG","UGA",800,"UG-315","Amolatar","district","UG-N")
            ,("UG","UGA",800,"UG-316","Amuru","district","UG-N")
            ,("UG","UGA",800,"UG-317","Dokolo","district","UG-N")
            ,("UG","UGA",800,"UG-318","Kaabong","district","UG-N")
            ,("UG","UGA",800,"UG-319","Koboko","district","UG-N")
            ,("UG","UGA",800,"UG-320","Maracha","district","UG-N")
            ,("UG","UGA",800,"UG-321","Oyam","district","UG-N")
            ,("UG","UGA",800,"UG-322","Agago","district","UG-N")
            ,("UG","UGA",800,"UG-323","Alebtong","district","UG-N")
            ,("UG","UGA",800,"UG-324","Amudat","district","UG-N")
            ,("UG","UGA",800,"UG-325","Kole","district","UG-N")
            ,("UG","UGA",800,"UG-326","Lamwo","district","UG-N")
            ,("UG","UGA",800,"UG-327","Napak","district","UG-N")
            ,("UG","UGA",800,"UG-328","Nwoya","district","UG-N")
            ,("UG","UGA",800,"UG-329","Otuke","district","UG-N")
            ,("UG","UGA",800,"UG-330","Zombo","district","UG-N")
            ,("UG","UGA",800,"UG-331","Omoro","district","UG-N")
            ,("UG","UGA",800,"UG-332","Pakwach","district","UG-N")
            ,("UG","UGA",800,"UG-333","Kwania","district","UG-N")
            ,("UG","UGA",800,"UG-334","Nabilatuk","district","UG-N")
            ,("UG","UGA",800,"UG-335","Karenga","district","UG-N")
            ,("UG","UGA",800,"UG-336","Madi-Okollo","district","UG-N")
            ,("UG","UGA",800,"UG-337","Obongi","district","UG-N")
            ,("UG","UGA",800,"UG-401","Bundibugyo","district","UG-W")
            ,("UG","UGA",800,"UG-402","Bushenyi","district","UG-W")
            ,("UG","UGA",800,"UG-403","Hoima","district","UG-W")
            ,("UG","UGA",800,"UG-404","Kabale","district","UG-W")
            ,("UG","UGA",800,"UG-405","Kabarole","district","UG-W")
            ,("UG","UGA",800,"UG-406","Kasese","district","UG-W")
            ,("UG","UGA",800,"UG-407","Kibaale","district","UG-W")
            ,("UG","UGA",800,"UG-408","Kisoro","district","UG-W")
            ,("UG","UGA",800,"UG-409","Masindi","district","UG-W")
            ,("UG","UGA",800,"UG-410","Mbarara","district","UG-W")
            ,("UG","UGA",800,"UG-411","Ntungamo","district","UG-W")
            ,("UG","UGA",800,"UG-412","Rukungiri","district","UG-W")
            ,("UG","UGA",800,"UG-413","Kamwenge","district","UG-W")
            ,("UG","UGA",800,"UG-414","Kanungu","district","UG-W")
            ,("UG","UGA",800,"UG-415","Kyenjojo","district","UG-W")
            ,("UG","UGA",800,"UG-416","Buliisa","district","UG-W")
            ,("UG","UGA",800,"UG-417","Ibanda","district","UG-W")
            ,("UG","UGA",800,"UG-418","Isingiro","district","UG-W")
            ,("UG","UGA",800,"UG-419","Kiruhura","district","UG-W")
            ,("UG","UGA",800,"UG-420","Buhweju","district","UG-W")
            ,("UG","UGA",800,"UG-421","Kiryandongo","district","UG-W")
            ,("UG","UGA",800,"UG-422","Kyegegwa","district","UG-W")
            ,("UG","UGA",800,"UG-423","Mitooma","district","UG-W")
            ,("UG","UGA",800,"UG-424","Ntoroko","district","UG-W")
            ,("UG","UGA",800,"UG-425","Rubirizi","district","UG-W")
            ,("UG","UGA",800,"UG-426","Sheema","district","UG-W")
            ,("UG","UGA",800,"UG-427","Kagadi","district","UG-W")
            ,("UG","UGA",800,"UG-428","Kakumiro","district","UG-W")
            ,("UG","UGA",800,"UG-429","Rubanda","district","UG-W")
            ,("UG","UGA",800,"UG-430","Bunyangabu","district","UG-W")
            ,("UG","UGA",800,"UG-431","Rukiga","district","UG-W")
            ,("UG","UGA",800,"UG-432","Kikuube","district","UG-W")
            ,("UG","UGA",800,"UG-433","Kazo","district","UG-W")
            ,("UG","UGA",800,"UG-434","Kitagwenda","district","UG-W")
            ,("UG","UGA",800,"UG-435","Rwampara","district","UG-W")
            ,("UG","UGA",800,"UG-C","Central","geographical_region",NULL)
            ,("UG","UGA",800,"UG-E","Eastern","geographical_region",NULL)
            ,("UG","UGA",800,"UG-N","Northern","geographical_region",NULL)
            ,("UG","UGA",800,"UG-W","Western","geographical_region",NULL)
            ,("UM","UMI",581,"UM-67","Johnston Atoll","island",NULL)
            ,("UM","UMI",581,"UM-71","Midway Islands","island",NULL)
            ,("UM","UMI",581,"UM-76","Navassa Island","island",NULL)
            ,("UM","UMI",581,"UM-79","Wake Island","island",NULL)
            ,("UM","UMI",581,"UM-81","Baker Island","island",NULL)
            ,("UM","UMI",581,"UM-84","Howland Island","island",NULL)
            ,("UM","UMI",581,"UM-86","Jarvis Island","island",NULL)
            ,("UM","UMI",581,"UM-89","Kingman Reef","island",NULL)
            ,("UM","UMI",581,"UM-95","Palmyra Atoll","island",NULL)
            ,("US","USA",840,"US-AK","Alaska","state",NULL)
            ,("US","USA",840,"US-AL","Alabama","state",NULL)
            ,("US","USA",840,"US-AR","Arkansas","state",NULL)
            ,("US","USA",840,"US-AS","American Samoa","outlying_area",NULL)
            ,("US","USA",840,"US-AZ","Arizona","state",NULL)
            ,("US","USA",840,"US-CA","California","state",NULL)
            ,("US","USA",840,"US-CO","Colorado","state",NULL)
            ,("US","USA",840,"US-CT","Connecticut","state",NULL)
            ,("US","USA",840,"US-DC","District of Columbia","District",NULL)
            ,("US","USA",840,"US-DE","Delaware","state",NULL)
            ,("US","USA",840,"US-FL","Florida","state",NULL)
            ,("US","USA",840,"US-GA","Georgia","state",NULL)
            ,("US","USA",840,"US-GU","Guam","outlying_area",NULL)
            ,("US","USA",840,"US-HI","Hawaii","state",NULL)
            ,("US","USA",840,"US-IA","Iowa","state",NULL)
            ,("US","USA",840,"US-ID","Idaho","state",NULL)
            ,("US","USA",840,"US-IL","Illinois","state",NULL)
            ,("US","USA",840,"US-IN","Indiana","state",NULL)
            ,("US","USA",840,"US-KS","Kansas","state",NULL)
            ,("US","USA",840,"US-KY","Kentucky","state",NULL)
            ,("US","USA",840,"US-LA","Louisiana","state",NULL)
            ,("US","USA",840,"US-MA","Massachusetts","state",NULL)
            ,("US","USA",840,"US-MD","Maryland","state",NULL)
            ,("US","USA",840,"US-ME","Maine","state",NULL)
            ,("US","USA",840,"US-MI","Michigan","state",NULL)
            ,("US","USA",840,"US-MN","Minnesota","state",NULL)
            ,("US","USA",840,"US-MO","Missouri","state",NULL)
            ,("US","USA",840,"US-MP",
                "Northern Mariana Islands","outlying_area",NULL)
            ,("US","USA",840,"US-MS","Mississippi","state",NULL)
            ,("US","USA",840,"US-MT","Montana","state",NULL)
            ,("US","USA",840,"US-NC","North Carolina","state",NULL)
            ,("US","USA",840,"US-ND","North Dakota","state",NULL)
            ,("US","USA",840,"US-NE","Nebraska","state",NULL)
            ,("US","USA",840,"US-NH","New Hampshire","state",NULL)
            ,("US","USA",840,"US-NJ","New Jersey","state",NULL)
            ,("US","USA",840,"US-NM","New Mexico","state",NULL)
            ,("US","USA",840,"US-NV","Nevada","state",NULL)
            ,("US","USA",840,"US-NY","New York","state",NULL)
            ,("US","USA",840,"US-OH","Ohio","state",NULL)
            ,("US","USA",840,"US-OK","Oklahoma","state",NULL)
            ,("US","USA",840,"US-OR","Oregon","state",NULL)
            ,("US","USA",840,"US-PA","Pennsylvania","state",NULL)
            ,("US","USA",840,"US-PR","Puerto Rico","outlying_area",NULL)
            ,("US","USA",840,"US-RI","Rhode Island","state",NULL)
            ,("US","USA",840,"US-SC","South Carolina","state",NULL)
            ,("US","USA",840,"US-SD","South Dakota","state",NULL)
            ,("US","USA",840,"US-TN","Tennessee","state",NULL)
            ,("US","USA",840,"US-TX","Texas","state",NULL)
            ,("US","USA",840,"US-UM",
                "United States Minor Outlying Islands","outlying_area",NULL)
            ,("US","USA",840,"US-UT","Utah","state",NULL)
            ,("US","USA",840,"US-VA","Virginia","state",NULL)
            ,("US","USA",840,"US-VI",
                "Virgin Islands, U.S.","outlying_area",NULL)
            ,("US","USA",840,"US-VT","Vermont","state",NULL)
            ,("US","USA",840,"US-WA","Washington","state",NULL)
            ,("US","USA",840,"US-WI","Wisconsin","state",NULL)
            ,("US","USA",840,"US-WV","West Virginia","state",NULL)
            ,("US","USA",840,"US-WY","Wyoming","state",NULL)
            ,("UY","URY",858,"UY-AR","Artigas","department",NULL)
            ,("UY","URY",858,"UY-CA","Canelones","department",NULL)
            ,("UY","URY",858,"UY-CL","Cerro Largo","department",NULL)
            ,("UY","URY",858,"UY-CO","Colonia","department",NULL)
            ,("UY","URY",858,"UY-DU","Durazno","department",NULL)
            ,("UY","URY",858,"UY-FD","Florida","department",NULL)
            ,("UY","URY",858,"UY-FS","Flores","department",NULL)
            ,("UY","URY",858,"UY-LA","Lavalleja","department",NULL)
            ,("UY","URY",858,"UY-MA","Maldonado","department",NULL)
            ,("UY","URY",858,"UY-MO","Montevideo","department",NULL)
            ,("UY","URY",858,"UY-PA","Paysandú","department",NULL)
            ,("UY","URY",858,"UY-RN","Río Negro","department",NULL)
            ,("UY","URY",858,"UY-RO","Rocha","department",NULL)
            ,("UY","URY",858,"UY-RV","Rivera","department",NULL)
            ,("UY","URY",858,"UY-SA","Salto","department",NULL)
            ,("UY","URY",858,"UY-SJ","San José","department",NULL)
            ,("UY","URY",858,"UY-SO","Soriano","department",NULL)
            ,("UY","URY",858,"UY-TA","Tacuarembó","department",NULL)
            ,("UY","URY",858,"UY-TT","Treinta y Tres","department",NULL)
            ,("UZ","UZB",860,"UZ-AN","Andijon","region",NULL)
            ,("UZ","UZB",860,"UZ-BU","Buxoro","region",NULL)
            ,("UZ","UZB",860,"UZ-FA","Farg'ona","region",NULL)
            ,("UZ","UZB",860,"UZ-JI","Jizzax","region",NULL)
            ,("UZ","UZB",860,"UZ-NG","Namangan","region",NULL)
            ,("UZ","UZB",860,"UZ-NW","Navoiy","region",NULL)
            ,("UZ","UZB",860,"UZ-QA","Qashqadaryo","region",NULL)
            ,("UZ","UZB",860,"UZ-QR",
                "Qoraqalpog'iston Respublikasi","republic",NULL)
            ,("UZ","UZB",860,"UZ-SA","Samarqand","region",NULL)
            ,("UZ","UZB",860,"UZ-SI","Sirdaryo","region",NULL)
            ,("UZ","UZB",860,"UZ-SU","Surxondaryo","region",NULL)
            ,("UZ","UZB",860,"UZ-TK","Toshkent","city",NULL)
            ,("UZ","UZB",860,"UZ-TO","Toshkent","region",NULL)
            ,("UZ","UZB",860,"UZ-XO","Xorazm","region",NULL)
            ,("VA","VAT",336,"VA-??","Vatican City","city",NULL)
            ,("VC","VCT",670,"VC-01","Charlotte","parish",NULL)
            ,("VC","VCT",670,"VC-02","Saint Andrew","parish",NULL)
            ,("VC","VCT",670,"VC-03","Saint David","parish",NULL)
            ,("VC","VCT",670,"VC-04","Saint George","parish",NULL)
            ,("VC","VCT",670,"VC-05","Saint Patrick","parish",NULL)
            ,("VC","VCT",670,"VC-06","Grenadines","parish",NULL)
            ,("VE","VEN",862,"VE-A","Distrito Capital","capital_district",NULL)
            ,("VE","VEN",862,"VE-B","Anzoátegui","state",NULL)
            ,("VE","VEN",862,"VE-C","Apure","state",NULL)
            ,("VE","VEN",862,"VE-D","Aragua","state",NULL)
            ,("VE","VEN",862,"VE-E","Barinas","state",NULL)
            ,("VE","VEN",862,"VE-F","Bolívar","state",NULL)
            ,("VE","VEN",862,"VE-G","Carabobo","state",NULL)
            ,("VE","VEN",862,"VE-H","Cojedes","state",NULL)
            ,("VE","VEN",862,"VE-I","Falcón","state",NULL)
            ,("VE","VEN",862,"VE-J","Guárico","state",NULL)
            ,("VE","VEN",862,"VE-K","Lara","state",NULL)
            ,("VE","VEN",862,"VE-L","Mérida","state",NULL)
            ,("VE","VEN",862,"VE-M","Miranda","state",NULL)
            ,("VE","VEN",862,"VE-N","Monagas","state",NULL)
            ,("VE","VEN",862,"VE-O","Nueva Esparta","state",NULL)
            ,("VE","VEN",862,"VE-P","Portuguesa","state",NULL)
            ,("VE","VEN",862,"VE-R","Sucre","state",NULL)
            ,("VE","VEN",862,"VE-S","Táchira","state",NULL)
            ,("VE","VEN",862,"VE-T","Trujillo","state",NULL)
            ,("VE","VEN",862,"VE-U","Yaracuy","state",NULL)
            ,("VE","VEN",862,"VE-V","Zulia","state",NULL)
            ,("VE","VEN",862,"VE-W",
                "Dependencias Federales","federal_dependency",NULL)
            ,("VE","VEN",862,"VE-X","La Guaira","state",NULL)
            ,("VE","VEN",862,"VE-Y","Delta Amacuro","state",NULL)
            ,("VE","VEN",862,"VE-Z","Amazonas","state",NULL)
            ,("VG","VGB",92,"VG-??","British Virgin Islands","country",NULL)
            ,("VI","VIR",850,"VI-??",
                "United States Virgin Islands","country",NULL)
            ,("VN","VNM",704,"VN-01","Lai Châu","province",NULL)
            ,("VN","VNM",704,"VN-02","Lào Cai","province",NULL)
            ,("VN","VNM",704,"VN-03","Hà Giang","province",NULL)
            ,("VN","VNM",704,"VN-04","Cao Bằng","province",NULL)
            ,("VN","VNM",704,"VN-05","Sơn La","province",NULL)
            ,("VN","VNM",704,"VN-06","Yên Bái","province",NULL)
            ,("VN","VNM",704,"VN-07","Tuyên Quang","province",NULL)
            ,("VN","VNM",704,"VN-09","Lạng Sơn","province",NULL)
            ,("VN","VNM",704,"VN-13","Quảng Ninh","province",NULL)
            ,("VN","VNM",704,"VN-14","Hòa Bình","province",NULL)
            ,("VN","VNM",704,"VN-18","Ninh Bình","province",NULL)
            ,("VN","VNM",704,"VN-20","Thái Bình","province",NULL)
            ,("VN","VNM",704,"VN-21","Thanh Hóa","province",NULL)
            ,("VN","VNM",704,"VN-22","Nghệ An","province",NULL)
            ,("VN","VNM",704,"VN-23","Hà Tĩnh","province",NULL)
            ,("VN","VNM",704,"VN-24","Quảng Bình","province",NULL)
            ,("VN","VNM",704,"VN-25","Quảng Trị","province",NULL)
            ,("VN","VNM",704,"VN-26","Thừa Thiên-Huế","province",NULL)
            ,("VN","VNM",704,"VN-27","Quảng Nam","province",NULL)
            ,("VN","VNM",704,"VN-28","Kon Tum","province",NULL)
            ,("VN","VNM",704,"VN-29","Quảng Ngãi","province",NULL)
            ,("VN","VNM",704,"VN-30","Gia Lai","province",NULL)
            ,("VN","VNM",704,"VN-31","Bình Định","province",NULL)
            ,("VN","VNM",704,"VN-32","Phú Yên","province",NULL)
            ,("VN","VNM",704,"VN-33","Đắk Lắk","province",NULL)
            ,("VN","VNM",704,"VN-34","Khánh Hòa","province",NULL)
            ,("VN","VNM",704,"VN-35","Lâm Đồng","province",NULL)
            ,("VN","VNM",704,"VN-36","Ninh Thuận","province",NULL)
            ,("VN","VNM",704,"VN-37","Tây Ninh","province",NULL)
            ,("VN","VNM",704,"VN-39","Đồng Nai","province",NULL)
            ,("VN","VNM",704,"VN-40","Bình Thuận","province",NULL)
            ,("VN","VNM",704,"VN-41","Long An","province",NULL)
            ,("VN","VNM",704,"VN-43","Bà Rịa - Vũng Tàu","province",NULL)
            ,("VN","VNM",704,"VN-44","An Giang","province",NULL)
            ,("VN","VNM",704,"VN-45","Đồng Tháp","province",NULL)
            ,("VN","VNM",704,"VN-46","Tiền Giang","province",NULL)
            ,("VN","VNM",704,"VN-47","Kiến Giang","province",NULL)
            ,("VN","VNM",704,"VN-49","Vĩnh Long","province",NULL)
            ,("VN","VNM",704,"VN-50","Bến Tre","province",NULL)
            ,("VN","VNM",704,"VN-51","Trà Vinh","province",NULL)
            ,("VN","VNM",704,"VN-52","Sóc Trăng","province",NULL)
            ,("VN","VNM",704,"VN-53","Bắc Kạn","province",NULL)
            ,("VN","VNM",704,"VN-54","Bắc Giang","province",NULL)
            ,("VN","VNM",704,"VN-55","Bạc Liêu","province",NULL)
            ,("VN","VNM",704,"VN-56","Bắc Ninh","province",NULL)
            ,("VN","VNM",704,"VN-57","Bình Dương","province",NULL)
            ,("VN","VNM",704,"VN-58","Bình Phước","province",NULL)
            ,("VN","VNM",704,"VN-59","Cà Mau","province",NULL)
            ,("VN","VNM",704,"VN-61","Hải Dương","province",NULL)
            ,("VN","VNM",704,"VN-63","Hà Nam","province",NULL)
            ,("VN","VNM",704,"VN-66","Hưng Yên","province",NULL)
            ,("VN","VNM",704,"VN-67","Nam Định","province",NULL)
            ,("VN","VNM",704,"VN-68","Phú Thọ","province",NULL)
            ,("VN","VNM",704,"VN-69","Thái Nguyên","province",NULL)
            ,("VN","VNM",704,"VN-70","Vĩnh Phúc","province",NULL)
            ,("VN","VNM",704,"VN-71","Điện Biên","province",NULL)
            ,("VN","VNM",704,"VN-72","Đắk Nông","province",NULL)
            ,("VN","VNM",704,"VN-73","Hậu Giang","province",NULL)
            ,("VN","VNM",704,"VN-CT","Cần Thơ","municipality",NULL)
            ,("VN","VNM",704,"VN-DN","Đà Nẵng","municipality",NULL)
            ,("VN","VNM",704,"VN-HN","Hà Nội","municipality",NULL)
            ,("VN","VNM",704,"VN-HP","Hải Phòng","municipality",NULL)
            ,("VN","VNM",704,"VN-SG","Hồ Chí Minh","municipality",NULL)
            ,("VU","VUT",548,"VU-MAP","Malampa","province",NULL)
            ,("VU","VUT",548,"VU-PAM","Pénama","province",NULL)
            ,("VU","VUT",548,"VU-SAM","Sanma","province",NULL)
            ,("VU","VUT",548,"VU-SEE","Shéfa","province",NULL)
            ,("VU","VUT",548,"VU-TAE","Taféa","province",NULL)
            ,("VU","VUT",548,"VU-TOB","Torba","province",NULL)
            ,("WF","WLF",876,"WF-AL","Alo","precinct",NULL)
            ,("WF","WLF",876,"WF-SG","Sigave","precinct",NULL)
            ,("WF","WLF",876,"WF-UV","Uvea","precinct",NULL)
            ,("WS","WSM",882,"WS-AA","A'ana","district",NULL)
            ,("WS","WSM",882,"WS-AL","Aiga-i-le-Tai","district",NULL)
            ,("WS","WSM",882,"WS-AT","Atua","district",NULL)
            ,("WS","WSM",882,"WS-FA","Fa'asaleleaga","district",NULL)
            ,("WS","WSM",882,"WS-GE","Gaga'emauga","district",NULL)
            ,("WS","WSM",882,"WS-GI","Gagaifomauga","district",NULL)
            ,("WS","WSM",882,"WS-PA","Palauli","district",NULL)
            ,("WS","WSM",882,"WS-SA","Satupa'itea","district",NULL)
            ,("WS","WSM",882,"WS-TU","Tuamasaga","district",NULL)
            ,("WS","WSM",882,"WS-VF","Va'a-o-Fonoti","district",NULL)
            ,("WS","WSM",882,"WS-VS","Vaisigano","district",NULL)
            ,("YE","YEM",887,"YE-AB","Abyan","governorate",NULL)
            ,("YE","YEM",887,"YE-AD","'Adan","governorate",NULL)
            ,("YE","YEM",887,"YE-AM","'Amrān","governorate",NULL)
            ,("YE","YEM",887,"YE-BA","Al Bayḑā'","governorate",NULL)
            ,("YE","YEM",887,"YE-DA","Aḑ Ḑāli'","governorate",NULL)
            ,("YE","YEM",887,"YE-DH","Dhamār","governorate",NULL)
            ,("YE","YEM",887,"YE-HD","Ḩaḑramawt","governorate",NULL)
            ,("YE","YEM",887,"YE-HJ","Ḩajjah","governorate",NULL)
            ,("YE","YEM",887,"YE-HU","Al Ḩudaydah","governorate",NULL)
            ,("YE","YEM",887,"YE-IB","Ibb","governorate",NULL)
            ,("YE","YEM",887,"YE-JA","Al Jawf","governorate",NULL)
            ,("YE","YEM",887,"YE-LA","Laḩij","governorate",NULL)
            ,("YE","YEM",887,"YE-MA","Ma'rib","governorate",NULL)
            ,("YE","YEM",887,"YE-MR","Al Mahrah","governorate",NULL)
            ,("YE","YEM",887,"YE-MW","Al Maḩwīt","governorate",NULL)
            ,("YE","YEM",887,"YE-RA","Raymah","governorate",NULL)
            ,("YE","YEM",887,"YE-SA","Amānat al 'Āşimah","municipality",NULL)
            ,("YE","YEM",887,"YE-SD","Şā'dah","governorate",NULL)
            ,("YE","YEM",887,"YE-SH","Shabwah","governorate",NULL)
            ,("YE","YEM",887,"YE-SN","San'a'","governorate",NULL)
            ,("YE","YEM",887,"YE-SU","Arkhabīl Suquţrá","governorate",NULL)
            ,("YE","YEM",887,"YE-TA","Tā'izz","governorate",NULL)
            ,("YT","MYT",175,"YT-??","Mayotte","country",NULL)
            ,("ZA","ZAF",710,"ZA-EC","Eastern Cape","province",NULL)
            ,("ZA","ZAF",710,"ZA-FS","Free State","province",NULL)
            ,("ZA","ZAF",710,"ZA-GP","Gauteng","province",NULL)
            ,("ZA","ZAF",710,"ZA-KZN","Kwazulu-Natal","province",NULL)
            ,("ZA","ZAF",710,"ZA-LP","Limpopo","province",NULL)
            ,("ZA","ZAF",710,"ZA-MP","Mpumalanga","province",NULL)
            ,("ZA","ZAF",710,"ZA-NC","Northern Cape","province",NULL)
            ,("ZA","ZAF",710,"ZA-NW","North-West","province",NULL)
            ,("ZA","ZAF",710,"ZA-WC","Western Cape","province",NULL)
            ,("ZM","ZMB",894,"ZM-01","Western","province",NULL)
            ,("ZM","ZMB",894,"ZM-02","Central","province",NULL)
            ,("ZM","ZMB",894,"ZM-03","Eastern","province",NULL)
            ,("ZM","ZMB",894,"ZM-04","Luapula","province",NULL)
            ,("ZM","ZMB",894,"ZM-05","Northern","province",NULL)
            ,("ZM","ZMB",894,"ZM-06","North-Western","province",NULL)
            ,("ZM","ZMB",894,"ZM-07","Southern","province",NULL)
            ,("ZM","ZMB",894,"ZM-08","Copperbelt","province",NULL)
            ,("ZM","ZMB",894,"ZM-09","Lusaka","province",NULL)
            ,("ZM","ZMB",894,"ZM-10","Muchinga","province",NULL)
            ,("ZW","ZWE",716,"ZW-BU","Bulawayo","province",NULL)
            ,("ZW","ZWE",716,"ZW-HA","Harare","province",NULL)
            ,("ZW","ZWE",716,"ZW-MA","Manicaland","province",NULL)
            ,("ZW","ZWE",716,"ZW-MC","Mashonaland Central","province",NULL)
            ,("ZW","ZWE",716,"ZW-ME","Mashonaland East","province",NULL)
            ,("ZW","ZWE",716,"ZW-MI","Midlands","province",NULL)
            ,("ZW","ZWE",716,"ZW-MN","Matabeleland North","province",NULL)
            ,("ZW","ZWE",716,"ZW-MS","Matabeleland South","province",NULL)
            ,("ZW","ZWE",716,"ZW-MV","Masvingo","province",NULL)
            ,("ZW","ZWE",716,"ZW-MW","Mashonaland West","province",NULL);

        """
        return sql_script.replace("        ", "")

    def iso_timezones() -> str:
        """
        Returns a SQL INSERT script that inserts a list of timezones,
        and their corresponding ISO country.
        Data sourced from https://gist.github.com/pamelafox/986163

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a a SQL INSERT script that inserts
        a list of timezones, and their corresponding ISO country

        """

        sql_script = """
        CREATE TABLE iso_timezones(
            "timezone_name"         TEXT NOT NULL PRIMARY KEY
            ,"nation_iso_alpha_2"   TEXT NOT NULL
        );
        INSERT INTO iso_timezones("timezone_name","nation_iso_alpha_2") VALUES
            ('Europe/Andorra','AD')
            ,('Asia/Kabul','AF')
            ,('America/Antigua','AG')
            ,('Europe/Tirane','AL')
            ,('Asia/Yerevan','AM')
            ,('Africa/Luanda','AO')
            ,('America/Argentina/Buenos_Aires','AR')
            ,('America/Argentina/Cordoba','AR')
            ,('America/Argentina/Jujuy','AR')
            ,('America/Argentina/Tucuman','AR')
            ,('America/Argentina/Catamarca','AR')
            ,('America/Argentina/La_Rioja','AR')
            ,('America/Argentina/San_Juan','AR')
            ,('America/Argentina/Mendoza','AR')
            ,('America/Argentina/Rio_Gallegos','AR')
            ,('America/Argentina/Ushuaia','AR')
            ,('Europe/Vienna','AT')
            ,('Australia/Lord_Howe','AU')
            ,('Australia/Hobart','AU')
            ,('Australia/Currie','AU')
            ,('Australia/Melbourne','AU')
            ,('Australia/Sydney','AU')
            ,('Australia/Broken_Hill','AU')
            ,('Australia/Brisbane','AU')
            ,('Australia/Lindeman','AU')
            ,('Australia/Adelaide','AU')
            ,('Australia/Darwin','AU')
            ,('Australia/Perth','AU')
            ,('Asia/Baku','AZ')
            ,('America/Barbados','BB')
            ,('Asia/Dhaka','BD')
            ,('Europe/Brussels','BE')
            ,('Africa/Ouagadougou','BF')
            ,('Europe/Sofia','BG')
            ,('Asia/Bahrain','BH')
            ,('Africa/Bujumbura','BI')
            ,('Africa/Porto-Novo','BJ')
            ,('Asia/Brunei','BN')
            ,('America/La_Paz','BO')
            ,('America/Noronha','BR')
            ,('America/Belem','BR')
            ,('America/Fortaleza','BR')
            ,('America/Recife','BR')
            ,('America/Araguaina','BR')
            ,('America/Maceio','BR')
            ,('America/Bahia','BR')
            ,('America/Sao_Paulo','BR')
            ,('America/Campo_Grande','BR')
            ,('America/Cuiaba','BR')
            ,('America/Porto_Velho','BR')
            ,('America/Boa_Vista','BR')
            ,('America/Manaus','BR')
            ,('America/Eirunepe','BR')
            ,('America/Rio_Branco','BR')
            ,('America/Nassau','BS')
            ,('Asia/Thimphu','BT')
            ,('Africa/Gaborone','BW')
            ,('Europe/Minsk','BY')
            ,('America/Belize','BZ')
            ,('America/St_Johns','CA')
            ,('America/Halifax','CA')
            ,('America/Glace_Bay','CA')
            ,('America/Moncton','CA')
            ,('America/Goose_Bay','CA')
            ,('America/Blanc-Sablon','CA')
            ,('America/Montreal','CA')
            ,('America/Toronto','CA')
            ,('America/Nipigon','CA')
            ,('America/Thunder_Bay','CA')
            ,('America/Pangnirtung','CA')
            ,('America/Iqaluit','CA')
            ,('America/Atikokan','CA')
            ,('America/Rankin_Inlet','CA')
            ,('America/Winnipeg','CA')
            ,('America/Rainy_River','CA')
            ,('America/Cambridge_Bay','CA')
            ,('America/Regina','CA')
            ,('America/Swift_Current','CA')
            ,('America/Edmonton','CA')
            ,('America/Yellowknife','CA')
            ,('America/Inuvik','CA')
            ,('America/Dawson_Creek','CA')
            ,('America/Vancouver','CA')
            ,('America/Whitehorse','CA')
            ,('America/Dawson','CA')
            ,('Africa/Kinshasa','CD')
            ,('Africa/Lubumbashi','CD')
            ,('Africa/Brazzaville','CG')
            ,('Africa/Abidjan','CI')
            ,('America/Santiago','CL')
            ,('Pacific/Easter','CL')
            ,('Africa/Douala','CM')
            ,('Asia/Shanghai','CN')
            ,('Asia/Harbin','CN')
            ,('Asia/Chongqing','CN')
            ,('Asia/Urumqi','CN')
            ,('Asia/Kashgar','CN')
            ,('America/Bogota','CO')
            ,('America/Costa_Rica','CR')
            ,('America/Havana','CU')
            ,('Atlantic/Cape_Verde','CV')
            ,('Asia/Nicosia','CY')
            ,('Europe/Prague','CZ')
            ,('Europe/Berlin','DE')
            ,('Africa/Djibouti','DJ')
            ,('Europe/Copenhagen','DK')
            ,('America/Dominica','DM')
            ,('America/Santo_Domingo','DO')
            ,('America/Guayaquil','EC')
            ,('Pacific/Galapagos','EC')
            ,('Europe/Tallinn','EE')
            ,('Africa/Cairo','EG')
            ,('Africa/Asmera','ER')
            ,('Africa/Addis_Ababa','ET')
            ,('Europe/Helsinki','FI')
            ,('Pacific/Fiji','FJ')
            ,('Europe/Paris','FR')
            ,('Africa/Libreville','GA')
            ,('Asia/Tbilisi','GE')
            ,('Africa/Accra','GH')
            ,('Africa/Banjul','GM')
            ,('Africa/Conakry','GN')
            ,('Europe/Athens','GR')
            ,('America/Guatemala','GT')
            ,('Africa/Bissau','GW')
            ,('America/Guyana','GY')
            ,('America/Tegucigalpa','HN')
            ,('Europe/Budapest','HU')
            ,('Asia/Jakarta','ID')
            ,('Asia/Pontianak','ID')
            ,('Asia/Makassar','ID')
            ,('Asia/Jayapura','ID')
            ,('Europe/Dublin','IE')
            ,('Asia/Jerusalem','IL')
            ,('Asia/Calcutta','IN')
            ,('Asia/Baghdad','IQ')
            ,('Asia/Tehran','IR')
            ,('Atlantic/Reykjavik','IS')
            ,('Europe/Rome','IT')
            ,('America/Jamaica','JM')
            ,('Asia/Amman','JO')
            ,('Asia/Tokyo','JP')
            ,('Africa/Nairobi','KE')
            ,('Asia/Bishkek','KG')
            ,('Pacific/Tarawa','KI')
            ,('Pacific/Enderbury','KI')
            ,('Pacific/Kiritimati','KI')
            ,('Asia/Pyongyang','KP')
            ,('Asia/Seoul','KR')
            ,('Asia/Kuwait','KW')
            ,('Asia/Beirut','LB')
            ,('Europe/Vaduz','LI')
            ,('Africa/Monrovia','LR')
            ,('Africa/Maseru','LS')
            ,('Europe/Vilnius','LT')
            ,('Europe/Luxembourg','LU')
            ,('Europe/Riga','LV')
            ,('Africa/Tripoli','LY')
            ,('Indian/Antananarivo','MG')
            ,('Pacific/Majuro','MH')
            ,('Pacific/Kwajalein','MH')
            ,('Europe/Skopje','MK')
            ,('Africa/Bamako','ML')
            ,('Asia/Rangoon','MM')
            ,('Asia/Ulaanbaatar','MN')
            ,('Asia/Hovd','MN')
            ,('Asia/Choibalsan','MN')
            ,('Africa/Nouakchott','MR')
            ,('Europe/Malta','MT')
            ,('Indian/Mauritius','MU')
            ,('Indian/Maldives','MV')
            ,('Africa/Blantyre','MW')
            ,('America/Mexico_City','MX')
            ,('America/Cancun','MX')
            ,('America/Merida','MX')
            ,('America/Monterrey','MX')
            ,('America/Mazatlan','MX')
            ,('America/Chihuahua','MX')
            ,('America/Hermosillo','MX')
            ,('America/Tijuana','MX')
            ,('Asia/Kuala_Lumpur','MY')
            ,('Asia/Kuching','MY')
            ,('Africa/Maputo','MZ')
            ,('Africa/Windhoek','NA')
            ,('Africa/Niamey','NE')
            ,('Africa/Lagos','NG')
            ,('America/Managua','NI')
            ,('Europe/Amsterdam','NL')
            ,('Europe/Oslo','NO')
            ,('Asia/Katmandu','NP')
            ,('Pacific/Nauru','NR')
            ,('Pacific/Auckland','NZ')
            ,('Pacific/Chatham','NZ')
            ,('Asia/Muscat','OM')
            ,('America/Panama','PA')
            ,('America/Lima','PE')
            ,('Pacific/Port_Moresby','PG')
            ,('Asia/Manila','PH')
            ,('Asia/Karachi','PK')
            ,('Europe/Warsaw','PL')
            ,('Europe/Lisbon','PT')
            ,('Atlantic/Madeira','PT')
            ,('Atlantic/Azores','PT')
            ,('Pacific/Palau','PW')
            ,('America/Asuncion','PY')
            ,('Asia/Qatar','QA')
            ,('Europe/Bucharest','RO')
            ,('Europe/Kaliningrad','RU')
            ,('Europe/Moscow','RU')
            ,('Europe/Volgograd','RU')
            ,('Europe/Samara','RU')
            ,('Asia/Yekaterinburg','RU')
            ,('Asia/Omsk','RU')
            ,('Asia/Novosibirsk','RU')
            ,('Asia/Krasnoyarsk','RU')
            ,('Asia/Irkutsk','RU')
            ,('Asia/Yakutsk','RU')
            ,('Asia/Vladivostok','RU')
            ,('Asia/Sakhalin','RU')
            ,('Asia/Magadan','RU')
            ,('Asia/Kamchatka','RU')
            ,('Asia/Anadyr','RU')
            ,('Africa/Kigali','RW')
            ,('Asia/Riyadh','SA')
            ,('Pacific/Guadalcanal','SB')
            ,('Indian/Mahe','SC')
            ,('Africa/Khartoum','SD')
            ,('Europe/Stockholm','SE')
            ,('Asia/Singapore','SG')
            ,('Europe/Ljubljana','SI')
            ,('Europe/Bratislava','SK')
            ,('Africa/Freetown','SL')
            ,('Europe/San_Marino','SM')
            ,('Africa/Dakar','SN')
            ,('Africa/Mogadishu','SO')
            ,('America/Paramaribo','SR')
            ,('Africa/Sao_Tome','ST')
            ,('Asia/Damascus','SY')
            ,('Africa/Lome','TG')
            ,('Asia/Bangkok','TH')
            ,('Asia/Dushanbe','TJ')
            ,('Asia/Ashgabat','TM')
            ,('Africa/Tunis','TN')
            ,('Pacific/Tongatapu','TO')
            ,('Europe/Istanbul','TR')
            ,('America/Port_of_Spain','TT')
            ,('Pacific/Funafuti','TV')
            ,('Africa/Dar_es_Salaam','TZ')
            ,('Europe/Kiev','UA')
            ,('Europe/Uzhgorod','UA')
            ,('Europe/Zaporozhye','UA')
            ,('Europe/Simferopol','UA')
            ,('Africa/Kampala','UG')
            ,('America/New_York','US')
            ,('America/Detroit','US')
            ,('America/Kentucky/Louisville','US')
            ,('America/Kentucky/Monticello','US')
            ,('America/Indiana/Indianapolis','US')
            ,('America/Indiana/Marengo','US')
            ,('America/Indiana/Knox','US')
            ,('America/Indiana/Vevay','US')
            ,('America/Chicago','US')
            ,('America/Indiana/Vincennes','US')
            ,('America/Indiana/Petersburg','US')
            ,('America/Menominee','US')
            ,('America/North_Dakota/Center','US')
            ,('America/North_Dakota/New_Salem','US')
            ,('America/Denver','US')
            ,('America/Boise','US')
            ,('America/Shiprock','US')
            ,('America/Phoenix','US')
            ,('America/Los_Angeles','US')
            ,('America/Anchorage','US')
            ,('America/Juneau','US')
            ,('America/Yakutat','US')
            ,('America/Nome','US')
            ,('America/Adak','US')
            ,('Pacific/Honolulu','US')
            ,('America/Montevideo','UY')
            ,('Asia/Samarkand','UZ')
            ,('Asia/Tashkent','UZ')
            ,('Europe/Vatican','VA')
            ,('America/Caracas','VE')
            ,('Asia/Saigon','VN')
            ,('Pacific/Efate','VU')
            ,('Asia/Aden','YE')
            ,('Africa/Lusaka','ZM')
            ,('Africa/Harare','ZW')
            ,('Africa/Algiers','DZ')
            ,('Europe/Sarajevo','BA')
            ,('Asia/Phnom_Penh','KH')
            ,('Africa/Bangui','CF')
            ,('Africa/Ndjamena','TD')
            ,('Indian/Comoro','KM')
            ,('Europe/Zagreb','HR')
            ,('Asia/Dili','TL')
            ,('America/El_Salvador','SV')
            ,('Africa/Malabo','GQ')
            ,('America/Grenada','GD')
            ,('Asia/Almaty','KZ')
            ,('Asia/Qyzylorda','KZ')
            ,('Asia/Aqtobe','KZ')
            ,('Asia/Aqtau','KZ')
            ,('Asia/Oral','KZ')
            ,('Asia/Vientiane','LA')
            ,('Pacific/Truk','FM')
            ,('Pacific/Ponape','FM')
            ,('Pacific/Kosrae','FM')
            ,('Europe/Chisinau','MD')
            ,('Europe/Monaco','MC')
            ,('Europe/Podgorica','ME')
            ,('Africa/Casablanca','MA')
            ,('America/St_Kitts','KN')
            ,('America/St_Lucia','LC')
            ,('America/St_Vincent','VC')
            ,('Pacific/Apia','WS')
            ,('Europe/Belgrade','RS')
            ,('Africa/Johannesburg','ZA')
            ,('Europe/Madrid','ES')
            ,('Africa/Ceuta','ES')
            ,('Atlantic/Canary','ES')
            ,('Asia/Colombo','LK')
            ,('Africa/Mbabane','SZ')
            ,('Europe/Zurich','CH')
            ,('Asia/Dubai','AE')
            ,('Europe/London','GB');

        CREATE UNIQUE INDEX idx_timezones_id
        ON iso_timezones (timezone_name);

        """
        return sql_script.replace("        ", "")

    def leagues_sql_file() -> str:
        """
        Returns a SQLite3 script that creates
        a table to hold football league information.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a table
        to hold football league information.
        """

        sql_script = """
        CREATE TABLE "fb_leagues" (
            "league_id"  TEXT UNIQUE,
            "league_long_name"  TEXT NOT NULL,
            "league_short_name"  TEXT NOT NULL,
            -- "league_sport_type"  TEXT NOT NULL,
            -- "league_default_sex"  TEXT NOT NULL,
            -- "league_default_gender"  TEXT NOT NULL,
            "league_notes"  TEXT,
            "field_length"  INTEGER NOT NULL DEFAULT 100,
            "downs"  INTEGER NOT NULL DEFAULT 4,
            "first_down_yards"  INTEGER NOT NULL DEFAULT 10,
            "end_zone_length"  INTEGER NOT NULL DEFAULT 10,
            "kickoff_yardline"  INTEGER NOT NULL DEFAULT 35,
            "safety_kick_yardline"  INTEGER NOT NULL DEFAULT 20,
            "kickoff_touchback_yardline"	INTEGER NOT NULL DEFAULT 75,
            "punt_touchback_yardline"   INTEGER NOT NULL DEFAULT 80,
            "normal_touchback_yardline"   INTEGER NOT NULL DEFAULT 80,
            "kansas_ot_yardline"  INTEGER NOT NULL DEFAULT 25,
            "pat_yardline"  INTEGER NOT NULL DEFAULT 3,
            "1PC_yardline"  INTEGER NOT NULL DEFAULT 3,
            "2PC_yardline"  INTEGER NOT NULL DEFAULT 3,
            "3PC_yardline"  INTEGER NOT NULL DEFAULT 10,
            "quarters"  INTEGER NOT NULL DEFAULT 4,
            "timeouts_per_half"  INTEGER NOT NULL DEFAULT 3,
            "ot_period_seconds"  INTEGER NOT NULL DEFAULT 900,
            "game_seconds"  INTEGER NOT NULL DEFAULT 3600,
            "half_seconds"  INTEGER NOT NULL DEFAULT 1800,
            "quarter_seconds"  INTEGER NOT NULL DEFAULT 900,
            "ot_periods"  INTEGER NOT NULL DEFAULT 1,
            "ot_periods_until_shootout"   INTEGER NOT NULL DEFAULT -1,
            "min_xfl_ot_periods"  INTEGER NOT NULL DEFAULT -1,
            "set_xfl_ot_periods"  INTEGER NOT NULL DEFAULT -1,
            "touchdown_points"  INTEGER NOT NULL DEFAULT 6,
            "field_goal_points"  INTEGER NOT NULL DEFAULT 3,
            "safety_points"  INTEGER NOT NULL DEFAULT 2,
            "pat_points"  INTEGER NOT NULL DEFAULT 1,
            "pat_defense"  INTEGER NOT NULL DEFAULT 2,
            "pat_safety"  INTEGER NOT NULL DEFAULT 1,
            "players_on_field"  INTEGER NOT NULL DEFAULT 11,
            "xfl_pat"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "preseason_ot_enabled"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "reg_season_ot_enabled"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "postseason_ot_enabled"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,

            "preseason_ot_type"  TEXT DEFAULT "Kansas OT",
            "reg_season_ot_type" TEXT DEFAULT "Kansas OT",
            "postseason_ot_type" TEXT DEFAULT "Kansas OT",

            "two_forward_passes"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "spikes_are_team_stats"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "sacks_are_rushes"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "kneeldowns_are_team_stats"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "kickoff_fc_always_goes_to_touchback"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "kickoffs_enabled"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "use_xfl_kickoff"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "drop_kick_enabled"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "drop_kick_bonus_point"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "fg_adds_ez_length"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "long_fg_bonus_point"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "xp_is_a_fg"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "rouges_enabled"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "punting_enabled"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "onside_punts_enabled"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "fair_catch_enabled"
            INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "special_onside_play_enabled"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            CONSTRAINT "pk_league_id" PRIMARY KEY("league_id")
        );

        CREATE UNIQUE INDEX idx_leagues_id
        ON fb_leagues (league_id);

        INSERT INTO "fb_leagues" (
            "league_id",
            "league_short_name",
            "league_long_name",
            "league_notes"
        )
        VALUES (
            "DEFL",
            "DEFL",
            "DEfault Football League",
            "The default football league for this application."
        );

        """
        return sql_script.replace("        ", "")

    def seasons_sql_file() -> str:
        """
        Returns a SQLite3 script that creates a table that holds data
        for various league's seasons.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a table that holds data
        for various league's seasons.

        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_seasons" (
            "season"                                INT NOT NULL,
            "league_id"                             TEXT NOT NULL,
            "season_notes"                          TEXT,
            "field_length"          INTEGER NOT NULL DEFAULT 100,
            "downs"                  INTEGER NOT NULL DEFAULT 4,
            "first_down_yards"      INTEGER NOT NULL DEFAULT 10,
            "end_zone_length"      INTEGER NOT NULL DEFAULT 10,
            "kickoff_yardline"      INTEGER NOT NULL DEFAULT 35,
            "safety_kick_yardline"  INTEGER NOT NULL DEFAULT 20,
            "kickoff_touchback_yardline"  INTEGER NOT NULL DEFAULT 75,
            "punt_touchback_yardline"      INTEGER NOT NULL DEFAULT 80,
            "normal_touchback_yardline"      INTEGER NOT NULL DEFAULT 80,
            "kansas_ot_yardline"  INTEGER NOT NULL DEFAULT 25,
            "pat_yardline"          INTEGER NOT NULL DEFAULT 3,
            "1PC_yardline"          INTEGER NOT NULL DEFAULT 3,
            "2PC_yardline"          INTEGER NOT NULL DEFAULT 5,
            "3PC_yardline"          INTEGER NOT NULL DEFAULT 10,
            "quarters"              INTEGER NOT NULL DEFAULT 4,
            "timeouts_per_half"      INTEGER NOT NULL DEFAULT 3,
            "ot_period_seconds"      INTEGER NOT NULL DEFAULT 900,
            "game_seconds"          INTEGER NOT NULL DEFAULT 3600,
            "half_seconds"          INTEGER NOT NULL DEFAULT 1800,
            "quarter_seconds"      INTEGER NOT NULL DEFAULT 900,
            "ot_periods"          INTEGER NOT NULL DEFAULT 1,
            "ot_periods_until_shootout"      INTEGER NOT NULL DEFAULT -1,
            "min_xfl_ot_periods"  INTEGER NOT NULL DEFAULT -1,
            "set_xfl_ot_periods"  INTEGER NOT NULL DEFAULT -1,
            "touchdown_points"      INTEGER NOT NULL DEFAULT 6,
            "field_goal_points"      INTEGER NOT NULL DEFAULT 3,
            "safety_points"          INTEGER NOT NULL DEFAULT 2,
            "pat_points"          INTEGER NOT NULL DEFAULT 1,
            "pat_defense"          INTEGER NOT NULL DEFAULT 2,
            "pat_safety"          INTEGER NOT NULL DEFAULT 1,
            "players_on_field"      INTEGER NOT NULL DEFAULT 11,
            "xfl_pat"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "preseason_ot_enabled"
                INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "reg_season_ot_enabled" INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "postseason_ot_enabled" INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,

            "preseason_ot_type" TEXT DEFAULT "Kansas OT",
            "reg_season_ot_type" TEXT DEFAULT "Kansas OT",
            "postseason_ot_type" TEXT DEFAULT "Kansas OT",

            "two_forward_passes"  INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "spikes_are_team_stats"  INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "sacks_are_rushes"      INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "kneeldowns_are_team_stats"
                INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "kickoff_fc_always_goes_to_touchback"
                INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "kickoffs_enabled"      INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "use_xfl_kickoff"      INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "drop_kick_enabled"      INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "drop_kick_bonus_point"  INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "fg_adds_ez_length"      INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "long_fg_bonus_point"  INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "xp_is_a_fg"          INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "rouges_enabled"      INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "punting_enabled"      INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "onside_punts_enabled"  INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            "fair_catch_enabled"  INTEGER NOT NULL DEFAULT 1 COLLATE BINARY,
            "special_onside_play_enabled"
            INTEGER NOT NULL DEFAULT 0 COLLATE BINARY,
            FOREIGN KEY ("league_id")
                REFERENCES "fb_leagues" ("league_id")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
        );

        CREATE UNIQUE INDEX idx_seasons_id
        ON fb_seasons ("season", "league_id");

        INSERT INTO "fb_seasons" ("season","league_id","season_notes")
        VALUES (2023,"DEFL","Default season for the Default Football League."),
            (2022,"DEFL","The 2022 season for the Default Football League."),
            (2021,"DEFL","The 2021 season for the Default Football League."),
            (2020,"DEFL","The 2020 season for the Default Football League."),
            --(2020,"NFL","The 2020 season for the National Football League."),
            (2019,"DEFL","The 2019 season for the Default Football League.");

        """
        return sql_script.replace("        ", "")

    def teams_sql_file() -> str:
        """
        Returns a SQLite3 script that creates a table that holds data
        for various teams.
        In this app, teams are exclusive to specific teams.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a table that holds data
        for various teams.

        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_teams" (
            "season"                INT NOT NULL,
            "league_id"             TEXT NOT NULL,
            "team_id"               TEXT NOT NULL,
            -- Pro Football Reference Team ID (NFL)
            "pfr_team_id"           TEXT,
            -- Pro Football Reference Franchise ID (NFL)
            "pfr_fran_id"           TEXT,
            -- Sports Reference Team ID (CFB)
            "sr_team_id"            TEXT,
            -- NCAA Team ID (stats.ncaa.org team ID)
            "ncaa_team_id"          INT,
            -- Stats Crew Team ID (Various, https://www.statscrew.com/)
            "stats_crew_team_id"    TEXT,
            -- Football Database Team ID (https://www.footballdb.com/)
            "footballdb_team_id"    TEXT,
            -- ESPN Team ID
            "espn_team_id"          INT,
            -- ArenaFan Team ID (https://www.arenafan.com/)
            "arenafan_team_id"      INT,
            "team_abv"              TEXT NOT NULL,
            "team_name"             TEXT NOT NULL,
            "team_location"         TEXT NOT NULL,
            "team_nickname"         TEXT NOT NULL,
            "team_city"             TEXT NOT NULL,
            "team_state"            TEXT NOT NULL,
            "team_nation"           TEXT NOT NULL,
            "team_conference"       TEXT,
            "team_division"         TEXT,
            "team_head_coach"       TEXT,
            "team_oc"               TEXT,
            "team_dc"               TEXT,
            "timezone_name"         TEXT NOT NULL,
            "team_notes"            TEXT,
            "stadium_id"            INT NOT NULL DEFAULT 0,
            FOREIGN KEY ("league_id")
                REFERENCES "fb_leagues" ("league_id")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
        );

        CREATE UNIQUE INDEX idx_teams_id
        ON fb_teams ("season", "league_id","team_id");

        INSERT INTO "fb_teams" (
            "season",
            "league_id",
            "team_id",
            "team_abv",
            "team_name",
            "team_location",
            "team_nickname",
            "team_city",
            "team_state",
            "team_nation",
            "timezone_name",
            "stadium_id"
        )
        VALUES
            (
                2019,
                "DEFL",
                "UGF",
                "UGF",
                "UGF Pandas",
                "University of Georgia-Fairburn",
                "Pandas",
                "Fairburn",
                "US-GA",
                "US",
                "America/New_York",
                1
            ),
            (
                2019,
                "DEFL",
                "DVSU",
                "DVSU",
                "DVSU Dingoes",
                "Death Valley State University",
                "Dingoes",
                "Death Valley",
                "US-NV",
                "US",
                'America/Phoenix',
                2
            ),
            (
                2019,
                "DEFL",
                "RCU",
                "RCU",
                "RCU Moon Men",
                "Rocket City",
                "Moon Men",
                "Huntsville",
                "US-AL",
                "US",
                "America/New_York",
                3
            );

        """
        return sql_script.replace("        ", "")

    def rosters_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table that mostly
        mirrors elements from the `weekly_rosters` dataset from
        `nflverse/nflverse-data`
        (https://github.com/nflverse/nflverse-data/releases/tag/rosters).

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a table that holds data
        for various teams.

        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_rosters"(
            "season"                    INT NOT NULL,
            "league_id"                 TEXT NOT NULL,
            "team_id"                   TEXT NOT NULL,
            "player_id"                 INTEGER PRIMARY KEY AUTOINCREMENT,
            -- Won't be set by a user.
            "position"                  TEXT NOT NULL,
            "depth_chart_position"      TEXT NOT NULL,
            "jersey_number"             INT NOT NULL,
            "status"                    TEXT NOT NULL DEFAULT "ACT",
            "player_full_name"          TEXT NOT NULL,
            /*
            Defaults to the value of "player_first_name",
            but can be set to a differient value
            (for example, Boomer Esiason,
            who's birth name is Norman Esiason,
            you can have his "player_first_name" == "Norman"
            and his "player_football_name" == "Boomer").
            */
            "player_football_name"      TEXT,
            "player_first_name"         TEXT NOT NULL,
            "player_last_name"          TEXT NOT NULL,
            -- SQLite has no internal date/datetime datatype.
            -- Birthdays will be stored as "YYYY-MM-DD".
            "player_bday"               TEXT,
            "height"                    INT, -- Player height, in inches.
            /*
            Calculated before data is inserted,
            this and "height_in" combine to show the player's height.

            For example, if a player is 5'10",
            "height_ft" will be set to `5`,
            "height_in" will be set to `10`,
            and "height" will be `70`.
            */
            "height_ft"                 INT,
            "height_in"                 INT,
            "weight"                    INT, -- Player weight, in lbs.
            "college"                   TEXT,
            "fb_master_player_id"       TEXT, -- Won't be touched by a user.
            "gsis_id"                   TEXT,-- NFL GSIS Player ID.
            "espn_id"                   INT, -- ESPN Player ID.
            "sportradar_id"             TEXT,-- Sportradar Player ID.
            "yahoo_id"                  INT, -- Yahoo Sports Player ID.
            "rotowire_id"               INT, -- Rotowire Player ID.
            -- Pro Football Focus (PFF) Player ID.
            "pff_id"                    INT,
            -- Pro Football Reference Player ID.
            "pfr_id"                    TEXT,
            "fantasy_data_id"           INT,
            "sleeper_id"                INT,
            "esb_id"                    TEXT,
            "smart_id"                  TEXT,
            "sr_player_id"              TEXT,
            "ncaa_player_id"            TEXT, -- stats.ncaa.org Player ID.
            "stats_crew_player_id"      TEXT,
            "footballdb_player_id"      TEXT,
            "arenafan_player_id"        TEXT,
            "years_exp"                 INT,
            "headshot_url"              TEXT,
            "ngs_position"              TEXT,
            -- Here for nflverse compatibility.
            "status_description_abbr"   TEXT,
            /* Can have the following values, and is explained in detail here:
            https://www.the33rdteam.com/category/analysis/how-and-why-the-practice-squad-works/
                -- "A01": Active player.
                -- "E02": Ex/Comm. Perm.
                -- "P01": Practice Squad Player.
                -- "P02": Practice Squad Player, Injured.
                -- "P03": International Practice Squad Player.
                -- "P06": Practice Squad Player, Exception.
                -- "P01": Practice Squad Player, Veteran.
                -- "R01": Reserve/Injured (Injured Reserve).
                -- "R02": Reserve/Retired.
                -- "R03": Reserve/Did Not Report.
                -- "R04": Reserve/Physically Unable to Perform (PUP).
                -- "R05": Reserve/Non-Football Injury
                    (Designation for injuries outside of NFL games/practices).
                -- "R06": Reserve/Left Squad.
                -- "R23": Reserve/Future
                    (If a player has this designation,
                    they are not eligible for games in this season).
                -- "R27": Reserve/Non-Football Illness.
                -- "R30": Reserve/Commissioner Suspension, 1 year.
                -- "R33": Reserve/Club Suspension.
                -- "R40": Reserve/Suspension, less than 1 year.
                -- "R47": Reserve/Non-Football Injury, Designated For Return.
                -- "R48": Reserve/Injured, Designated For Return.
                -- "W03": Waived, no recall.
            */
            -- Year this player finished college,
            -- and/or started playing professionally.
            "entry_year"                INT,
            -- Year this player started playing in this league.
            "rookie_year"               INT,
            FOREIGN KEY ("league_id")
                REFERENCES "fb_leagues" ("league_id")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION,
            FOREIGN KEY ("league_id","season")
                REFERENCES "fb_seasons" ("league_id","season")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION

        );

        CREATE UNIQUE INDEX idx_rosters_id
        ON "fb_rosters" (
            "season",
            "league_id",
            "team_id",
            "jersey_number",
            "player_full_name"
        );

        INSERT INTO
            fb_rosters (
                'season',
                'league_id',
                'team_id',
                'player_id',
                'position',
                'depth_chart_position',
                'jersey_number',
                'status',
                'player_full_name',
                'player_football_name',
                'player_first_name',
                'player_last_name',
                'player_bday',
                'height',
                'height_ft',
                'height_in',
                'weight',
                'college',
                'years_exp',
                'entry_year',
                'rookie_year'
            )
        VALUES
            (
                2019,
                'DEFL',
                'UGF',
                1,
                'QB',
                'QB',
                4,
                'ACT',
                'Will Horton',
                'Will',
                'Will',
                'Horton',
                '1997-09-06',
                73,
                6,
                1,
                242,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                2,
                'QB',
                'QB',
                16,
                'ACT',
                'Howard Cooke',
                'Howard',
                'Howard',
                'Cooke',
                '1990-09-20',
                75,
                6,
                3,
                255,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                3,
                'QB',
                'QB',
                5,
                'ACT',
                'Rodney Calhoun',
                'Rodney',
                'Rodney',
                'Calhoun',
                '2000-07-30',
                75,
                6,
                3,
                216,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                4,
                'RB',
                'RB',
                7,
                'ACT',
                'BJ Hale',
                'BJ',
                'BJ',
                'Hale',
                '1998-04-25',
                73,
                6,
                1,
                229,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                5,
                'RB',
                'RB',
                2,
                'ACT',
                'Ryan Dingle',
                'Ryan',
                'Ryan',
                'Dingle',
                '2001-08-07',
                71,
                5,
                11,
                190,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                6,
                'RB',
                'RB',
                42,
                'ACT',
                'Rob Minton',
                'Rob',
                'Rob',
                'Minton',
                '1995-08-27',
                67,
                5,
                7,
                189,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                7,
                'RB',
                'FB',
                40,
                'ACT',
                'Tom Adamo',
                'Tom',
                'Tom',
                'Adamo',
                '1991-02-08',
                73,
                6,
                1,
                232,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                8,
                'RB',
                'FB',
                39,
                'ACT',
                'Jason Eaton',
                'Jason',
                'Jason',
                'Eaton',
                '2003-08-06',
                72,
                6,
                0,
                236,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                9,
                'RB',
                'RB',
                11,
                'ACT',
                'Elliot Denman',
                'Elliot',
                'Elliot',
                'Denman',
                '1992-08-19',
                73,
                6,
                1,
                180,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                10,
                'WR',
                'WR',
                12,
                'ACT',
                'Neghan Stance',
                'Neghan',
                'Neghan',
                'Stance',
                '1992-06-25',
                74,
                6,
                2,
                209,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                11,
                'WR',
                'WR',
                88,
                'ACT',
                'Torren Engle',
                'Torren',
                'Torren',
                'Engle',
                '1992-09-30',
                72,
                6,
                0,
                175,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                12,
                'WR',
                'WR',
                84,
                'ACT',
                'Vance McMahon',
                'Vance',
                'Vance',
                'McMahon',
                '1998-10-04',
                72,
                6,
                0,
                185,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                13,
                'WR',
                'WR',
                6,
                'ACT',
                'Jake Nelson',
                'Jake',
                'Jake',
                'Nelson',
                '1999-06-27',
                71,
                5,
                11,
                165,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                14,
                'TE',
                'TE',
                18,
                'ACT',
                'Tez Triplett',
                'Tez',
                'Tez',
                'Triplett',
                '1993-10-24',
                76,
                6,
                4,
                233,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                15,
                'TE',
                'TE',
                80,
                'ACT',
                'Nick Riley',
                'Nick',
                'Nick',
                'Riley',
                '1991-09-06',
                75,
                6,
                3,
                219,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                16,
                'TE',
                'TE',
                90,
                'ACT',
                'Ernest Hunter',
                'Ernest',
                'Ernest',
                'Hunter',
                '2003-10-24',
                75,
                6,
                3,
                231,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                17,
                'OL',
                'LT',
                77,
                'ACT',
                'Eric Robinson',
                'Eric',
                'Eric',
                'Robinson',
                '1999-01-07',
                78,
                6,
                6,
                312,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                18,
                'OL',
                'OT',
                71,
                'ACT',
                'Bryce Bass',
                'Bryce',
                'Bryce',
                'Bass',
                '2004-11-22',
                73,
                6,
                1,
                258,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                19,
                'OL',
                'RT',
                55,
                'ACT',
                'Emmitt Rich',
                'Emmitt',
                'Emmitt',
                'Rich',
                '2004-07-29',
                75,
                6,
                3,
                303,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                20,
                'OL',
                'OT',
                64,
                'ACT',
                'Tyson James',
                'Tyson',
                'Tyson',
                'James',
                '1991-01-31',
                75,
                6,
                3,
                287,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                21,
                'OL',
                'RG',
                57,
                'ACT',
                'Brent Tanner',
                'Brent',
                'Brent',
                'Tanner',
                '2003-05-31',
                75,
                6,
                3,
                281,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                22,
                'OL',
                'OG',
                63,
                'ACT',
                'D.D. Henderson',
                'D.D.',
                'D.D.',
                'Henderson',
                '1996-11-04',
                72,
                6,
                0,
                297,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                23,
                'OL',
                'LG',
                72,
                'ACT',
                'J.T. Milton',
                'J.T.',
                'J.T.',
                'Milton',
                '2001-03-20',
                75,
                6,
                3,
                279,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                24,
                'OL',
                'OG',
                59,
                'ACT',
                'Adam Huber',
                'Adam',
                'Adam',
                'Huber',
                '2004-03-09',
                73,
                6,
                1,
                300,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                25,
                'OL',
                'C',
                61,
                'ACT',
                'Bubba Eldrich',
                'Bubba',
                'Bubba',
                'Eldrich',
                '1999-11-22',
                76,
                6,
                4,
                305,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                26,
                'OL',
                'C',
                54,
                'ACT',
                'Saud Bates',
                'Saud',
                'Saud',
                'Bates',
                '2002-10-20',
                70,
                5,
                10,
                284,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                27,
                'DL',
                'LDE',
                89,
                'ACT',
                'LeRoy Singleton',
                'LeRoy',
                'LeRoy',
                'Singleton',
                '1996-08-02',
                76,
                6,
                4,
                249,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                28,
                'DL',
                'RDE',
                91,
                'ACT',
                'Jakari McClelland',
                'Jakari',
                'Jakari',
                'McClelland',
                '2003-08-20',
                72,
                6,
                0,
                248,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                29,
                'DL',
                'DE',
                95,
                'ACT',
                'Eric Jennings',
                'Eric',
                'Eric',
                'Jennings',
                '1992-07-01',
                75,
                6,
                3,
                250,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                30,
                'DL',
                'DE',
                66,
                'ACT',
                'Harrison Hodges',
                'Harrison',
                'Harrison',
                'Hodges',
                '1991-05-17',
                76,
                6,
                4,
                250,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                31,
                'DL',
                'NT',
                87,
                'ACT',
                'Leigh Manley',
                'Leigh',
                'Leigh',
                'Manley',
                '2003-06-13',
                72,
                6,
                0,
                280,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                32,
                'DL',
                'DT',
                98,
                'ACT',
                'D.D. Nixon',
                'D.D.',
                'D.D.',
                'Nixon',
                '1994-04-07',
                77,
                6,
                5,
                273,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                33,
                'DL',
                'DT',
                96,
                'ACT',
                'Eli Griffith',
                'Eli',
                'Eli',
                'Griffith',
                '1994-10-25',
                75,
                6,
                3,
                279,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                34,
                'DL',
                'DT',
                67,
                'ACT',
                'J.T. Benton',
                'J.T.',
                'J.T.',
                'Benton',
                '2005-01-16',
                73,
                6,
                1,
                243,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                35,
                'DL',
                'NG',
                92,
                'ACT',
                'Mike Daley',
                'Mike',
                'Mike',
                'Daley',
                '1992-03-30',
                73,
                6,
                1,
                287,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                36,
                'DL',
                'DT',
                78,
                'ACT',
                'Gabriel Johnson',
                'Gabriel',
                'Gabriel',
                'Johnson',
                '1995-01-07',
                70,
                5,
                10,
                248,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                37,
                'LB',
                'ROLB',
                45,
                'ACT',
                'Harry Bridges',
                'Harry',
                'Harry',
                'Bridges',
                '2004-12-30',
                74,
                6,
                2,
                220,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                38,
                'LB',
                'LOLB',
                50,
                'ACT',
                'Tyler Ruff',
                'Tyler',
                'Tyler',
                'Ruff',
                '1993-08-28',
                73,
                6,
                1,
                227,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                39,
                'LB',
                'EDGE',
                99,
                'ACT',
                'Ira Riley',
                'Ira',
                'Ira',
                'Riley',
                '1992-04-16',
                74,
                6,
                2,
                238,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                40,
                'LB',
                'OLB',
                49,
                'ACT',
                'Donta Erickson',
                'Donta',
                'Donta',
                'Erickson',
                '1996-02-23',
                72,
                6,
                0,
                220,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                41,
                'LB',
                'ILB',
                52,
                'ACT',
                'Eric Tyson',
                'Eric',
                'Eric',
                'Tyson',
                '2001-09-08',
                72,
                6,
                0,
                235,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                42,
                'LB',
                'MLB',
                51,
                'ACT',
                'Elfin Landry',
                'Elfin',
                'Elfin',
                'Landry',
                '2003-07-15',
                72,
                6,
                0,
                231,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                43,
                'DB',
                'RCB',
                37,
                'ACT',
                'Andrew Dale',
                'Andrew',
                'Andrew',
                'Dale',
                '1994-04-07',
                75,
                6,
                3,
                200,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                44,
                'DB',
                'LCB',
                19,
                'ACT',
                'Avery Thompson',
                'Avery',
                'Avery',
                'Thompson',
                '2004-10-13',
                70,
                5,
                10,
                185,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                45,
                'DB',
                'SCB',
                1,
                'ACT',
                'Casey Eaton',
                'Casey',
                'Casey',
                'Eaton',
                '1990-11-16',
                74,
                6,
                2,
                195,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                46,
                'DB',
                'CB',
                46,
                'ACT',
                'Derek Lindsey',
                'Derek',
                'Derek',
                'Lindsey',
                '1997-04-12',
                68,
                5,
                8,
                175,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                47,
                'DB',
                'CB',
                28,
                'ACT',
                'Kareem Huffman',
                'Kareem',
                'Kareem',
                'Huffman',
                '1991-07-16',
                68,
                5,
                8,
                177,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                48,
                'DB',
                'CB',
                24,
                'ACT',
                'Jimmie Ricks',
                'Jimmie',
                'Jimmie',
                'Ricks',
                '1997-03-12',
                67,
                5,
                7,
                160,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                49,
                'DB',
                'FS',
                26,
                'ACT',
                'Benny Preston',
                'Benny',
                'Benny',
                'Preston',
                '1994-01-04',
                73,
                6,
                1,
                180,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                50,
                'DB',
                'SAF',
                23,
                'ACT',
                'Keenan Manning',
                'Keenan',
                'Keenan',
                'Manning',
                '1992-11-25',
                73,
                6,
                1,
                185,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                51,
                'DB',
                'SS',
                34,
                'ACT',
                'Buck Poole',
                'Buck',
                'Buck',
                'Poole',
                '2002-01-04',
                71,
                5,
                11,
                188,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                52,
                'DB',
                'SAF',
                48,
                'ACT',
                'Kendal Huber',
                'Kendal',
                'Kendal',
                'Huber',
                '1991-04-10',
                70,
                5,
                10,
                189,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                53,
                'SPEC',
                'K',
                38,
                'ACT',
                'Andy Francis',
                'Andy',
                'Andy',
                'Francis',
                '2005-05-17',
                73,
                6,
                1,
                170,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                54,
                'SPEC',
                'K',
                62,
                'ACT',
                'Rex Johnson',
                'Rex',
                'Rex',
                'Johnson',
                '2001-05-27',
                73,
                6,
                1,
                175,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                55,
                'SPEC',
                'P',
                69,
                'ACT',
                'Jacob Rigdon',
                'Jacob',
                'Jacob',
                'Rigdon',
                '2003-03-08',
                72,
                6,
                0,
                180,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                56,
                'SPEC',
                'P',
                65,
                'ACT',
                'Stephen Washington',
                'Stephen',
                'Stephen',
                'Washington',
                '2004-03-15',
                75,
                6,
                3,
                185,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                57,
                'SPEC',
                'LS',
                14,
                'ACT',
                'Legwarmer Smith',
                'Legwarmer',
                'Legwarmer',
                'Smith',
                '2001-12-08',
                72,
                6,
                0,
                180,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'UGF',
                58,
                'SPEC',
                'LS',
                56,
                'ACT',
                'Triple Parakeet-Shoes',
                'Triple',
                'Triple',
                'Parakeet-Shoes',
                '2000-07-26',
                72,
                6,
                0,
                181,
                'UGF',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                59,
                'QB',
                'QB',
                19,
                'ACT',
                'Micheal Wilson',
                'Micheal',
                'Micheal',
                'Wilson',
                '1999-10-23',
                74,
                6,
                2,
                206,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                60,
                'QB',
                'QB',
                18,
                'ACT',
                'Antwon Goodwin',
                'Antwon',
                'Antwon',
                'Goodwin',
                '1998-10-01',
                74,
                6,
                2,
                198,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                61,
                'QB',
                'QB',
                1,
                'ACT',
                'JT Martinez',
                'JT',
                'JT',
                'Martinez',
                '1992-03-30',
                73,
                6,
                1,
                200,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                62,
                'QB',
                'QB',
                5,
                'ACT',
                'Travis Wood',
                'Travis',
                'Travis',
                'Wood',
                '1998-06-24',
                76,
                6,
                4,
                219,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                63,
                'RB',
                'RB',
                21,
                'ACT',
                'Matt Morrow',
                'Matt',
                'Matt',
                'Morrow',
                '1992-09-06',
                70,
                5,
                10,
                199,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                64,
                'RB',
                'RB',
                2,
                'ACT',
                'Zach Thompson',
                'Zach',
                'Zach',
                'Thompson',
                '1999-05-29',
                70,
                5,
                10,
                196,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                65,
                'RB',
                'RB',
                30,
                'ACT',
                'Jamie James',
                'Jamie',
                'Jamie',
                'James',
                '1995-07-01',
                70,
                5,
                10,
                204,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                66,
                'RB',
                'RB',
                41,
                'ACT',
                'Terence Wall',
                'Terence',
                'Terence',
                'Wall',
                '1992-10-27',
                70,
                5,
                10,
                210,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                67,
                'RB',
                'RB',
                12,
                'ACT',
                'Tre Eaton',
                'Tre',
                'Tre',
                'Eaton',
                '1991-11-17',
                68,
                5,
                8,
                190,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                68,
                'RB',
                'FB',
                49,
                'ACT',
                'Perry Samuels',
                'Perry',
                'Perry',
                'Samuels',
                '2001-07-15',
                74,
                6,
                2,
                225,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                69,
                'RB',
                'FB',
                29,
                'ACT',
                'Chip Godsey',
                'Chip',
                'Chip',
                'Godsey',
                '2001-12-12',
                76,
                6,
                4,
                215,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                70,
                'RB',
                'FB',
                25,
                'ACT',
                'Kellen West',
                'Kellen',
                'Kellen',
                'West',
                '1997-03-11',
                71,
                5,
                11,
                200,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                71,
                'WR',
                'WR',
                3,
                'ACT',
                'Seth McKenna',
                'Seth',
                'Seth',
                'McKenna',
                '2003-11-20',
                67,
                5,
                7,
                170,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                72,
                'WR',
                'WR',
                80,
                'ACT',
                'Richard Boulder',
                'Richard',
                'Richard',
                'Boulder',
                '2004-12-11',
                71,
                5,
                11,
                180,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                73,
                'WR',
                'WR',
                85,
                'ACT',
                'Brady Miller',
                'Brady',
                'Brady',
                'Miller',
                '1993-11-09',
                74,
                6,
                2,
                220,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                74,
                'WR',
                'WR',
                47,
                'ACT',
                'Alex King',
                'Alex',
                'Alex',
                'King',
                '1994-02-23',
                74,
                6,
                2,
                220,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                75,
                'WR',
                'WR',
                84,
                'ACT',
                'Jacob Hill',
                'Jacob',
                'Jacob',
                'Hill',
                '2000-11-20',
                73,
                6,
                1,
                196,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                76,
                'WR',
                'WR',
                34,
                'ACT',
                'Estman Gorman',
                'Estman',
                'Estman',
                'Gorman',
                '1992-01-11',
                72,
                6,
                0,
                175,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                77,
                'TE',
                'TE',
                81,
                'ACT',
                'Grankie Gandy',
                'Grankie',
                'Grankie',
                'Gandy',
                '2001-05-03',
                74,
                6,
                2,
                236,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                78,
                'TE',
                'TE',
                86,
                'ACT',
                'Bernard Gill',
                'Bernard',
                'Bernard',
                'Gill',
                '1991-04-12',
                71,
                5,
                11,
                191,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                79,
                'OL',
                'LT',
                72,
                'ACT',
                'Patrick Boulware',
                'Patrick',
                'Patrick',
                'Boulware',
                '1995-11-15',
                78,
                6,
                6,
                270,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                80,
                'OL',
                'RT',
                52,
                'ACT',
                'Benji Odom',
                'Benji',
                'Benji',
                'Odom',
                '1996-02-29',
                78,
                6,
                6,
                264,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                81,
                'OL',
                'OT',
                68,
                'ACT',
                'Deshon Haley',
                'Deshon',
                'Deshon',
                'Haley',
                '1991-06-13',
                78,
                6,
                6,
                287,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                82,
                'OL',
                'OT',
                75,
                'ACT',
                'C.J. Rozner',
                'C.J.',
                'C.J.',
                'Rozner',
                '1996-08-09',
                78,
                6,
                6,
                278,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                83,
                'OL',
                'OT',
                70,
                'ACT',
                'Bobby Giles',
                'Bobby',
                'Bobby',
                'Giles',
                '2004-02-11',
                77,
                6,
                5,
                287,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                84,
                'OL',
                'OT',
                64,
                'ACT',
                'Davon Snyder',
                'Davon',
                'Davon',
                'Snyder',
                '1993-08-11',
                75,
                6,
                3,
                239,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                85,
                'OL',
                'RG',
                78,
                'ACT',
                'Jermaine Hodges',
                'Jermaine',
                'Jermaine',
                'Hodges',
                '2004-02-18',
                75,
                6,
                3,
                261,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                86,
                'OL',
                'LG',
                62,
                'ACT',
                'Aaron White',
                'Aaron',
                'Aaron',
                'White',
                '1997-02-21',
                76,
                6,
                4,
                317,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                87,
                'OL',
                'OG',
                67,
                'ACT',
                'Errick Humphrey',
                'Errick',
                'Errick',
                'Humphrey',
                '1991-03-29',
                76,
                6,
                4,
                306,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                88,
                'OL',
                'OG',
                58,
                'ACT',
                'Blake Klein',
                'Blake',
                'Blake',
                'Klein',
                '2001-09-19',
                78,
                6,
                6,
                255,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                89,
                'OL',
                'C',
                63,
                'ACT',
                'Matt Hampton',
                'Matt',
                'Matt',
                'Hampton',
                '1995-05-13',
                74,
                6,
                2,
                240,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                90,
                'OL',
                'C',
                71,
                'ACT',
                'Reshard Boone',
                'Reshard',
                'Reshard',
                'Boone',
                '1999-09-28',
                73,
                6,
                1,
                265,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                91,
                'DL',
                'LDE',
                92,
                'ACT',
                'Brylan Down',
                'Brylan',
                'Brylan',
                'Down',
                '2004-11-30',
                74,
                6,
                2,
                228,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                92,
                'DL',
                'RDE',
                93,
                'ACT',
                'Dom Atamo',
                'Dom',
                'Dom',
                'Atamo',
                '2001-08-27',
                74,
                6,
                2,
                235,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                93,
                'DL',
                'DE',
                99,
                'ACT',
                'Nolan Poole',
                'Nolan',
                'Nolan',
                'Poole',
                '2003-01-07',
                75,
                6,
                3,
                259,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                94,
                'DL',
                'DE',
                96,
                'ACT',
                'Del Smith',
                'Del',
                'Del',
                'Smith',
                '1998-01-03',
                78,
                6,
                6,
                250,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                95,
                'DL',
                'DE',
                48,
                'ACT',
                'Wesley Stamps',
                'Wesley',
                'Wesley',
                'Stamps',
                '2001-10-30',
                76,
                6,
                4,
                243,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                96,
                'DL',
                'DT',
                95,
                'ACT',
                'Joe Walker',
                'Joe',
                'Joe',
                'Walker',
                '1999-09-06',
                74,
                6,
                2,
                238,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                97,
                'DL',
                'DT',
                91,
                'ACT',
                'Sammy Sam',
                'Sammy',
                'Sammy',
                'Sam',
                '2001-01-03',
                75,
                6,
                3,
                260,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                98,
                'DL',
                'DT',
                65,
                'ACT',
                'Nathan McKee',
                'Nathan',
                'Nathan',
                'McKee',
                '1999-03-04',
                76,
                6,
                4,
                253,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                99,
                'DL',
                'DT',
                61,
                'ACT',
                'Doug Campers',
                'Doug',
                'Doug',
                'Campers',
                '1994-08-18',
                74,
                6,
                2,
                253,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                100,
                'LB',
                'OLB',
                73,
                'ACT',
                'Neil Krause',
                'Neil',
                'Neil',
                'Krause',
                '1992-04-25',
                73,
                6,
                1,
                195,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                101,
                'LB',
                'OLB',
                56,
                'ACT',
                'Oliver McIntyre',
                'Oliver',
                'Oliver',
                'McIntyre',
                '1999-04-23',
                72,
                6,
                0,
                206,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                102,
                'LB',
                'EDGE',
                98,
                'ACT',
                'Johnnie Barr',
                'Johnnie',
                'Johnnie',
                'Barr',
                '1994-10-17',
                72,
                6,
                0,
                211,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                103,
                'LB',
                'EDGE',
                94,
                'ACT',
                'Abdul Young',
                'Abdul',
                'Abdul',
                'Young',
                '1994-05-05',
                73,
                6,
                1,
                222,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                104,
                'LB',
                'LB',
                45,
                'ACT',
                'Samuel Schneider',
                'Samuel',
                'Samuel',
                'Schneider',
                '1990-10-17',
                73,
                6,
                1,
                214,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                105,
                'LB',
                'MLB',
                55,
                'ACT',
                'DD Rodgers',
                'DD',
                'DD',
                'Rodgers',
                '2002-07-08',
                74,
                6,
                2,
                217,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                106,
                'LB',
                'ILB',
                55,
                'ACT',
                'Will Hughes',
                'Will',
                'Will',
                'Hughes',
                '1999-03-23',
                74,
                6,
                2,
                220,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                107,
                'LB',
                'ILB',
                43,
                'ACT',
                'Cooper Stevenson',
                'Cooper',
                'Cooper',
                'Stevenson',
                '2001-02-04',
                73,
                6,
                1,
                213,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                108,
                'LB',
                'LB',
                87,
                'ACT',
                'Grant Eaton',
                'Grant',
                'Grant',
                'Eaton',
                '1991-11-03',
                73,
                6,
                1,
                225,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                109,
                'DB',
                'LCB',
                24,
                'ACT',
                'Bill Dingle',
                'Bill',
                'Bill',
                'Dingle',
                '2001-12-08',
                69,
                5,
                9,
                180,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                110,
                'DB',
                'RCB',
                39,
                'ACT',
                'Jeremy Jimmy',
                'Jeremy',
                'Jeremy',
                'Jimmy',
                '2000-11-22',
                72,
                6,
                0,
                180,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                111,
                'DB',
                'NCB',
                4,
                'ACT',
                'DeAngelo Woodard',
                'DeAngelo',
                'DeAngelo',
                'Woodard',
                '1994-06-02',
                72,
                6,
                0,
                185,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                112,
                'DB',
                'DCB',
                46,
                'ACT',
                'Lemarcus Parsons',
                'Lemarcus',
                'Lemarcus',
                'Parsons',
                '1997-09-09',
                71,
                5,
                11,
                175,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                113,
                'DB',
                'FS',
                36,
                'ACT',
                'Jesse Shelton',
                'Jesse',
                'Jesse',
                'Shelton',
                '2004-08-25',
                74,
                6,
                2,
                190,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                114,
                'DB',
                'SAF',
                23,
                'ACT',
                'Chris Hickmon',
                'Chris',
                'Chris',
                'Hickmon',
                '1998-01-23',
                74,
                6,
                2,
                199,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                115,
                'DB',
                'SS',
                31,
                'ACT',
                'Timothy Dickens',
                'Timothy',
                'Timothy',
                'Dickens',
                '1996-08-24',
                74,
                6,
                2,
                194,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                116,
                'DB',
                'SAF',
                26,
                'ACT',
                'LaShaun Gutierrez',
                'LaShaun',
                'LaShaun',
                'Gutierrez',
                '1995-08-26',
                71,
                5,
                11,
                191,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                117,
                'SPEC',
                'K',
                17,
                'ACT',
                'Justin Powell',
                'Justin',
                'Justin',
                'Powell',
                '1999-01-04',
                70,
                5,
                10,
                209,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                118,
                'SPEC',
                'P',
                69,
                'ACT',
                'Rob Butler',
                'Rob',
                'Rob',
                'Butler',
                '2002-11-12',
                73,
                6,
                1,
                195,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                119,
                'SPEC',
                'LS',
                79,
                'ACT',
                'Velociraptor Maloish',
                'Velociraptor',
                'Scoish',
                'Maloish',
                '1999-11-25',
                0,
                NULL,
                NULL,
                NULL,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                120,
                'SPEC',
                'LS',
                83,
                'ACT',
                'Aristokles Prabhu',
                'Aristokles',
                'Aristokles',
                'Prabhu',
                '2005-03-18',
                0,
                NULL,
                NULL,
                NULL,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                121,
                'SPEC',
                'K',
                15,
                'ACT',
                'Legume Druprix',
                'Legume',
                'Legume',
                'Druprix',
                '1997-03-22',
                72,
                6,
                0,
                191,
                'DVSU',
                0,
                2019,
                2019
            ),
            (
                2019,
                'DEFL',
                'DVSU',
                122,
                'SPEC',
                'P',
                20,
                'ACT',
                'Creme De La Creme',
                'Creme',
                'Creme',
                'De La Creme',
                '2003-04-15',
                0,
                NULL,
                NULL,
                NULL,
                'DVSU',
                0,
                2019,
                2019
            );
        """
        return sql_script.replace("        ", "")

    def stadiums_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table
        that houses stadium information.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that creates a table that holds data
        for various teams.

        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_stadiums"(
            "stadium_id"            INTEGER PRIMARY KEY AUTOINCREMENT,
            -- Set to `???` if the stadium has no
            -- designated home team for some reason.
            "team_id"               TEXT NOT NULL,
            "pfr_stadium_id"        TEXT,
            "stadium_name"          TEXT NOT NULL,
            "stadium_capacity"      INT NOT NULL,
            "stadium_city"          TEXT NOT NULL,
            "stadium_state"         TEXT NOT NULL, -- ISO 3166-2 Code
            "stadium_nation"        TEXT NOT NULL, -- ISO 3 Letter code
            "is_dome"               BOOLEAN DEFAULT FALSE NOT NULL,
            -- If a stadium has a retractable roof,
            -- this and "is_dome" are set to TRUE.
            "is_retractable_roof"   BOOLEAN DEFAULT FALSE NOT NULL,
            "stadium_plus_code"     TEXT,
            "stadium_elevation_ft"  INT,
            "stadium_elevation_m"   INT,
            "stadium_timezone"      TEXT NOT NULL,
            "stadium_location_x"    FLOAT, -- Longitude
            "stadium_location_y"    FLOAT -- Latitude
        );

        CREATE UNIQUE INDEX idx_stadiums_id
        ON "fb_stadiums" ("stadium_id","team_id");

        INSERT INTO fb_stadiums(
            stadium_id,
            team_id,
            pfr_stadium_id,
            stadium_name,
            stadium_capacity,
            stadium_city,
            stadium_state,
            stadium_nation,
            is_dome,
            is_retractable_roof,
            stadium_timezone
        )
        VALUES
            (
                0,
                '---',
                NULL,
                'Default Stadium',
                50000,
                'Cincinnati',
                'US-OH',
                'USA',
                FALSE,
                FALSE,
                'America/Kentucky/Louisville'
            )
            ,(
                1,
                'UGF',
                NULL,
                'Adamo Dome',
                50000,
                'Fairburn',
                'US-GA',
                'USA',
                TRUE,
                FALSE,
                'America/New_York'
            )
            ,(
                2,
                'DVSU',
                NULL,
                'Hale Kitchen',
                10000,
                'Death Valley',
                'US-NV',
                'USA',
                FALSE,
                FALSE,
                'America/Phoenix'
            )
            ,(
                3,
                'RCU',
                NULL,
                'Apollo Field',
                30000,
                'Huntsville',
                'US-AL',
                'USA',
                FALSE,
                FALSE,
                'America/New_York'
            );

        """
        return sql_script.replace("        ", "")

    def weekly_rosters_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table that mostly
        mirrors the `weekly_rosters` dataset from `nflverse/nflverse-data`
        (https://github.com/nflverse/nflverse-data/releases/tag/weekly_rosters).

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that generates a SQLite3 table that mostly
        mirrors the `weekly_rosters` dataset from `nflverse/nflverse-data`.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS 'fb_weekly_rosters'(
            'season'                    INT NOT NULL,
            'game_id'                   INT NOT NULL,
            'league_id'                 TEXT NOT NULL,
            'team_id'                   TEXT NOT NULL,
            'team_abv'                  TEXT NOT NULL,
            -- Won't be set by a user.
            'position'                  TEXT NOT NULL,
            'depth_chart_position'      TEXT NOT NULL,
            -- TEXT so a player can be identified by
            -- '00', '01', '1A', or '1O'/'1D'
            'jersey_number'             TEXT NOT NULL,
            'status'                    TEXT NOT NULL,
            'player_full_name'          TEXT NOT NULL,
            /*
            Defaults to the value of 'player_first_name',
            but can be set to a differient value
            (for example, Boomer Esiason, who's birth name is Norman Esiason,
            can have his 'player_first_name' == 'Norman',
            and his 'player_football_name' == 'Boomer').
            */
            'player_football_name'      TEXT,
            'player_first_name'         TEXT NOT NULL,
            'player_last_name'          TEXT NOT NULL,
            -- SQLite has no internal date/datetime datatype.
            -- Birthdays will be stored as 'YYYY-MM-DD'.
            'player_bday'               TEXT,
            'height'                    INT, -- Player height, in inches
            /*
            Calculated before data is inserted,
            this and 'height_in' combine to show the player's height.
            For example, if a player is 5'10',
            'height_ft' will be set to `5`,
            'height_in' will be set to `10`,
            and 'height' will be `70`.
            */
            'height_ft'                 INT,
            'height_in'                 INT,
            'weight'                    INT, -- Player weight, in lbs.
            'college'                   TEXT,
            'gsis_id'                   TEXT,-- NFL GSIS Player ID.
            'espn_id'                   INT, -- ESPN Player ID.
            'sportradar_id'             TEXT,-- Sportradar Player ID.
            'yahoo_id'                  INT, -- Yahoo Sports Player ID.
            'rotowire_id'               INT, -- Rotowire Player ID.
            -- Pro Football Focus (PFF) Player ID.
            'pff_id'                    INT,
            -- Pro Football Reference Player ID.
            'pfr_id'                    TEXT,
            'fantasy_data_id'           INT,
            'sleeper_id'                INT,
            'years_exp'                 INT NOT NULL,
            -- Letting users modify this is potentially a bad idea.
            -- Only here for nflverse compatibility.
            'headshot_url'              TEXT,
            'headshot_image'            BLOB,
            -- Only here for nflverse compatibility.
            'ngs_position'              TEXT,
            'week'                      INT NOT NULL,
            -- can be 'PRE', 'REG', or 'POST'.
            -- Optionally, postseason games can be represented by
            -- > 'WC' (wild card)
            -- > 'DIV' (divisional round)
            -- > 'CON' (conference championship)
            -- > 'SB' (Super Bowl)
            'game_type'                 TEXT NOT NULL,
            -- Here for nflverse compatibility.
            'status_description_abbr'   TEXT,
            /*
            Can have the following values, and is explained in detail here:
            https://www.the33rdteam.com/category/analysis/how-and-why-the-practice-squad-works/
                -- 'A01': Active player.
                -- 'E02': Ex/Comm. Perm.
                -- 'P01': Practice Squad Player.
                -- 'P02': Practice Squad Player, Injured.
                -- 'P03': International Practice Squad Player.
                -- 'P06': Practice Squad Player, Exception.
                -- 'P01': Practice Squad Player, Veteran.
                -- 'R01': Reserve/Injured (Injured Reserve).
                -- 'R02': Reserve/Retired.
                -- 'R03': Reserve/Did Not Report.
                -- 'R04': Reserve/Physically Unable to Perform (PUP).
                -- 'R05': Reserve/Non-Football Injury
                    (Designation for injuries outside of NFL games/practices).
                -- 'R06': Reserve/Left Squad.
                -- 'R23': Reserve/Future
                    (If a player has this designation,
                    they are not eligible for games in this season).
                -- 'R27': Reserve/Non-Football Illness.
                -- 'R30': Reserve/Commissioner Suspension, 1 year.
                -- 'R33': Reserve/Club Suspension.
                -- 'R40': Reserve/Suspension, less than 1 year.
                -- 'R47': Reserve/Non-Football Injury, Designated For Return.
                -- 'R48': Reserve/Injured, Designated For Return.
                -- 'W03': Waived, no recall.
            */
            'esb_id'                    TEXT,
            'smart_id'                  TEXT,
            -- Year this player finished college,
            -- and/or started playing professionally.
            'entry_year'                INT,
            -- Year this player started playing in this league.
            'rookie_year'               INT

        );

        CREATE UNIQUE INDEX idx_weekly_rosters_id
        ON 'fb_weekly_rosters' (
            'season',
            'league_id',
            'team_id',
            'jersey_number',
            'player_full_name',
            'week',
            'game_type'
        );


    INSERT_INTO fb_weekly_rosters (
        "season",
        "game_id",
        "league_id",
        "team_id",
        "team_abv",
        "position",
        "depth_chart_position",
        "jersey_number",
        "status",
        "player_full_name",
        "player_football_name",
        "player_first_name",
        "player_last_name",
        "player_bday",
        "height",
        "height_ft",
        "height_in",
        "weight",
        "college",
        "years_exp",
        "week",
        "game_type",
        "entry_year",
        "rookie_year"
    )
    VALUES
        (2019,1,'DEFL','UGF','UGF','QB','QB',4,'Active',
            'Will Horton','Will','Will','Horton','9/6/1997',
            73,6,1,242,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','QB','QB',16,'Active',
            'Howard Cooke','Howard','Howard','Cooke','9/20/1990',
            75,6,3,255,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','QB','QB',5,'Active',
            'Rodney Calhoun','Rodney','Rodney','Calhoun','7/30/2000',
            75,6,3,216,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','RB','RB',7,'Active',
            'BJ Hale','BJ','Brian','Hale','4/25/1998',
            73,6,1,229,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','RB','RB',2,'Active',
            'Ryan Dingle','Ryan','Ryan','Dingle','8/7/2001',
            71,5,11,190,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','RB','RB',42,'Active',
            'Rob Minton','Rob','Rob','Minton','8/27/1995',
            67,5,7,189,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','RB','FB',40,'Active',
            'Tom Adamo','Tom','Tom','Adamo','2/8/1991',
            73,6,1,232,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','RB','FB',39,'Active',
            'Jason Eaton','Jason','Jason','Eaton','8/6/2003',
            72,6,0,236,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','WR','WR',11,'Active',
            'Elliot Denman','Elliot','Elliot','Denman','8/19/1992',
            73,6,1,180,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','WR','WR',12,'Active',
            'Neghan Stance','Neghan','Neghan','Stance','6/25/1992',
            74,6,2,209,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','WR','WR',88,'Active',
            'Torren Engle','Torren','Torren','Engle','9/30/1992',
            72,6,0,175,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','WR','WR',84,'Active',
            'Vance McMahon','Vance','Vance','McMahon','10/4/1998',
            72,6,0,185,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','WR','WR',6,'Active',
            'Jake Nelson','Jake','Jake','Nelson','6/27/1999',
            71,5,11,165,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','TE','TE',18,'Active',
            'Tez Triplett','Tez','Tez','Triplett','10/24/1993',
            76,6,4,233,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','TE','TE',80,'Active',
            'Nick Riley','Nick','Nick','Riley','9/6/1991',
            75,6,3,219,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','TE','TE',90,'Active',
            'Ernest Hunter','Ernest','Ernest','Hunter','10/24/2003',
            75,6,3,231,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','LT',77,'Active',
            'Eric Robinson','Eric','Eric','Robinson','1/7/1999',
            78,6,6,312,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','OT',71,'Active',
            'Bryce Bass','Bryce','Bryce','Bass','11/22/2004',
            73,6,1,258,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','RT',55,'Active',
            'Emmitt Rich','Emmitt','Emmitt','Rich','7/29/2004',
            75,6,3,303,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','OT',64,'Active',
            'Tyson James','Tyson','Tyson','James','1/31/1991',
            75,6,3,287,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','RG',57,'Active',
            'Brent Tanner','Brent','Brent','Tanner','5/31/2003',
            75,6,3,281,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','OG',63,'Active',
            'D.D. Henderson','D.D.','Dave','Henderson','11/4/1996',
            72,6,0,297,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','LG',72,'Active',
            'J.T. Milton','J.T.','Jeff','Milton','3/20/2001',
            75,6,3,279,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','OG',59,'Active',
            'Adam Huber','Adam','Adam','Huber','3/9/2004',
            73,6,1,300,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','C',61,'Active',
            'Bubba Eldridge','Bubba','Bubba','Eldridge','11/22/1999',
            76,6,4,305,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','OL','C',54,'Active',
            'Shaud Bates','Shaud','Shaud','Bates','10/20/2002',
            70,5,10,284,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','LDE',89,'Active',
            'LeRoy Singleton','LeRoy','LeRoy','Singleton','8/2/1996',
            76,6,4,249,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','RDE',91,'Active',
            'Jakari McClelland','Jakari','Jakari','McClelland','8/20/2003',
            72,6,0,248,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','DE',95,'Active',
            'Eric Jennings','Eric','Eric','Jennings','7/1/1992',
            75,6,3,250,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','DE',66,'Active',
            'Harrison Hodges','Harrison','Harrison','Hodges','5/17/1991',
            76,6,4,250,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','NT',87,'Active',
            'Leigh Manley','Leigh','Leigh','Manley','6/13/2003',
            72,6,0,280,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','DT',98,'Active',
            'D.D. Nixon','D.D.','Dent','Nixon','4/7/1994',
            77,6,5,273,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','DT',96,'Active',
            'Eli Griffith','Eli','Eli','Griffith','10/25/1994',
            75,6,3,279,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','DT',67,'Active',
            'J.T. Benton','J.T.','John','Benton','1/16/2005',
            73,6,1,243,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','NG',92,'Active',
            'Mike Dailey','Mike','Mike','Dailey','3/30/1992',
            73,6,1,287,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DL','DT',78,'Active',
            'Gabriel Johnson','Gabriel','Gabriel','Johnson','1/7/1995',
            70,5,10,248,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','LB','ROLB',45,'Active',
            'Harry Bridges','Harry','Harry','Bridges','12/30/2004',
            74,6,2,220,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','LB','LOLB',50,'Active',
            'Tyler Ruff','Tyler','Tyler','Ruff','8/28/1993',
            73,6,1,227,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','LB','EDGE',99,'Active',
            'Ira Riley','Ira','Ira','Riley','4/16/1992',
            74,6,2,238,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','LB','OLB',49,'Active',
            'Donta Erickson','Donta','Donta','Erickson','2/23/1996',
            72,6,0,220,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','LB','ILB',52,'Active',
            'Eric Tyson','Eric','Eric','Tyson','9/8/2001',
            72,6,0,235,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','LB','MLB',51,'Active',
            'Elgin Landry','Elgin','Elgin','Landry','7/15/2003',
            72,6,0,231,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','RCB',37,'Active',
            'Andrew Dale','Andrew','Andrew','Dale','4/7/1994',
            75,6,3,200,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','LCB',19,'Active',
            'Avery Thompson','Avery','Avery','Thompson','10/13/2004',
            70,5,10,185,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','SCB',1,'Active',
            'Casey Eaton','Casey','Casey','Eaton','11/16/1990',
            74,6,2,195,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','CB',46,'Active',
            'Derek Lindsey','Derek','Derek','Lindsey','4/12/1997',
            68,5,8,175,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','CB',28,'Active',
            'Kareem Huffman','Kareem','Kareem','Huffman','7/16/1991',
            68,5,8,177,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','CB',24,'Active',
            'Jimmie Ricks','Jimmie','Jimmie','Ricks','3/12/1997',
            67,5,7,160,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','FS',26,'Active',
            'Benny Preston','Benny','Benny','Preston','1/4/1994',
            73,6,1,180,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','SAF',23,'Active',
            'Keenan Manning','Keenan','Keenan','Manning','11/25/1992',
            73,6,1,185,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','SS',34,'Active',
            'Buck Poole','Buck','Buck','Poole','1/4/2002',
            71,5,11,188,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','DB','SAF',48,'Active',
            'Kendal Huber','Kendal','Kendal','Huber','4/10/1991',
            70,5,10,189,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','SPEC','K',38,'Active',
            'Andy Francis','Andy','Andy','Francis','5/17/2005',
            73,6,1,170,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','SPEC','K',62,'Active',
            'Rex Johnson','Rex','Rex','Johnson','5/27/2001',
            73,6,1,175,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','SPEC','P',69,'Active',
            'Jacob Rigdon','Jacob','Jacob','Rigdon','3/8/2003',
            72,6,0,180,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','SPEC','P',65,'Active',
            'Stephen Washington','Stephen','Stephen','Washington','3/15/2004',
            75,6,3,185,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','SPEC','LS',14,'Active',
            'Logjammer D''Baggagecling','Logjammer','Logjammer','Baggagecling',
            '12/8/2001',72,6,0,180,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','UGF','UGF','SPEC','LS',56,'Active',
            'Triple Parakeet-Shoes',
            'Triple','Triple','Parakeet-Shoes','7/26/2000',
            72,6,0,181,'UGF',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','QB','QB',19,'Active',
            'Micheal Wilson','Micheal','Micheal','Wilson','10/23/1999',
            74,6,2,206,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','QB','QB',18,'Active',
            'Antwon Goodwin','Antwon','Antwon','Goodwin','10/1/1998',
            74,6,2,198,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','QB','QB',1,'Active',
            'JT Martinez','JT','John','Martinez','3/30/1992',
            73,6,1,200,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','QB','QB',5,'Active',
            'Travis Wood','Travis','Travis','Wood','6/24/1998',
            76,6,4,219,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','RB',21,'Active',
            'Matt Morrow','Matt','Matt','Morrow','9/6/1992',
            70,5,10,199,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','RB',2,'Active',
            'Zach Thompson','Zach','Zach','Thompson','5/29/1999',
            70,5,10,196,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','RB',30,'Active',
            'Jamie James','Jamie','Jamie','James','7/1/1995',
            70,5,10,204,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','RB',41,'Active',
            'Terence Wall','Terence','Terence','Wall','10/27/1992',
            70,5,10,210,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','RB',12,'Active',
            'Tre Eaton','Tre','Tre','Eaton','11/17/1991',
            68,5,8,190,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','FB',49,'Active',
            'Perry Samuels','Perry','Perry','Samuels','7/15/2001',
            74,6,2,225,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','FB',29,'Active',
            'Chip Godsey','Chip','Chip','Godsey','12/12/2001',
            76,6,4,215,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','RB','FB',25,'Active',
            'Kellen West','Kellen','Kellen','West','3/11/1997',
            71,5,11,200,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','WR','WR',3,'Active',
            'Seth McKenna','Seth','Seth','McKenna','11/20/2003',
            67,5,7,170,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','WR','WR',80,'Active',
            'Richard Boulder','Richard','Richard','Boulder','12/11/2004',
            71,5,11,180,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','WR','WR',85,'Active',
            'Brady Millar','Brady','Brady','Millar','11/9/1993',
            74,6,2,220,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','WR','WR',47,'Active',
            'Alex King','Alex','Alex','King','2/23/1994',
            74,6,2,220,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','WR','WR',84,'Active',
            'Jacob Hill','Jacob','Jacob','Hill','11/20/2000',
            73,6,1,196,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','WR','WR',34,'Active',
            'Estman Gorman','Estman','Estman','Gorman','1/11/1992',
            72,6,0,175,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','TE','TE',81,'Active',
            'Grankie Gandy','Grankie','Grankie','Gandy','5/3/2001',
            74,6,2,236,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','TE','TE',86,'Active',
            'Bernard Gill','Bernard','Bernard','Gill','4/12/1991',
            71,5,11,191,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','LT',72,'Active',
            'Patrick Boulware','Patrick','Patrick','Boulware','11/15/1995',
            78,6,6,270,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','RT',52,'Active',
            'Benji Odom','Benji','Benji','Odom','2/29/1996',
            78,6,6,264,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','OT',68,'Active',
            'Deshon Haley','Deshon','Deshon','Haley','6/13/1991',
            78,6,6,287,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','OT',75,'Active',
            'C.J. Rozner','C.J.','Chris','Rozner','8/9/1996',
            78,6,6,278,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','OT',70,'Active',
            'Bobby Giles','Bobby','Bobby','Giles','2/11/2004',
            77,6,5,287,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','OT',64,'Active',
            'Davon Snyder','Davon','Davon','Snyder','8/11/1993',
            75,6,3,239,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','RG',78,'Active',
            'Jermaine Hodges','Jermaine','Jermaine','Hodges','2/18/2004',
            75,6,3,261,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','LG',62,'Active',
            'Aaron White','Aaron','Aaron','White','2/21/1997',
            76,6,4,317,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','OG',67,'Active',
            'Errick Humphrey','Errick','Errick','Humphrey','3/29/1991',
            76,6,4,306,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','OG',58,'Active',
            'Blake Klein','Blake','Blake','Klein','9/19/2001',
            78,6,6,255,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','C',63,'Active',
            'Matt Hampton','Matt','Matt','Hampton','5/13/1995',
            74,6,2,240,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','OL','C',71,'Active',
            'Reshard Boone','Reshard','Reshard','Boone','9/28/1999',
            73,6,1,265,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','LDE',92,'Active',
            'Brylan Down','Brylan','Brylan','Down','11/30/2004',
            74,6,2,228,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','RDE',93,'Active',
            'Dom Atamo','Dom','Dom','Atamo','8/27/2001',
            74,6,2,235,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','DE',99,'Active',
            'Nolan Poole','Nolan','Nolan','Poole','1/7/2003',
            75,6,3,259,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','DE',96,'Active',
            'Del Smith','Del','Del','Smith','1/3/1998',
            78,6,6,250,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','DE',48,'Active',
            'Wesley Stamps','Wesley','Wesley','Stamps','10/30/2001',
            76,6,4,243,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','DT',95,'Active',
            'Joe Walker','Joe','Joe','Walker','9/6/1999',
            74,6,2,238,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','DT',91,'Active',
            'Sammy Sam','Sammy','Sammy','Sam','1/3/2001',
            75,6,3,260,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','DT',65,'Active',
            'Nathan McKee','Nathan','Nathan','McKee','3/4/1999',
            76,6,4,253,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DL','DT',61,'Active',
            'Doug Campers','Doug','Doug','Campers','8/18/1994',
            74,6,2,253,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','OLB',73,'Active',
            'Neil Krause','Neil','Neil','Krause','4/25/1992',
            73,6,1,195,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','OLB',56,'Active',
            'Oliver McIntyre','Oliver','Oliver','McIntyre','4/23/1999',
            72,6,0,206,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','EDGE',98,'Active',
            'Johnnie Barr','Johnnie','Johnnie','Barr','10/17/1994',
            72,6,0,211,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','EDGE',94,'Active',
            'Abdul Young','Abdul','Abdul','Young','5/5/1994',
            73,6,1,222,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','LB',45,'Active',
            'Samuel Schneider','Samuel','Samuel','Schneider','10/17/1990',
            73,6,1,214,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','MLB',55,'Active',
            'DD Rodgers','DD','DD','Rodgers','7/8/2002',
            74,6,2,217,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','ILB',55,'Active',
            'Will Hughes','Will','Will','Hughes','3/23/1999',
            74,6,2,220,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','ILB',43,'Active',
            'Cooper Stevenson','Cooper','Cooper','Stevenson','2/4/2001',
            73,6,1,213,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','LB','LB',87,'Active',
            'Grant Eaton','Grant','Grant','Eaton','11/3/1991',
            73,6,1,225,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','LCB',24,'Active',
            'Bill Dingle','Bill','Bill','Dingle','12/8/2001',
            69,5,9,180,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','RCB',39,'Active',
            'Jeremy Jimmy','Jeremy','Jeremy','Jimmy','11/22/2000',
            72,6,0,180,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','NCB',4,'Active',
            'DeAngelo Woodard','DeAngelo','DeAngelo','Woodard','6/2/1994',
            72,6,0,185,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','DCB',46,'Active',
            'Lemarcus Parsons','Lemarcus','Lemarcus','Parsons','9/9/1997',
            71,5,11,175,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','FS',36,'Active',
            'Jesse Shelton','Jesse','Jesse','Shelton','8/25/2004',
            74,6,2,190,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','SAF',23,'Active',
            'Chris Hickmon','Chris','Chris','Hickmon','1/23/1998',
            74,6,2,199,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','SS',31,'Active',
            'Timothy Dickens','Timothy','Timothy','Dickens','8/24/1996',
            74,6,2,194,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','DB','SAF',26,'Active',
            'LaShaun Gutierrez','LaShaun','LaShaun','Gutierrez','8/26/1995',
            71,5,11,191,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','SPEC','K',17,'Active',
            'Justin Powell','Justin','Justin','Powell','1/4/1999',
            70,5,10,209,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','SPEC','P',69,'Active',
            'Rob Butler','Rob','Rob','Butler','11/12/2002',
            73,6,1,195,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','SPEC','LS',79,'Active',
            'Velociraptor Maloish',
            'Velociraptor','Scoish','Maloish','11/25/1999',
            0,NULL,NULL,NULL,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','SPEC','LS',83,'Active',
            'Aristokles Prabhu','Aristokles','Aristokles','Prabhu','3/18/2005',
            0,NULL,NULL,NULL,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','SPEC','K',15,'Active',
            'Legume Druprix','Legume','Legume','Druprix','3/22/1997',
            72,6,0,191,'DVSU',0,1,'REG',2019,2019)
        ,(2019,1,'DEFL','DVSU','DVSU','SPEC','P',20,'Active',
            'Creme De La Creme','Creme','Creme','De La Creme','4/15/2003',
            0,NULL,NULL,NULL,'DVSU',0,1,'REG',2019,2019);

        """
        return sql_script.replace("        ", "")

    def depth_chart_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table that mostly
        mirrors the `depth_charts` dataset from `nflverse/nflverse-data`
        (https://github.com/nflverse/nflverse-data/releases/tag/depth_charts).

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that generates a SQLite3 table that mostly
        mirrors the `depth_charts` dataset from `nflverse/nflverse-data`.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_depth_charts"(
            "season"                INT NOT NULL,
            "league_id"             TEXT NOT NULL,
            "team_abv"              TEXT NOT NULL,
            "game_id"               INT NOT NULL,
            "week"                  INT NOT NULL,
            "game_type"             TEXT NOT NULL,
            /*
            Indicates where this player is on the depth chart
            for this specific position.
            For example, the starting QB will have a "depth_team" of `1`,
            QB2 will have a "depth_team" of `2`,
            and QB3 will have a "depth_team" of `3`.
            */
            "depth_team"            INT NOT NULL,
            "player_id"             INT NOT NULL,
            -- TEXT so a player can be identified by
            -- "00", "01", "1A", or "1O"/"1D"
            "player_jersey_number"  TEXT NOT NULL,
            "player_last_name"      TEXT NOT NULL,
            "player_first_name"     TEXT NOT NULL,
            /*
            Defaults to the value of "player_first_name",
            but can be set to a differient value
            (for example, Boomer Esiason, who's birth name is Norman Esiason,
            can have his "player_first_name" == "Norman",
            and his "player_football_name" == "Boomer").
            */
            "player_football_name"  TEXT NOT NULL,
            "player_full_name"      TEXT NOT NULL,
            -- Will be set to "offense", "defense", or "special_teams".
            "formation"             TEXT NOT NULL,
            "player_position"       TEXT NOT NULL,
            "player_depth_position" TEXT NOT NULL,
            "gsis_id"               TEXT,-- NFL GSIS Player ID.
            "espn_id"               INT, -- ESPN Player ID.
            "sportradar_id"         TEXT,-- Sportradar Player ID.
            "yahoo_id"              INT, -- Yahoo Sports Player ID.
            "rotowire_id"           INT, -- Rotowire Player ID.
            "pff_id"                INT, -- Pro Football Focus (PFF) Player ID.
            "pfr_id"                TEXT,-- Pro Football Reference Player ID.
            "fantasy_data_id"       INT,
            "sleeper_id"            INT,
            "esb_id"                TEXT,
            "smart_id"              TEXT,
            FOREIGN KEY ("league_id")
                REFERENCES "fb_leagues" ("league_id")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION,
            FOREIGN KEY ("league_id","season")
                REFERENCES "fb_seasons" ("league_id","season")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
        );

        CREATE UNIQUE INDEX idx_depth_charts_id
        ON "fb_depth_charts" (
            "season",
            "league_id",
            "team_id",
            "player_full_name",
            "week",
            "game_type",
            "player_depth_position",
            "depth_team"
        );


        INSERT INTO fb_depth_charts (
            "season",
            "league_id",
            "team_abv",
            "game_id",
            "week",
            "game_type",
            "depth_team",
            "player_id",
            "player_jersey_number",
            "player_last_name",
            "player_first_name",
            "player_football_name",
            "player_full_name",
            "formation",
            "player_position",
            "player_depth_position"
        )
        VALUES
             (2019,'DEFL','UGF',1,1,'REG',1,
                1,4,'Horton','Will','Will','Will Horton',
                'offense','QB','QB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                2,16,'Cooke','Howard','Howard','Howard Cooke',
                'offense','QB','QB')
            ,(2019,'DEFL','UGF',1,1,'REG',3,
                3,5,'Calhoun','Rod','Rodney','Rodney Calhoun',
                'offense','QB','QB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                4,7,'Hale','BJ','BJ','BJ Hale',
                'offense','RB','RB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                5,2,'Dingle','Ryan','Ryan','Ryan Dingle',
                'offense','RB','RB')
            ,(2019,'DEFL','UGF',1,1,'REG',3,
                6,42,'Minton','Rob','Rob','Rob Minton',
                'offense','RB','RB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                7,40,'Adamo','Tom','Tom','Tom Adamo',
                'offense','RB','FB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                8,39,'Eaton','Jason','Jason','Jason Eaton',
                'offense','RB','FB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                9,11,'Denman','Elliot','Elliot','Elliot Denman',
                'offense','WR','WR')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                10,12,'Stance','Neghan','Neghan','Neghan Stance',
                'offense','WR','WR')
            ,(2019,'DEFL','UGF',1,1,'REG',3,
                11,88,'Engle','Torren','Torren','Torren Engle',
                'offense','WR','WR')
            ,(2019,'DEFL','UGF',1,1,'REG',4,
                12,84,'McMahon','Vance','Vance','Vance McMahon',
                'offense','WR','WR')
            ,(2019,'DEFL','UGF',1,1,'REG',5,
                13,6,'Nelson','Jake','Jake','Jake Nelson',
                'offense','WR','WR')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                14,18,'Triplett','Tez','Tez','Tez Triplett',
                'offense','TE','TE')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                15,80,'Riley','Nick','Nick','Nick Riley',
                'offense','TE','TE')
            ,(2019,'DEFL','UGF',1,1,'REG',3,
                16,90,'Hunter','Ernest','Ernest','Ernest Hunter',
                'offense','TE','TE')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                17,77,'Robinson','Eric','Eric','Eric Robinson',
                'offense','OL','LT')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                18,71,'Bass','Bryce','Bryce','Bryce Bass',
                'offense','OL','LT')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                19,55,'Rich','Emmitt','Emmitt','Emmitt Rich',
                'offense','OL','RT')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                20,64,'James','Tyson','Tyson','Tyson James',
                'offense','OL','RT')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                21,57,'Tanner','Brent','Brent','Brent Tanner',
                'offense','OL','RG')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                22,63,'Henderson','Dave','D.D.','D.D. Henderson',
                'offense','OL','RG')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                23,72,'Milton','James','J.T.','J.T. Milton',
                'offense','OL','LG')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                24,59,'Huber','Adam','Adam','Adam Huber',
                'offense','OL','LG')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                25,61,'Eldridge','Bubba','Bubba','Bubba Eldridge',
                'offense','OL','C')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                26,54,'Bates','Shaud','Shaud','Shaud Bates',
                'offense','OL','C')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                27,89,'Singleton','LeRoy','LeRoy','LeRoy Singleton',
                'defense','DL','LDE')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                28,91,'Clelland','Jakari','Jakari','Jakari Clelland',
                'defense','DL','RDE')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                29,95,'Jennings','Eric','Eric','Eric Jennings',
                'defense','DL','LDE')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                30,66,'Hodges','Harrison','Harrison','Harrison Hodges',
                'defense','DL','RDE')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                31,87,'Manley','Leigh','Leigh','Leigh Manley',
                'defense','DL','NT')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                32,98,'Nixon','Dan','D.D.','D.D. Nixon',
                'defense','DL','DT')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                33,96,'Griffith','Eli','Eli','Eli Griffith',
                'defense','DL','DT')
            ,(2019,'DEFL','UGF',1,1,'REG',3,
                34,67,'Benton','Jimmie','J.T.','J.T. Benton',
                'defense','DL','DT')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                35,92,'Dailey','Mike','Mike','Mike Dailey',
                'defense','DL','NT')
            ,(2019,'DEFL','UGF',1,1,'REG',4,
                36,78,'Johnson','Gabriel','Gabriel','Gabriel Johnson',
                'defense','DL','DT')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                37,45,'Bridges','Harry','Harry','Harry Bridges',
                'defense','LB','ROLB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                38,50,'Ruff','Tyler','Tyler','Tyler Ruff',
                'defense','LB','LOLB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                39,99,'Riley','Ira','Ira','Ira Riley',
                'defense','LB','ROLB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                40,49,'Erickson','Donta','Donta','Donta Erickson',
                'defense','LB','LOLB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                41,52,'Tyson','Eric','Eric','Eric Tyson',
                'defense','LB','ILB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                42,51,'Landry','Elgin','Elgin','Elgin Landry',
                'defense','LB','ILB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                43,37,'Dale','Andrew','Andrew','Andrew Dale',
                'defense','DB','RCB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                44,19,'Thompson','Avery','Avery','Avery Thompson',
                'defense','DB','LCB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                45,1,'Eaton','Casey','Casey','Casey Eaton',
                'defense','DB','SCB')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                46,46,'Lindsey','Derek','Derek','Derek Lindsey',
                'defense','DB','CB')
            ,(2019,'DEFL','UGF',1,1,'REG',3,
                47,28,'Huffman','Kareem','Kareem','Kareem Huffman',
                'defense','DB','CB')
            ,(2019,'DEFL','UGF',1,1,'REG',3,
                48,24,'Ricks','Jimmie','Jimmie','Jimmie Ricks',
                'defense','DB','CB')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                49,26,'Preston','Benny','Benny','Benny Preston',
                'defense','DB','FS')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                50,23,'Manning','Keenan','Keenan','Keenan Manning',
                'defense','DB','SAF')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                51,34,'Poole','Buck','Buck','Buck Poole',
                'defense','DB','SS')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                52,48,'Huber','Kendal','Kendal','Kendal Huber',
                'defense','DB','SAF')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                53,38,'Francis','Andy','Andy','Andy Francis',
                'special_teams','SPEC','K')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                54,62,'Johnson','Rex','Rex','Rex Johnson',
                'special_teams','SPEC','K')
            ,(2019,'DEFL','UGF',1,1,'REG',1,
                55,69,'Rigdon','Jacob','Jacob','Jacob Rigdon',
                'special_teams','SPEC','P')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                56,65,'Washington','Stephen','Stephen','Stephen Washington',
                'special_teams','SPEC','P')
            ,(2019,'DEFL','UGF',1,1,'REG',1,57,14,
                'Baggagecling','Ba-jain','Logjammer','Logjammer Baggagecling',
                'special_teams','SPEC','LS')
            ,(2019,'DEFL','UGF',1,1,'REG',2,
                58,56,'Shoes','Triple','Triple','Triple Shoes',
                'special_teams','SPEC','LS');

        """
        return sql_script.replace("        ", "")

    def schedule_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table that mostly
        mirrors the `schedule.csv` file from `nflverse/nfldata`
        (https://github.com/nflverse/nfldata/blob/master/data/games.csv).

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that generates a SQLite3 table that mostly
        mirrors the `schedule.csv` file from `nflverse/nfldata`.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_schedule"(
            "season"                INT NOT NULL,
            "game_id"               INTEGER PRIMARY KEY AUTOINCREMENT,
            "game_is_in_progress"   INTEGER NOT NULL DEFAULT 0,
            "game_is_finished"      INTEGER NOT NULL DEFAULT 0,
            "league_id"             TEXT NOT NULL,

            -- Can be "finished", "in_progress", "delayed", or "not_started"
            "game_status"           TEXT NOT NULL DEFAULT "not_started",

            -- Formatted as
            -- "[season]_[league]_[week]_[away_team_abv]_[home_team_abv]".
            "nflverse_game_id"      TEXT NOT NULL,

            -- Can be "PRE", "REG", or "POST".
            -- Optionally, postseason games can be represented by
            -- > "WC" (wild card)
            -- > "DIV" (divisional round)
            -- > "CON" (conference championship)
            -- > "SB" (Super Bowl)
            -- > "CHAMP" (Non-Super Bowl championship)
            "game_type"             TEXT NOT NULL,
            "week"                  INT NOT NULL,

            -- Dates will be stored as "YYYY-MM-DD".
            "game_day"              TEXT NOT NULL,

            -- Formatted as "HH:MM:SS", in 24-hour time.
            "game_time"             TEXT NOT NULL,
            "game_datetime"         TEXT NOT NULL,
            "game_time_zone"        TEXT NOT NULL,

            -- Stored as "YYYY-MM-DDTHH:MM:SS+00:00"
            "game_datetime_utc"     TEXT NOT NULL,
            "game_day_of_week"      TEXT NOT NULL, -- Like "Monday" or "Sunday"
            "game_nation"           TEXT NOT NULL,
            "game_state"            TEXT NOT NULL,

            "away_team_abv"         TEXT NOT NULL,
            "away_team_score"       INT DEFAULT 0 NOT NULL,
            "home_team_abv"         TEXT NOT NULL,
            "home_team_score"       INT DEFAULT 0 NOT NULL,
            "nflverse_old_game_id"  INT,
            "gsis_id"               INT,
            "pfr_game_id"           TEXT,
            "pff_game_id"           TEXT,
            "espn_game_id"          INT,
            "ftn_game_id"           INT,
            "ncaa_game_id"           INT,
            "football_db_game_id"   TEXT,
            "arenafan_game_id"      INT,
            "yahoo_game_id"         TEXT,
            "away_days_rest"        INT,
            "home_days_rest"        INT,
            "is_neutral_site_game"  BOOLEAN DEFAULT FALSE NOT NULL,
            "is_overtime_game"      BOOLEAN DEFAULT FALSE NOT NULL,
            "is_divisional_game"    BOOLEAN DEFAULT FALSE NOT NULL,

            /*
            Can be one of the following categories:
            -- "dome": Means the game is played in a stadium with
                a covered roof, but the roof cannot
                be opened up to see the sky.
            -- "outdoors": Means the stadium lacks
                a roof to cover the stadium in any capacity.
            -- "closed": Means the game is played in
                a stadium with a covered roof,
                and the roof is CLOSED for this game.
            -- "open": Means the game is played in
                a stadium with a covered roof,
                and the roof is OPEN for this game.
            */
            "game_roof"             TEXT NOT NULL,

            /*
            Playing surface used in this game.
            Can be  one of the following categories
            (although a user could specify additional field surface types):

            -- "a_turf"
            -- "astro_play"
            -- "astroturf"
            -- "desso_grass"
            -- "field_turf"
            -- "grass"
            -- "matrix_turf"
            -- "sport_turf"
            */
            "surface" STR DEFAULT "grass" NOT NULL,
            "temp_f"                DOUBLE, -- Temperature, in Fahrenheit (°F)
            "temp_c"                DOUBLE, -- Temperature, in Celsius (°C)

            -- Wind Speed, in MPH unless otherwise specified.
            "wind"                  INT,
            "stadium_id"            INT NOT NULL,
            FOREIGN KEY ("stadium_id") REFERENCES "fb_stadiums" ("stadium_id")
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        );

        CREATE UNIQUE INDEX idx_schedule_id
        ON "fb_schedule" ("game_id","away_team_abv","home_team_abv");

        INSERT INTO fb_schedule(
            "season",
            "league_id",
            "game_status",
            "nflverse_game_id",
            "game_type",
            "week",
            "game_day",
            "game_time",
            "game_time_zone",
            "game_datetime",
            "game_datetime_utc",
            "game_day_of_week",
            "game_nation",
            "game_state",
            "away_team_abv",
            "home_team_abv",
            "game_roof",
            "surface",
            "stadium_id"
        )
        VALUES (
            2019,
            'DEFL',
            'finished',
            '2019_DEFL_01_DVSU_UGF',
            'REG',
            1,
            '2019-08-01',
            '12:00',
            'EST',
            '2019-08-01T07:00:00+04:00',
            '2019-08-01T07:00:00Z',
            'Thursday',
            'US',
            'US-OH',
            'DVSU',
            'UGF',
            'dome',
            'fieldturf',
            1
        );

        """
        return sql_script.replace("        ", "")

    def game_betting_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table that
        holds betting data (if advalible) for specific games.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that generates a SQLite3 table that
        holds information about the ref crew for this specific game.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_betting"(
            "game_id"               INT NOT NULL,
            "betting_book"          TEXT NOT NULL,
            "over_under_open"       DOUBLE,
            "over_under_close"      DOUBLE,
            "home_spread_open"      DOUBLE,
            "home_spread_close"     DOUBLE,
            "away_spread_open"      DOUBLE,
            "away_spread_close"     DOUBLE,
            "home_moneyline_open"   INT,
            "home_moneyline_close"  INT,
            "away_moneyline_open"   INT,
            "away_moneyline_close"  INT,
            FOREIGN KEY ("game_id")
                REFERENCES "fb_schedule" ("game_id")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
        );
        CREATE UNIQUE INDEX idx_betting_id
        ON "fb_betting" ("game_id","betting_book");

        INSERT INTO fb_betting(
            game_id,
            betting_book,
            over_under_open,
            over_under_close,
            home_spread_open,
            home_spread_close,
            away_spread_open,
            away_spread_close,
            away_moneyline_open,
            away_moneyline_close,
            home_moneyline_open,
            home_moneyline_close
        )
        VALUES
            (1,'bettingisforlosers.com',50,30.5,-8,-3,8,3,-150,-150,1000,1000),
            (1,'onlysuckersbet.com',30.5,32,-21,-5,21,5,-1000,-1000,500,500);

        """
        return sql_script.replace("        ", "")

    def game_refs_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table that
        holds information about the ref crew for this specific game.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that generates a SQLite3 table that
        holds information about the ref crew for this specific game.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_game_refs"(
            "game_id"           INT NOT NULL,
            -- If unkown (rare, but can theoretically happen),
            -- just set this to `0` or NULL.
            "ref_num"           INT,
            "ref_position_abv"  TEXT NOT NULL, -- Can be the following values:
            /*
            -- "R": Referee. Responsible for the general supervision
                of the game and has the final authority on all rulings.
            -- "U": Umpire. Stands behind the defensive line and linebackers,
                observing the blocks by the offensive line and defenders
                trying to ward off those blocks,
                looking for holding or illegal blocks.
            -- "DJ": Down Judge. Stands at one end of the line of scrimmage
                (usually the side opposite the press box,
                always with the chain crew), looking for possible offsides,
                encroachment and other fouls before the snap.
            -- "HL": Head Linesman. Same job as Down Judge.
            -- "LJ": Line Judge. Assists the head linesman/down judge
                at the other end of the line of scrimmage,
                looking for possible offsides,
                encroachment and other fouls before the snap.
            -- "FJ": Field judge. Works downfield behind the defensive
                secondary on the same sideline as the line judge.
                The field judge makes decisions near the sideline on
                his or her side of the field, judging the action
                of nearby running backs, receivers and defenders.
            -- "BU": Back Umpire. Same job as field judge.
            -- "SJ": Side judge. Works downfield behind the
                defensive secondary on the same sideline
                as the head linesman or down judge.
            -- "BJ": Back judge. Stands deep behind the defensive secondary
                in the middle of the field, judging the action of nearby
                running backs, receivers (primarily the tight ends),
                and nearby defenders.
            -- "C": Center judge. Positioned beside the referee
                in the offensive backfield adjacent to the referee,
                positioned equivalent to the umpire.

            Other, atypical ref positions:
            -- "BS": Ball Spotter. Used in XFL 2.0/3.0,
                exactly what it sounds, and the ball spotter wears a red cap.
                Also serves as the kickoff holder if the ball
                keeps falling off before a successful kickoff.
            -- "SK": Sky Judge. Used in leagues such as
                the defunct Alliance of American Football (AAF).
                Effectively, a sky judge is a referee that is stationed
                off the field, but has the power of calling penalties
                and making corrections to the play after the play is over.
            -- "C8": CFL 8th Official.
                Briefly experimented with by the CFL in 2018,
                but never used post 2018.
                This official lined up in the offensive backfield,
                and whose sole responsibility was
                judging helmet contact on the quarterback.
            -- "DE": Deep Judge.
                Experimented from the NFL between the 2010
                and 2011 pre-seasons. The primary responsibility for
                this new position is the action of receivers,
                and it allowed the NFL to adjust coverage after
                the umpire was moved to the offensive backfield.
            -- "U2": Second Umpire. Abandoned idea by the NFL,
                but was experimented in pre-season games between
                2015 and 2019. Their responsibilities were to
                focus on center pre-snap and offensive guards and tackles.
            -- "MJ": Middle Judge. Experimented by the NFL between
                the 2015 and 2019. Main responsibilities were to
                look for holding near the line of scrimmage.
            -- "UK": Unknown. Only use if you know the official
                was officiating this game,
                but don't know what his position was for this game.

            sources:
            https://operations.nfl.com/officiating/the-officials/officials-responsibilities-positions/
            https://en.wikipedia.org/wiki/Official_(gridiron_football)
            */
            "ref_position_name" TEXT NOT NULL,
            -- ["ref_full_name"] = ["ref_first_name"] + " " + ["ref_last_name"]
            "ref_full_name"     TEXT NOT NULL,
            "ref_first_name"    TEXT NOT NULL,
            "ref_last_name"     TEXT NOT NULL,
            FOREIGN KEY ("game_id")
                REFERENCES "fb_schedule" ("game_id")
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
        );

        INSERT INTO fb_game_refs (
            "game_id",
            "ref_num",
            "ref_position_abv",
            "ref_position_name",
            "ref_full_name",
            "ref_first_name",
            "ref_last_name"
        )
        VALUES
            (1, 11, 'R', 'Referee', 'Cyril Apolinar', 'Cyril', 'Apolinar'),
            (1, 22, 'U', 'Umpire', 'Aya Stanimir', 'Aya', 'Stanimir'),
            (1, 33, 'DJ', 'Down Judge',
                'Shaka Catharine', 'Shaka', 'Catharine'),
            (1, 44, 'HL', 'Head Linesman',
                'Natsuki Europa', 'Natsuki', 'Europa'),
            (1, 55, 'LJ', 'Line Judge',
                'Petre Nikostratos', 'Petre', 'Nikostratos'),
            (1, 61, 'FJ', 'Field judge',
                'Shamil Prashant', 'Shamil', 'Prashant'),
            (1, 77, 'BU', 'Back Umpire',
                'Deneb Sneewittchen', 'Deneb', 'Sneewittchen'),
            (1, 88, 'SJ', 'Side judge', 'Bricius Nirmal', 'Bricius', 'Nirmal'),
            (1, 99, 'BJ', 'Back judge', 'Arevik Elliot', 'Arevik', 'Elliot'),
            (1, 101, 'C', 'Center judge', 'Ruslan Hadija', 'Ruslan', 'Hadija');
        """
        return sql_script.replace("        ", "")

    def game_pbp_sql_file() -> str:
        """
        Returns a SQLite3 script that generates a SQLite3 table that
        stores PBP data in a JSON format.

        Parameters
        ----------
        None

        Returns
        ----------
        A SQLite3 script that generates a SQLite3 table that
        stores PBP data in a JSON format.
        """

        sql_script = """
        CREATE TABLE IF NOT EXISTS "fb_pbp" (
            "game_id"     INT NOT NULL,
            "game_json_str"	TEXT NOT NULL,
            FOREIGN KEY(game_id) REFERENCES  fb_schedule(game_id)
        );
        """
        return sql_script.replace("        ", "")


def create_app_sqlite3_db(custom_dir: str = None):
    """ """
    # print(SqliteSampleFiles.leagues_sql_file())

    sql_file = ""
    if custom_dir is not None:
        # custom_dir
        try:
            makedirs(f"{custom_dir}/.sdv_pbp_fb/")

            # if platform.system() == "Windows":
            #     system(f"attrib +h {home_dir}/.sdv_pbp_fb")
        except FileExistsError:
            logging.info("%s/.sdv_pbp_fb/ already exists.", custom_dir)

        sql_file = f"{custom_dir}/.sdv_pbp_fb/sdv_pbp_py.sqlite"

    else:
        home_dir = expanduser("~")
        try:
            makedirs(f"{home_dir}/.sdv_pbp_fb/")

            # if platform.system() == "Windows":
            #     system(f"attrib +h {home_dir}/.sdv_pbp_fb")
        except FileExistsError:
            logging.info("%s/.sdv_pbp_fb/ already exists.", custom_dir)
        sql_file = f"{home_dir}/.sdv_pbp_fb/sdv_pbp_py.sqlite"

    del custom_dir

    con = sqlite_connect(sql_file)
    cur = con.cursor()

    cur.executescript(SqliteSampleFiles.iso_nations())
    con.commit()

    cur.executescript(SqliteSampleFiles.iso_timezones())
    con.commit()

    cur.executescript(SqliteSampleFiles.iso_3166_2_states())
    con.commit()

    cur.executescript(SqliteSampleFiles.iso_3166_2_data())
    con.commit()

    cur.executescript(SqliteSampleFiles.leagues_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.seasons_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.teams_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.rosters_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.stadiums_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.weekly_rosters_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.depth_chart_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.schedule_sql_file())
    con.commit()

    # cur.executescript(SqliteSampleFiles.game_betting_sql_file())
    # con.commit()

    cur.executescript(SqliteSampleFiles.game_refs_sql_file())
    con.commit()

    cur.executescript(SqliteSampleFiles.game_pbp_sql_file())
    con.commit()


if __name__ == "__main__":

    # For Debug purposesF
    create_app_sqlite3_db()
