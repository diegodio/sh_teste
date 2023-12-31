
def selecao_dia():
    st.text("Selecione um dia")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"])

    ### DOM ###
    lista_horarios_dom = []
    for i in range(0, len(info)):
        lista_horarios_dom += info[i]["dom"]
    lista_horarios_dom = list(set(lista_horarios_dom))
    lista_horarios_dom.remove("")
    lista_horarios_dom.sort()

    with tab1:
        st.text("Selecione um horário")
        tabs_dom = st.tabs(lista_horarios_dom)

        for indice, i in enumerate(lista_horarios_dom):
            lista_paroquias_horario_definido_dom = []
            for j in info:
                if i in info[j]["dom"]:
                    lista_paroquias_horario_definido_dom.append(info[j]["nome"])
            with tabs_dom[indice]:
                for k in lista_paroquias_horario_definido_dom:
                    st.write(k)

    ### SEG ###
    lista_horarios_seg = []
    for i in range(0, len(info)):
        lista_horarios_seg += info[i]["seg"]
    lista_horarios_seg = list(set(lista_horarios_seg))
    try:
        lista_horarios_seg.remove("")
    except:
        pass
    lista_horarios_seg.sort()

    with tab2:
        st.text("Selecione um horário")
        tabs_seg = st.tabs(lista_horarios_seg)

        for indice, i in enumerate(lista_horarios_seg):
            lista_paroquias_horario_definido_seg = []
            for j in info:
                if i in info[j]["seg"]:
                    lista_paroquias_horario_definido_seg.append(info[j]["nome"])
            with tabs_seg[indice]:
                for k in lista_paroquias_horario_definido_seg:
                    st.write(k)

    ### TER ###
    lista_horarios_ter = []
    for i in range(0, len(info)):
        lista_horarios_ter += info[i]["ter"]
    lista_horarios_ter = list(set(lista_horarios_ter))
    try:
        lista_horarios_ter.remove("")
    except:
        pass
    lista_horarios_ter.sort()

    with tab3:
        st.text("Selecione um horário")
        tabs_ter= st.tabs(lista_horarios_ter)

        for indice, i in enumerate(lista_horarios_ter):
            lista_paroquias_horario_definido_ter = []
            for j in info:
                if i in info[j]["ter"]:
                    lista_paroquias_horario_definido_ter.append(info[j]["nome"])
            with tabs_ter[indice]:
                for k in lista_paroquias_horario_definido_ter:
                    st.write(k)

    ### QUA ###
    lista_horarios_qua = []
    for i in range(0, len(info)):
        lista_horarios_qua += info[i]["qua"]
    lista_horarios_qua = list(set(lista_horarios_qua))
    try:
        lista_horarios_qua.remove("")
    except:
        pass
    lista_horarios_qua.sort()

    with tab4:
        st.text("Selecione um horário")
        tabs_qua= st.tabs(lista_horarios_qua)

        for indice, i in enumerate(lista_horarios_qua):
            lista_paroquias_horario_definido_qua = []
            for j in info:
                if i in info[j]["qua"]:
                    lista_paroquias_horario_definido_qua.append(info[j]["nome"])
            with tabs_qua[indice]:
                for k in lista_paroquias_horario_definido_qua:
                    st.write(k)

    ### QUI ###
    lista_horarios_qui = []
    for i in range(0, len(info)):
        lista_horarios_qui += info[i]["qui"]
    lista_horarios_qui = list(set(lista_horarios_qui))
    try:
        lista_horarios_qui.remove("")
    except:
        pass
    lista_horarios_qui.sort()

    with tab5:
        st.text("Selecione um horário")
        tabs_qui= st.tabs(lista_horarios_qui)

        for indice, i in enumerate(lista_horarios_qui):
            lista_paroquias_horario_definido_qui = []
            for j in info:
                if i in info[j]["qui"]:
                    lista_paroquias_horario_definido_qui.append(info[j]["nome"])
            with tabs_qui[indice]:
                for k in lista_paroquias_horario_definido_qui:
                    st.write(k)

    ### SEX ###
    lista_horarios_sex = []
    for i in range(0, len(info)):
        lista_horarios_sex += info[i]["sex"]
    lista_horarios_sex = list(set(lista_horarios_sex))
    try:
        lista_horarios_sex.remove("")
    except:
        pass
    lista_horarios_sex.sort()

    with tab6:
        st.text("Selecione um horário")
        tabs_sex= st.tabs(lista_horarios_sex)

        for indice, i in enumerate(lista_horarios_sex):
            lista_parosexas_horario_definido_sex = []
            for j in info:
                if i in info[j]["sex"]:
                    lista_parosexas_horario_definido_sex.append(info[j]["nome"])
            with tabs_sex[indice]:
                for k in lista_parosexas_horario_definido_sex:
                    st.write(k)

    ### SAB ###
    lista_horarios_sab = []
    for i in range(0, len(info)):
        lista_horarios_sab += info[i]["sab"]
    lista_horarios_sab = list(set(lista_horarios_sab))
    try:
        lista_horarios_sab.remove("")
    except:
        pass
    lista_horarios_sab.sort()

    with tab7:
        st.text("Selecione um horário")
        tabs_sab= st.tabs(lista_horarios_sab)

        for indice, i in enumerate(lista_horarios_sab):
            lista_parosabas_horario_definido_sab = []
            for j in info:
                if i in info[j]["sab"]:
                    lista_parosabas_horario_definido_sab.append(info[j]["nome"])
            with tabs_sab[indice]:
                for k in lista_parosabas_horario_definido_sab:
                    st.write(k)