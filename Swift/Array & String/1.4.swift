/************************************
              cc150
        1.4 replace spaces

************************************/


func replaceSpaces(str: String) -> String {

    var newStr = String()
    for char in str {
        if char == " " {
            newStr += "%20"
        } else {
            newStr += char
        }
    }

    return newStr
}