# !!full code to search for patterns/words in an input and create an output!!
# parts of code need to be separated for other parts of code...

        # ONLY PHOSPHATE, PHOSPHITE, SULFATE, AND SULFITE WORK FOR THE COMPOUND PART...

# import all modules
# subscript 'import'
# used for subscripting numbers in formulas
subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

# import RegEx module
# used for searching strings
import re # askpython.com, PYnative.com

# dict for words to formulas
# used in elements and compounds
Elements = {
    'Actinium': 'Ac',
    'Aluminum': 'Al',
    'Americium': 'Am',
    'Antimony': 'Sb',
    'Argon': 'Ar',
    'Arsenic': 'As',
    'Astatine': 'At',
    'Barium': 'Ba',
    'Berkelium': 'Bk',
    'Beryllium': 'Be',
    'Bismuth': 'Bi',
    'Bohrium': 'Bh',
    'Boron': 'B',
    'Bromine': 'Br',
    'Cadmium': 'Cd',
    'Calcium': 'Ca',
    'Californium': 'Cf',
    'Carbon': 'C',
    'Cerium': 'Ce',
    'Cesium': 'Cs',
    'Chlorine': 'Cl',
    'Chromium': 'Cr',
    'Cobalt': 'Co',
    'Copper': 'Cu',
    'Curium': 'Cm',
    'Darmstadtium': 'Ds',
    'Dubnium': 'Db',
    'Dysprosium': 'Dy',
    'Einsteinium': 'Es',
    'Erbium': 'Er',
    'Europium': 'Eu',
    'Fermium': 'Fm',
    'Fluorine': 'F',
    'Francium': 'Fr',
    'Gadolinium': 'Gd',
    'Gallium': 'Ga',
    'Germanium': 'Ge',
    'Gold': 'Au',
    'Hafnium': 'Hf',
    'Hassium': 'Hs',
    'Helium': 'He',
    'Holmium': 'Ho',
    'Hydrogen': 'H',
    'Indium': 'In',
    'Iodine': 'I',
    'Iridium': 'Ir',
    'Iron': 'Fe',
    'Krypton': 'Kr',
    'Lanthanum': 'La',
    'Lawrencium': 'Lr',
    'Lead': 'Pb',
    'Lithium': 'Li',
    'Lutetium': 'Lu',
    'Magnesium': 'Mg',
    'Manganese': 'Mn',
    'Meitnerium': 'Mt',
    'Mendelevium': 'Md',
    'Mercury': 'Hg',
    'Molybdenum': 'Mo',
    'Neodymium': 'Nd',
    'Neon': 'Ne',
    'Neptunium': 'Np',
    'Nickel': 'Ni',
    'Niobium': 'Nb',
    'Nitrogen': 'N',
    'Nobelium': 'No',
    'Oganesson': 'Uuo',
    'Osmium': 'Os',
    'Oxygen': 'O',
    'Palladium': 'Pd',
    'Phosphorus': 'P',
    'Platinum': 'Pt',
    'Plutonium': 'Pu',
    'Polonium': 'Po',
    'Potassium': 'K',
    'Praseodymium': 'Pr',
    'Promethium': 'Pm',
    'Protactinium': 'Pa',
    'Radium': 'Ra',
    'Radon': 'Rn',
    'Rhenium': 'Re',
    'Rhodium': 'Rh',
    'Roentgenium': 'Rg',
    'Rubidium': 'Rb',
    'Ruthenium': 'Ru',
    'Rutherfordium': 'Rf',
    'Samarium': 'Sm',
    'Scandium': 'Sc',
    'Seaborgium': 'Sg',
    'Selenium': 'Se',
    'Silicon': 'Si',
    'Silver': 'Ag',
    'Sodium': 'Na',
    'Strontium': 'Sr',
    'Sulfur': 'S',
    'Tantalum': 'Ta',
    'Technetium': 'Tc',
    'Tellurium': 'Te',
    'Terbium': 'Tb',
    'Thallium': 'Tl',
    'Thorium': 'Th',
    'Thulium': 'Tm',
    'Tin': 'Sn',
    'Titanium': 'Ti',
    'Tungsten': 'W',
    'Ununbium': 'Uub',
    'Ununhexium': 'Uuh',
    'Ununpentium': 'Uup',
    'Ununquadium': 'Uuq',
    'Ununseptium': 'Uus', 
    'Ununtrium': 'Uut', 
    'Uranium': 'U',
    'Vanadium': 'V',
    'Xenon': 'Xe',
    'Ytterbium': 'Yb',
    'Yttrium': 'Y',
    'Zinc': 'Zn',
    'Zirconium': 'Zr'
}

