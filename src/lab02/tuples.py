def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    if isinstance(rec, tuple) == False: return "TypeError"

    if len(rec) != 3:
        return "ValueError"

    if not isinstance(fio, str):
        return ValueError("ФИО должно быть строкой")
    if not isinstance(group, str):
        return ValueError("Группа должна быть строкой")
    if not isinstance(gpa, (float, int)):
        return ValueError("GPA должно быть числом")

    fio = ' '.join(fio.strip().split())
    group = group.strip()

    if not fio:
        return "ValueError"
    if not group:
        return "ValueError"
    
    gpa = float(gpa)

    parts = fio.split()
    if len(parts) < 1:
        return "ValueError"
    surname = parts[0]

    inizial = ''

    if len(parts) >= 2:
        inizial += parts[1][0].upper() + '.'

    if len(parts) >= 3:
        inizial += parts[2][0].upper() + '.'
        
    if len(parts) == 1:
        inizial = ''
    
    if inizial:
        full_name = f"{surname} {inizial}"
    else:
        full_name = surname

    gpa_str = f"{gpa:.2f}"

    return f"{full_name}, гр. {group}, GPA {gpa_str}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "ABB-01", 3.999)))
