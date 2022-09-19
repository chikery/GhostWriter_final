def assemble(*args):
    return " ".join(args)


def NP(T,N):
    return assemble(T,N)

def VP(Verb,NP):
    return assemble(Verb, NP)

def sentence(NP,VP):
    return assemble(NP,VP)


def loop(X):

    T = ['the', 'their', 'our', 'his', 'her']
    N = ['Deaths', 'Due', 'COVID-19', 'World', 'Reaches', 'Million', 'People', 'JAKARTA', 'world', 'deaths', 'mark', 'Friday', 'Reuters', 'data', 'world', 'year', 'deaths', 'months', 'average', 'deaths', 'worldwide', 'week', 'deaths', 'minute', 'half', 'death', 'toll', 'week', 'United', 'States', 'Russia', 'Brazil', 'Mexico', 'India', 'death', 'toll', 'US', 'Friday', 'world', 'COVID-19', 'cases', 'hospitalizations', 'US', 'country', 'health', 'authorities', 'spike', 'winter', 'people', 'indoors', 'day', 'Russia', 'deaths', 'country', 'figure', 'year', 'pandemic', 'South', 'America', 'region', 'mortality', 'rate', 'world', 'percent', 'deaths', 'region', 'North', 'America', 'Eastern', 'Europe', 'account', 'percent', 'deaths', 'Reuters', 'analysis', 'death', 'toll', 'India', 'countries', 'Delta', 'variant', 'average', 'day', 'vaccination', 'program', 'Delta', 'world', 'variant', 'coronavirus', 'member', 'countries', 'World', 'Health', 'Organization', 'WHO', 'variants', 'vaccination', 'rates', 'levels', 'countries', 'World', 'attention', 'days', 'efforts', 'share', 'vaccines', 'countries', 'people', 'dose', 'time', 'people', 'countries', 'doses', 'half', 'world', 'population', 'dose', 'COVID-19', 'vaccine', 'World', 'Data', 'week', 'time', 'COVAX', 'program', 'doses', 'countries', 'vaccination', 'rates', 'vaccine', 'program', 'January', 'vaccine', 'countries', 'proportion', 'population', 'Director-General', 'WHO', 'recording', 'week', 'conference', 'presentation', 'WHO', 'website', 'Germany', 'deaths', 'Germany', 'country', 'threshold', 'figures', 'country', 'Robert', 'Koch', 'Institute', 'people', 'COVID-19', 'number', 'name', 'person', 'year', 'Kerstin', 'father', 'COVID-19', 'DW', 'days', 'hospital', 'bed', 'forehead', 'hand', 'Kerstin', 'Düsseldorf', '—', 'kilometers', 'miles', 'parents', 'Berlin', 'virus', 'infectiousness', 'distancing', 'restrictions', 'hospital', 'visit', 'Kerstin', 'daughter', 'choice', 'goodbye', 'father', 'son', 'car', 'drove', 'Berlin', 'minutes', 'plastic', 'father', 'day', 'hospital', 'tuberculosis', 'coronavirus', 'doctor', 'Germany', 'people', 'figures', 'Robert', 'Koch', 'Institute', 'Disease', 'Control', '—', 'illness', 'Kerstin', 'memories', 'laughter', 'tears', 'father', 'life', 'randomness', 'death', 'Caregivers', 'Nurses', 'pandemic', 'people', 'ventilators', 'health', 'deteriorating', 'afraid', 'dying', 'caregiver', 'Rita', 'Kremers', 'DW', 'colleagues', 'virus', 'ICU', 'weeks', 'infection', 'person', 'COVID', 'death', 'mourning', 'Germany', 'People', 'deaths', 'homes', 'hospitals', 'Germany', 'restrictions', 'contact', 'behind', 'ambulance', 'hospital', 'doctors', 'Silke', 'Kleibömer', 'day', 'father', 'hospital', '—', 'April', 'birthday', 'daughter', 'life', 'end', 'Hans-Jürgen', 'disease', 'oxygen', 'years', 'family', 'paramedics', 'hospital', 'care', 'unit', 'ICU', 'days', 'phase', 'coronavirus', 'hospitals', 'nursing', 'homes', 'restrictions', 'bans', 'contact', 'loosening', 'rules', 'summer', 'stricter', 'infection', 'rates', 'State', 'governments', 'individuals', 'hospitals', 'nursing', 'homes', 'testing', 'regulations', 'restrictions', 'patients', 'people', 'Silke', 'Kleibömer', 'Heinz-Jürgen', 'hospital', 'doctors', 'pneumonia', 'Silke', 'Kleibömer', 'father', 'telephone', 'day', 'seconds', '—', 'breath', 'Anyone', 'shortness', 'breath', 'knows', "'He", 'Silke', 'mother', 'hospital', 'family', 'doctor', 'time', 'relative', 'father', 'care', 'one', 'family', 'Silke', 'Kleibömer', 'nursing', 'service', 'attitudes', 'time', 'phone', 'call', 'Indignant', 'Kleibömer', 'ICU', 'doctor', 'mother', 'father', 'faculties', '…', 'Silke', 'Kleibömer', 'stops', 'eye', 'dad', 'Visits', 'ICU', 'person', 'maximum', 'hour', 'day', 'staff', 'case', 'May', 'alarms', 'father', 'bed', 'call', 'hospital', 'Hurry', 'Silke', 'Kleibömer', 'mother', 'hospital', 'side', 'wife', 'daughter', 'grandchildren', 'Papa', 'ICU', 'staff', 'doctor', 'colleague', 'decides', 'day', 'family', 'hand', 'father', 'relief', 'face', 'coronavirus', 'victims', 'COVID-19', 'people', 'COVID-19', 'coronavirus', 'hit', 'Germany', 'story', 'fates', 'individuals', 'families', 'thing', 'COVID-19', 'people', 'circumstances', 'death', 'isolation', 'doors', 'Reporters', 'Nicola', 'Albrecht', 'Susann', 'von', 'Lojewski', 'COVID-19', 'experience', 'death', 'people', 'ones', 'Manu', 'fiancée', 'Brittanya', 'COVID-19', 'Instagram', 'sickbed', 'Brittanya', 'fans', 'confidence', 'battle', 'virus', 'days', 'Ralf', 'Brepohl', 'mother', 'one', 'care', 'workers', 'people', 'patients', 'COVID-19', 'COVID-19', 'limit', 'Nurse', 'Celine', 'Pinkau', 'Senftenberg', 'moment', 'patient', 'fond', 'body', 'bag', 'Where', 'humanity', 'dignity', '’', 'Hospital', 'chaplains', 'Stefan', 'Pfeifer', 'family', 'members', 'goodbye', 'ones', 'toll', 'film', 'COVID-19', 'death', 'rituals', 'dignity', 'dying', 'time', 'coronavirus', 'death', 'toll', 'COVID-19', 'Monday', 'years', 'crisis', 'countries', 'ones', 'health', 'care', 'systems', 'United', 'States', 'European', 'Union', 'Britain', 'Brazil', '—', 'countries', 'account', 'one-eighth', 'world', '’', 'population', 'half', 'deaths', 'U.S.', 'lives', 'nation', '“', 'moment', 'lifetime']
    Verb = ['crossed', 'bracing', 'trending', 'during', 'dropped', 'launched', 'found', 'received', 'moans', 'according', 'is', 'telling', 'stroke', 'remember', 'recalls', 'spend', 'drove', 'suffered', 'mourning', 'struggling', 'knew', 'devastating', 'nursing', 'recalling','rushed', 'dying', 'turning', 'seeming', 'taken', 'pushing', 'making', 'vaccinnated', 'oppose', 'claimed', 'criticized', 'refused', 'climbing', 'going', 'accounting', 'imposes', 'struggles', 'confined', 'lacking', 'developing']

    import random as ran

    for i in range(X):
        N1, N2 = ran.choice(N), ran.choice(N)
        T1, T2 = ran.choice(T), ran.choice(T)
        Verb1 = ran.choice(Verb)

        NP1 = NP(T1, N1)
        NP2 = NP(T2, N2)
        VP1 = VP(Verb1, NP2)

        print(sentence(NP1,VP1))

loop(1000)
