def CG_urgent_attention_MS_indicators():
    # guidelines urgent attention indicator
    BP_UA_indicators = {
        "BP": '>=160/110',
    }
    CG_urgent_attention_MS_indicators = {
        "status_or_numberofWeeks": 'Yes',
        "Fever": 'Yes',
        "BP": '>=140/90',
        "bleeding": 'Yes',
        "convulsion": 'Yes',
        "headache": 'Yes',
        "blurredvision": 'Yes',
        "abdominalPain": 'Yes',
        "proteinuria": '>1+',
        "temprature": '>=38°C',
        "weakeness": 'Yes',
        "backpain": 'Yes',
        "breathingDifficulty": 'Yes',
        "swollenPainfulCalf": 'Yes',
        "vaginalBleeding": 'Yes',
        "decrease_or_absentof_fetalMovement": 'Yes',
        "painfulContractionLessthan37wks": 'Yes',
        "suddenGushofClear_or_pale": 'Yes',
        "cervical": 'Yes',
        "chorioamnionitis": 'Yes',
        "pain": 'Yes',
        "vaginaldischarge": 'Yes',
        "rh_negative": 'Yes',
        "pulse": 'Yes',
    }
    return CG_urgent_attention_MS_indicators, BP_UA_indicators
