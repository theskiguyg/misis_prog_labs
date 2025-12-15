def format_record(rec: tuple[str, str, float]) -> str:

    name_processing = rec[0].strip().split()
    final_name = ""
    if len(name_processing) == 1:
        final_name = f"{name_processing[0][0].upper()}{name_processing[0][1:]}"
    elif len(name_processing) == 2:
        final_name = f"{name_processing[0][0].upper()}{name_processing[0][1:]} {name_processing[1][0:1].upper()}."
    elif len(name_processing) == 3:
        final_name = f"{name_processing[0][0].upper()}{name_processing[0][1:]} {name_processing[1][0:1].upper()}. {name_processing[2][0:1].upper()}."
    else:
        return ValueError

    group = ""
    group_processing = rec[1].strip()
    if group_processing == "":
        return ValueError
    else:
        group = group_processing

    gpa = float(rec[2])
    if not (isinstance(gpa, float)):
        return TypeError

    return f"{final_name}, гр. {group}, GPA: {gpa:.2f}"


print(format_record(()))