# dict of different common compound elements (shortened)
# dict of 'compounded elements' and oxide


Comb = {
    'Actin': 'Ac',
    'Alumin': 'Al',
    'Americ': 'Am',
    'Antimon': 'Sb',
    'Arsen': 'As',
    'Astatin': 'At',
    'Bar': 'Ba',
    'Berkel': 'Bk',
    'Beryll': 'Be',
    'Bism': 'Bi',
    'Bohr': 'Bh',
    'Bor': 'B',
    'Brom': 'Br',
    'Cadm': 'Cd',
    'Calc': 'Ca',
    'Californ': 'Cf',
    'Carbon': 'C',
    'Cer': 'Ce',
    'Ces': 'Cs',
    'Chlor': 'Cl',
    'Chrom': 'Cr',
    'Cob': 'Co',
    'Copper': 'Cu',
    'Cur': 'Cm',
    'Darmstadt': 'Ds',
    'Dubn': 'Db',
    'Dyspros': 'Dy',
    'Einstein': 'Es',
    'Erb': 'Er',
    'Europ': 'Eu',
    'Ferm': 'Fm',
    'Fluor': 'F',
    'Franc': 'Fr',
    'Gadolin': 'Gd',
    'Gall': 'Ga',
    'German': 'Ge',
    'Hafn': 'Hf',
    'Hass': 'Hs',
    'Holm': 'Ho',
    'Hydro': 'H',
    'Ind': 'In',
    'Iod': 'I',
    'Irid': 'Ir',
    'Iron': 'Fe',
    'Krypton': 'Kr',
    'Lanthan': 'La',
    'Lawrenc': 'Lr',
    'Lead': 'Pb',
    'Lith': 'Li',
    'Lutet': 'Lu',
    'Magnes': 'Mg',
    'Mangan': 'Mn',
    'Meitner': 'Mt',
    'Mendelev': 'Md',
    'Mercur': 'Hg',
    'Molybden': 'Mo',
    'Neodym': 'Nd',
    'Neptun': 'Np',
    'Nickel': 'Ni',
    'Niob': 'Nb',
    'Nitr': 'N',
    'Nobel': 'No',
    'Oganesson': 'Uuo',
    'Osmium': 'Os',
    'Oxide': 'O',
    'Palladium': 'Pd',
    'Phosphorus': 'P',
    'Platinum': 'Pt',
    'Plutonium': 'Pu',
    'Polonium': 'Po',
    'Potassium': 'K',
    'Praseodymium': 'Pr',
    'Promethium': 'Pm',
    'Protactinium': 'Pa',
    'Radium': 'Ra',
    'Radon': 'Rn',
    'Rhenium': 'Re',
    'Rhodium': 'Rh',
    'Roentgenium': 'Rg',
    'Rubidium': 'Rb',
    'Ruthenium': 'Ru',
    'Rutherfordium': 'Rf',
    'Samarium': 'Sm',
    'Scandium': 'Sc',
    'Seaborgium': 'Sg',
    'Selenium': 'Se',
    'Silicon': 'Si',
    'Silver': 'Ag',
    'Sodium': 'Na',
    'Strontium': 'Sr',
    'Sulfur': 'S',
    'Tantalum': 'Ta',
    'Technetium': 'Tc',
    'Tellurium': 'Te',
    'Terbium': 'Tb',
    'Thallium': 'Tl',
    'Thorium': 'Th',
    'Thulium': 'Tm',
    'Tin': 'Sn',
    'Titanium': 'Ti',
    'Tungsten': 'W',
    'Ununbium': 'Uub',
    'Ununhexium': 'Uuh',
    'Ununpentium': 'Uup',
    'Ununquadium': 'Uuq',
    'Ununseptium': 'Uus', 
    'Ununtrium': 'Uut', 
    'Uranium': 'U',
    'Vanadium': 'V',
    'Xenon': 'Xe',
    'Ytterbium': 'Yb',
    'Yttrium': 'Y',
    'Zinc': 'Zn',
    'Zirconium': 'Zr'
}


