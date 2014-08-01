/************************************
              cc150
  1.1 judge unique chars in a string
  Assume the string is ASCII

************************************/


func permutation(string1: String, string2: String) -> Bool {

    var string1 = string1.stringByReplacingOccurrencesOfString(" ", withString: "")

    var string2 = string2.stringByReplacingOccurrencesOfString(" ", withString: "")

    if countElements(string1) != countElements(string2) {
        return false
    }

    var charSet = [Int](count: 128, repeatedValue: 0)

    for charVal in string1.utf8 {
        ++charSet[Int(charVal)]
    }

    for charVal in string2.utf8 {
        if --charSet[Int(charVal)] < 0 {
            return false
        }
    }

    return true
}