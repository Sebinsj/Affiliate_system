def individual_serial(affiliate) -> dict:
    return {
        "id"    :  str(affiliate["_id"]),
        "name"  :  affiliate["name"],
        "email" :  affiliate["email"],
    }

def list_serial(affiliates)->list:
    return[individual_serial(affiliate) for affiliate ]