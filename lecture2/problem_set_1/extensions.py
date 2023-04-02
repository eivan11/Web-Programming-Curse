def check_type(doc):
    type = ["gif", "jpg", "jpeg", "png" , "pdf" , "txt", "zip" ]
    doc = doc.split(".")
    if len(doc) == 1:
        return "application/octet-stream"
    else:
        if doc[1] in type:
            if doc[1] == "gif" or doc[1] == "jpg" or doc[1] == "jpeg" or doc[1] == "png":
                return f"image/{doc[1]}"
            else :
                match(doc[1]):
                    case "pdf": return "application/pdf"
                    case "txt": return "text/plain"
                    case "zip": return "application/zip"
                    case _: return "application/octet-stream"
                    
       


def main():
    print(check_type(input("File name: ")))

if __name__ == "__main__":
    main()