def individual_serial(affiliate)->dict:
    return {
        "id":str(affiliate["_id"]),
        "name": affiliate["name"],
        "email": affiliate["email"],
    }

def lis