# dict of different compound prefixes/suffixes and what they mean
# used in compounds
Fixes = {
    'Mon': '1',
    'Di': '2',
    'Tri': '3',
    'Tetr': '4',
    'Pent': '5',
    'Hex': '6',
    'Hept': '7',
    'Oct': '8',
    'Non': '9',
    'Dec': '10'
}

# ide occurs when two nonmetals bond together so it's only a placeholder and doesn't mean very much
# used in compounds
ite = ('O2'.translate(subscript))
ate = ('O3'.translate(subscript))

# special cases of ate/ite being different
# used in compounds
Phosphite = ('PO3'.translate(subscript))
Phosphate = ('PO4'.translate(subscript))
Sulfite = ('SO3'.translate(subscript))
Sulfate = ('SO4'.translate(subscript))



# ALL ABOVE ARE FOR REFERENCE IN LATER CODE
# ALL BELOW ARE THE CODES THAT USE THE REFERENCES



# directory for different stages of code
i = input('1 for Elements, 2 for Compounds, 3 for Extended Elements: ')
if i == '1':
    y = input('Give the name of the individual elements with all beginning letters capitalized (Max 4): ')
    
    # split the words from the input
    split = re.split(r'\s',y) # askpython.com
    num_split = len(split)
    
    # use get method to reference dict based on input and length of input
    if num_split == 1:
        print(Elements.get(split[0])) # for one element

    if num_split == 2:
        print(Elements.get(split[0]), Elements.get(split[1])) # for two elements

    if num_split == 3:
        print(Elements.get(split[0]), Elements.get(split[1]), Elements.get(split[2])) # for 3 elements

    if num_split == 4:
        print(Elements.get(split[0]), Elements.get(split[1]), Elements.get(split[2]), Elements.get(split[3])) # for 4 elements
    
elif i == '2':
    y = input('Give the name of the compound with all beginning letters capitalized (Max 4 words, oxides & acids not supported): ')
    
    # split the words from the input
    split = re.split(r'\s',y) # askpython.com
    num_split = len(split)
    
    # use get method to reference dict based on phosphate/sulfate
    #phosphate
    if any('Phosphate' in word for word in split):
        if split[0] == 'Phosphate':
            print(Phosphate)
            quit()

        if split[1] == 'Phosphate':
            print(Elements.get(split[0]), Phosphate)
            quit()

        if split[2] == 'Phosphate':
            print(Elements.get(split[0]), Elements.get(split[1]), Phosphate)
            quit()

        if split[3] == 'Phosphate':
            print(Elements.get(split[0]), Elements.get(split[1]), Elements.get(split[2]), Phosphate)
            quit()

    # phosphite
    if any('Phosphite' in word for word in split):
        if split[0] == 'Phosphite':
            print(Phosphite)
            quit()

        if split[1] == 'Phosphite':
            print(Elements.get(split[0]), Phosphite)
            quit()

        if split[2] == 'Phosphite':
            print(Elements.get(split[0]), Elements.get(split[1]), Phosphite)
            quit()

        if split[3] == 'Phosphite':
            print(Elements.get(split[0]), Elements.get(split[1]), Elements.get(split[2]), Phosphite)
            quit()

    # sulfate
    if any('Sulfate' in word for word in split):
        if split[0] == 'Sulfate':
            print(Sulfate)
            quit()

        if split[1] == 'Sulfate':
            print(Elements.get(split[0]), Sulfate)
            quit()

        if split[2] == 'Sulfate':
            print(Elements.get(split[0]), Elements.get(split[1]), Sulfate)
            quit()

        if split[3] == 'Sulfate':
            print(Elements.get(split[0]), Elements.get(split[1]), Elements.get(split[2]), Sulfate)
            quit()

    # sulfite
    if any('Sulfite' in word for word in split):
        if split[0] == 'Sulfite':
            print(Sulfite)
            quit()

        if split[1] == 'Sulfite':
            print(Elements.get(split[0]), Sulfite)
            quit()

        if split[2] == 'Sulfite':
            print(Elements.get(split[0]), Elements.get(split[1]), Sulfite)
            quit()

        if split[3] == 'Sulfite':
            print(Elements.get(split[0]), Elements.get(split[1]), Elements.get(split[2]), Sulfite)
            quit()

    # figure out how to search words for patterns, ie Di = 2 ite = O2,
    # search string (split) for each prefix/suffix
    Mon_ = re.search(r'Mon', str(split))
    if Mon_:
        print(Fixes.get(Mon_.group()))
        # takes output from above formula and references Fixes dict and outputs value

    Di_ = re.search(r'Di', str(split))
    if Di_:
        print(Fixes.get(Di_.group()))

    Tri_ = re.search(r'Tri', str(split))
    if Tri_:
        print(Fixes.get(Tri_.group()))

    Tetr_ = re.search(r'Tetr', str(split))
    if Tetr_:
        print(Fixes.get(Tetr_.group()))

    Pent_ = re.search(r'Pent', str(split))
    if Pent_:
        print(Fixes.get(Pent_.group()))

    Hex_ = re.search(r'Hex', str(split))
    if Hex_:
        print(Fixes.get(Hex_.group()))

    Hept_ = re.search(r'Hept', str(split))
    if Hept_:
        print(Fixes.get(Hept_.group()))

    Oct_ = re.search(r'Oct', str(split))
    if Oct_:
        print(Fixes.get(Oct_.group()))

    Non_ = re.search(r'Non', str(split))
    if Non_:
        print(Fixes.get(Non_.group()))

    Dec_ = re.search(r'Dec', str(split))
    if Dec_:
        print(Fixes.get(Dec_.group()))

    # search string split for root of elements
    Nitrate_ = re.search(r'Nitr', str(split))
    if Nitrate_:
        print(Comb.get(Nitrate_.group()))




    # combine above prefixes with ide ite and ate, ie O8
    ite_ = re.search(r'ite', str(split))
    if ite_:
        print(ite)

    ate_ = re.search(r'ate', str(split))
    if ate_:
        print(ate)


