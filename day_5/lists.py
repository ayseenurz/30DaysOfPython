empty_list = []
some_list = [1, 2, 3, 4, 5]
print(len(some_list))
print(some_list[0::2])

mixed_data_types = ['ayşenur', 22, 1.67, 'bekar', 'türkiye']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0::3])

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('Twitter')

it_companies.insert(4, 'LinkedIn')
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

#it_companies = '#; '.join(it_companies)
#print(it_companies)

is_there_Meta = 'Meta' in it_companies
print(is_there_Meta)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies) 

it_companies_first3 = it_companies[0:3]
print(it_companies_first3)

it_companies_middle3 = it_companies[3:6]
print(it_companies_middle3)

it_companies_last3 = it_companies[6:9]
print(it_companies_last3)

it_companies_midd_somn = it_companies[3:6]
print(it_companies_midd_somn)

it_companies.remove("Meta")
print(it_companies)

it_companies.remove("LinkedIn")
print(it_companies)

it_companies.remove("Amazon")
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies #destroy the list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
full_stack.insert(7, 'Redux')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

max_age = max(ages)
min_age = min(ages)
print(max_age)
print(min_age)

ages.append(max_age)
ages.append(min_age)
print(ages)

if len(ages) % 2 == 0:
    median1 = ages[len(ages)//2]
    median2 = ages[len(ages)//2 - 1]
    median = (median1 + median2)/2
else:
    median = ages[len(ages)//2]
print(median)

ages_avg = sum(ages)/len(ages)
print(ages_avg)

print(abs(max_age - min_age))

min_avg = abs(min_age - ages_avg)
max_avg = abs(max_age - ages_avg)
print(min_avg)
print(max_avg)
print(min_avg == max_avg)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

if len(countries) % 2 == 0:
    median1 = countries[len(countries)//2]
    median2 = countries[len(countries)//2 - 1]
    median = (median1 + median2)/2
else:
    median = countries[len(countries)//2]
print(median)

len_countries = len(countries)
print(len_countries)

first_half_countries = countries[:len(countries)//2+1]
print(len(first_half_countries))
last_half_countries = countries[len(countries)//2+1:len(countries)]
print(len(last_half_countries))

some_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = some_countries
print(scandic)
