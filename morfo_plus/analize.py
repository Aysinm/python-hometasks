from pymystem3 import Mystem

def get_glagols(text):
    m = Mystem()
    a_list = m.analyze(text)
    all_good_words = []
    glagols = []
    perehod = []
    neperehod = []
    sov = []
    nesov = []
    for i in a_list:
        # i - Это словарь
        # если там есть analisis - значит нормальное слово
        if 'analysis' in i:
            all_good_words.append(i)
            #нам нужен только анализ
            analisis = i['analysis']
            #analisis - это список, но там только один элемент, берем его
            elem = analisis[0]
            #там нам нужен gr и lex для глаголов
            #сначала возьмем gr
            gr = elem['gr']
            #print(elem)
            if 'V,' in gr:
                # значит это глагол
                #добавляем только его лемму
                lex = elem['lex']
                glagols.append(lex)
                if 'несов' in gr:
                    nesov.append(lex)
                else:
                    sov.append(lex)
                if 'нп=' in gr:
                    neperehod.append(lex)
                else:
                    perehod.append(lex)

    print(glagols)
    print(sov)
    print(nesov)
    print(neperehod)
    print(perehod)
    #делаем частотный анализ
    res_ch = {}
    for g in glagols:
        if g in res_ch:
            res_ch[g] += 1
        else:
            res_ch[g] = 1
    #отсортируем частотный словарь по частоте
    g_ches = sorted(res_ch.items(), key=lambda x: x[1], reverse=True)
    #возвращаем результат
    result = {
        'g_count': len(glagols),
        'g_p': (float(len(glagols))/float(len(all_good_words)))*100,
        'g_perehod': len(perehod),
        'g_neperehod': len(neperehod),
        'g_sov': len(sov),
        'g_nesov': len(nesov),
        'g_ches': g_ches
    }
    return result