elif i == '3':
    
    # Finding elements and their respective features.

    # Create a dictionary of all of the elements as the keys and the different features of the elements as vales.
    # features include: Atomic number, Atomic mass, Electron configuration, and Common oxidation states.

    atomic_features =  {'Actinium': ('89', '227', '[Rn] 6d^1 7s^2', '+3'),
        'Aluminum': ('13', '26.982', '[Ne] 3s^2 3p^1', '+3'),
        'Americium': ('95', '243', '[Rn] 5f^7 7s^2', '+3'),
        'Antimony': ('51', '121.76', '[Kr] 4d^10 5s^2 5p^3', '-3, +3, +5'),
        'Argon': ('18', '39.948', '[Ne] 3s^2 3p^6', '0'),
        'Arsenic': ('33', '74.922', '[Ar] 3d^10 4s^2 4p^3', '-3, +3, +5'),
        'Astatine': ('85', '210', '[Xe] 4f^14 5d^10 6s^2 6p^5', '-1, +1'),
        'Barium': ('56', '157.33', '[Xe] 6s^2', '+2'),
        'Berkelium': ('97', '247', '[Rn] 5f^9 7s^2', '+3'),
        'Beryllium': ('4', '9.012', '[He] 2s^2', '+2'),
        'Bismuth': ('83', '208.98', '[Xe] 4f^14 5d^10 6s^2 6p^3', '+3'),
        'Bohrium': ('107', '264', '', '[Rn] 5f^14 6d^5 7s^2'),
        'Boron': ('5', '10.811', '[He] 2s^2 2p^1', '+3'),
        'Bromine': ('35', '79.904', '[Ar] 3d^10 4s^2 4p^5', '-1, +1, +3, +5'),
        'Cadmium': ('48', '112.41', '[Kr] 4d^10 5s^2', '+2'),
        'Calcium': ('20', '40.078', '[Ar] 4s^2', '+2'),
        'Californium': ('98', '251', '[Rn] 5f^10 7s^2', '+3'),
        'Carbon': ('6', '12.011', '[He] 2s^2 2p^2', '-4, -3, -2, -1, +1, +2, +3, +4'),
        'Cerium': ('58', '140.12', '[Xe] 4f^1 5d^1 6s^2', '+3, +4'),
        'Cesium': ('55', '132.91', '[Xe] 6s^1', '+1'),
        'Chlorine': ('17', '35.453', '[Ne] 3s^2 3p^5', '-1'),
        'Chromium': ('24', '51.996', '[Ar] 3d^5 4s^1', '+2, +3, +6'),
        'Cobalt': ('27', '58.933', '[Ar] 3d^7 4s^2', '−3, −1, 0, +1, +2, +3, +4, +5'),
        'Copper': ('29', '63.546', '[Ar] 3d^10 4s^1', '+2'),
        'Curium': ('96', '247', '[Rn] 5f^7 6d^1 7s^2', '+3, +4'),
        'Darmstadtium': ('110', '281', '[Rn] 5f^14 6d^9 7s^1', 'Unknown'),
        'Dubnium': ('105', '262', '[Rn] 5f^14 6d^3 7s^2', 'Unknown'),
        'Dysprosium': ('66', '162.5', '[Xe] 4f^10 6s^2', '+3'),
        'Einsteinium': ('99', '252', '[Rn] 5f^11 7s^2', '+2, +3'),
        'Erbium': ('68', '167.26', '[Xe] 4f^12 6s^2', '+3'),
        'Europium': ('63', '151.96', '[Xe] 4f^7 6s^2', '+2, +3'),
        'Fermium': ('100', '257', '[Rn] 5f^12 7s^2', '+2, +3'),
        'Fluorine': ('9', '18.998', ' [He] 2s^2 2p^5', '-1'),
        'Francium': ('87', '223', '[Rn] 7s^1', '+1'),
        'Gadolinium': ('64', '157.25', '[Xe] 4f^7 5d^1 6s^2', '+3'),
        'Gallium': ('31', '69.723', '[Ar] 3d^10 4s^2 4p^1', '+3'),
        'Germanium': ('32', '74.620', '[Ar] 3d^10 4s^2 4p^2', '+2, +3'),
        'Gold': ('79', '196.967', '[Xe] 4f^14 5d^10 6s^1', '+1, +3'),
        'Hafnium': ('72', '178.49', '[Xe] 4f^14 5d^2 6s^2', '−2, 0, +1, +2, +3, +4'),
        'Hassium': ('108', '269', '[Rn] 5f^14 6d^6 7s^2', '8'),
        'Helium': ('2', '4.003', '1s^2', '0'),
        'Holmium': ('67', '164.93', '[Xe] 4f^11 6s^2', '+3'),
        'Hydrogen': ('1', '1.008', '1s^1', '+1, -1'),
        'Indium': ('49', '114.82', '[Kr] 4d^10 5s^2 5p^1', '+1, +3'),
        'Iodine': ('53', '126.905', '[Kr] 4d^10 5s^2 5p^5', '−1, +1, +3, +5, +7'),
        'Iridium': ('77', '192.217', '[Xe] 4f^14 5d^7 6s^2', '−3, −1, 0, +1, +2, +3, +4, +5, +6, +7, +8, +9'),
        'Iron': ('26', '55.845', '[Ar] 3d^6 4s^2', '+2, +3, +4, +6'),
        'Krypton': ('36', '83.798', '[Ar] 3d^10 4s^2 4p^6', '0'),
        'Lanthanum': ('57', '138.905', '[Xe] 5d^1 6s^2', '0, +1, +2, +3'),
        'Lawrencium': ('103', '262', '[Rn] 5f^14 7s^2 7p^1', '+3'),
        'Lead': ('82', '207.2', '[Xe] 6s^2 4f^14 5d^10 6^2', '+2, +4'),
        'Lithium': ('3', '6.941', '1s^2 2s^1', '+1'),
        'Lutetium': ('71', '174.967', '[Xe] 4f^14 5d^1 6s^2', '+3'),
        'Magnesium': ('12', '24.305', '[Ne] 3s^2', '+1'),
        'Manganese': ('25', '54.908', '[Ar] 3d^5 4s^2', '−3, −2, −1, 0, +1, +2, +3, +4, +5, +6, +7'),
        'Meitnerium': ('109', '278', '[Rn] 5f^14 6d^7 7s^2', '+1, +3, +4, +6, +8, +9 (predicted)'),
        'Mendelevium': ('101', '258', '[Rn] 5f^13 7s^2', '+2, +3'),
        'Mercury': ('80', '200.59', '[Xe] 4f^14 5d^10 6s^2', '+1, +2'),
        'Molybdenum': ('42', '95.95', '[Kr] 4d^5 5s^1', '+2, +3, +4, +5, +6'),
        'Neodymium': ('60', '144.242', '[Xe] 4f^4 6s^2', '+2, +3, +4'),
        'Neon': ('10', '20.18', '[He] 2s^2 2p^6', '0'),
        'Neptunium': ('93', '237.048', '[Rn] 5f^4 6d^1 7s^2', '+3, +4, +5, +6, +7'),
        'Nickel': ('28', '58.693', '[Ar] 3d^8 4s²^2', '-1,+2, +3, +4'),
        'Niobium': ('41', '92.906', '[Kr] 4d^4 5s^1', '+2, +3, +4, +5'),
        'Nitrogen': ('7', '14.007', '[He] 2s^2 2p^3', '-3, +5'),
        'Nobelium': ('102', '259', '[Rn] 5f^14 7s^2', '+2, +3'),
        'Oganesson': ('118', '294', '5f^14 6d^10 7s^2 7p^6', '+6, +4, +2, +1, 0, -1'),
        'Osmium': ('76', '190.23', '[Xe] 4f^14 5d^6 6s^2', '+2, +3, +4, +6, +8'),
        'Oxygen': ('8', '15.999', '[He] 2s^2 2p^4', '-2'),
        'Palladium': ('46', '106.2', '[Kr] 4d^10', '0, +1, +2, +3, +4'),
        'Phosphorus': ('15', '30.974', '[Ne] 3s^2 3p^3', '-3, −2, −1, 0, +1, +2, +3, +4, +5'),
        'Platinum': ('78', '195.084', '[Xe] 4f^14 5d^9 6s^1', '+2, +4'),
        'Plutonium': ('94', '244', '[Rn] 5f^6 7s^2', '+2, +3, +4, +5, +6, +7, +8'),
        'Polonium': ('84', '209', '[Xe] 6s^2 4f^14 5d^10 6p^4', '	−2, +2, +3, +4, +6'),
        'Potassium': ('19', '39.098', '[Ar] 4s^1', '+1'),
        'Praseodymium': ('59', '140.908', '[Xe] 4f^3 6s^2', '+3, +4'),
        'Promethium': ('61', '145', '[Xe] 4f^5 6s^2', '+3'),
        'Protactinium': ('91', '231.036', '[Rn] 5f^2 6d^1 7s^2', '+4, +5'),
        'Radium': ('88', '226', '[Rn] 7s^2', '+2'),
        'Radon': ('86', '222', '[Xe] 4f^14 5d^10 6s^2 6p^6', '0'),
        'Rhenium': ('75', '186.207', '[Xe] 4f^14 5d^5 6s^2', '+1, +2, +3, +4, +5, +6, +7'),
        'Rhodium': ('42', '102.906', '[Kr] 4d^8 5s^1', '+1, +2, +3, +4, +5, +6'),
        'Roentgenium': ('111', '282', '[Rn] 5f^14 6d^9 7s^2 ', 'Unknown'),
        'Rubidium': ('37', '85.468', '[Kr] 5s^1', '+1'),
        'Ruthenium': ('44', '101.07', '[Kr]4d^7 5s^1', '+3, +4'),
        'Rutherfordium': ('104', '261', '[Rn] 5f^14 6d^2 7s^2', '+4'),
        'Samarium': ('62', '150.36', '[Xe] 4f^6 6s^2', '+2, +3'),
        'Scandium': ('21', '44.956', '[Ar] 3d^1 4s^2', '+3'),
        'Seaborgium': ('106', '269.108', '[Rn] 5f^14 6d^4 7s^2', '+3, +4, +5, +6'),
        'Selenium': ('34', '78.96', '[Ar] 3d^10 4s^2 4p^4', '-2, +4, +6'),
        'Silicon': ('14', '28.086', '[Ne] 3s^2 3p²^2', '-4, +4'),
        'Silver': ('47', '107.868', '[Kr] 4d^105s^1', '+1, +2, +3'),
        'Sodium': ('11', '22.99', '[Ne] 3s¹', '+1'),
        'Strontium': ('38', '87.62', ' [Kr] 5s^2', '+2'),
        'Sulfur': ('16', '32.065', '[Ne] 3s^2 3p^4', '-2'),
        'Tantalum': ('73', '180.948', '[Xe] 4f^14 5d^3 6s^2', '+5'),
        'Technetium': ('43', '98', ' [Kr] 4d^5 5s^2', '+4, +6, +7'),
        'Tellurium': ('52', '127.6', '[Kr] 4d^10 5s^2 5p^4', '−2, +2, +4, +6'),
        'Terbium': ('65', '158.925', '[Xe] 4f^9 6s^2', '+3, +4'),
        'Thallium': ('81', '204.383', '[Xe] 4f^14 5d^10 6s^2 6p^1', '	+1, +3'),
        'Thorium': ('90', '232.038', '[Rn] 6d^2 7s^2', '+1, +2, +3, +4'),
        'Thulium': ('69', '168.934', '[Xe] 4f^13 6s^2', '+3'),
        'Tin': ('50', '118.71', '[Kr] 4d^10 5s^2 5p^2', '+2, +4'),
        'Titanium': ('22', '47.867', '[Ar] 3d^2 4s^2', '+2, +3, +4'),
        'Tungsten': ('74', '183.84', '[Xe] 6s^2 4f^14 5d^4', '+2, +3, +4, +5, +6'),
        'Copernicium': ('112', '285', '[Rn] 5f^14 6d^10 7s^2', '+2'),
        'Livermorium': ('116', '293', '[Rn] 5f^14 6d^10 7s^2 7p^4', 'Unknown'),
        'Moscovium': ('115', '289', '[Rn] 5f^14 6d^10 7s^2 7p^3', 'Unknown'),
        'Flerovium': ('114', '289', '[Rn] 5f^14 6d^10 7s^2 7p^2', 'Unknown'),
        'Tennesine': ('117', '294', '[Rn] 5f^14 6d^10 7s^2 7p^5', 'Unknown'),
        'Ununtrium': ('113', '286', '[Rn] 5f^14 6d^10 7s^2 7p^1', 'Unknown'),
        'Uranium': ('92', '238.029', '[Rn] 5f^3 6d^1 7s^2', '+3, +4, +5, +6'),
        'Vanadium': ('23', '50.924', '[Ar] 3d^3 4s^2', '+2, +3, +4, +5'),
        'Xenon': ('54', '131.293', ' [Kr] 4d^10 5s^2 5p^6', '0'),
        'Ytterbium': ('70', '173.04', ' [Xe] 4f^14 6s^2', '+2, +3'),
        'Yttrium': ('39', '88.906', '[Kr] 4d^1 5s^2', '+3'),
        'Zinc': ('30', '65.38', '[Ar] 3d^10 4s^2', '+2'),
        'Zirconium': ('40', '91.224', '[Kr] 4d^2 5s^2', '+4'),
    }

    # ask for the user to input the element and feature they want, as well as check to make sure they are correct
    element_input = input('What element do you want? Please capitalize the first letter and none others: ')
    feature = input('What Item do you want? Atomic number, Atomic mass, Electron configuration, or Common oxidation states: ')
    
    # utilizing a try/except to account for a potential error if the user inputs an invalid element
    try:
        # While loop to ensure that the feature the user inputs is valid, and to reprompt them if it isn't
        while feature != 'Atomic number' and feature != 'Atomic mass' and feature != 'Electron configuration' and feature != 'Common oxidation states':
            feature = input('''invalid input. Please enter: 'Atomic number', 'Atomic mass', 'Electron configuration', or 'Common oxidation states'. These are case sensitive''')
        if feature == 'Atomic number':
            ind_var = 0
        elif feature == 'Atomic mass':
            ind_var = 1
        elif feature == 'Electron configuration':
            ind_var = 2
        elif feature == 'Common oxidation states':
            ind_var = 3

        # define ind_var: a variable to determine where to index into the lists within the dictionary.    
        ind_var = int(ind_var)

        # put the list of the elements into a seperate variable
        element = atomic_features[element_input]


        # print the correct element and feature.
        if ind_var == 0:
            print('The atomic number for ' + element_input + ' is ' + element[ind_var])
        elif ind_var == 1:
            print('The atomic mass of ' + element_input + ' is ' + element[ind_var])
        elif ind_var == 2:
            print('The Electron configuration of ' + element_input + ' is ' + element[ind_var])
        elif ind_var == 3:
            print('The common oxidation states for ' + element_input + ' are ' + element[ind_var])
        # complete the try/except statement to account for the previously error
    except:
        print('Invalid element.  Note to capitalize the first letter of the element. Please run the program again.')

