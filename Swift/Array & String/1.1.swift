/************************************
              cc150
  1.1 judge unique chars in a string
  Assume the string is ASCII

************************************/


func isUniqueChars(str: String) -> Bool {

    var charSet = [Bool](count: 128, repeatedValue: false)

    for charVal in str.utf8 {
    	if charVal < 128 { // For now, it only support judge ASCII chars
    		if charSet[Int(charVal)] {
    		    return false
    		}
    		charSet[Int(charVal)] = true
    	}
    }
    return true
}