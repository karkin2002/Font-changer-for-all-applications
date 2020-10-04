import keyboard,time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'space']
fancyAlphabetLower = ['𝒶', '𝒷', '𝒸', '𝒹', 'ℯ', '𝒻', 'ℊ', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓂', '𝓃', 'ℴ', '𝓅', '𝓆','𝓇', '𝓈', '𝓉', '𝓊', '𝓋','𝓌','𝓍','𝓎','𝓏','space']
fancyAlphabetUpper = ['𝒜', 'ℬ', '𝒞', '𝒟', 'ℰ', 'ℱ', '𝒢', 'ℋ', 'ℐ', '𝒥', '𝒦', 'ℒ', 'ℳ', '𝒩', '𝒪', '𝒫', '𝒬', 'ℛ','𝒮', '𝒯', '𝒰', '𝒱', '𝒲', '𝒳','space']

time.sleep(2)
fancyFont = False
spaces = False 
while True:
    keysPressDown = list(keyboard.get_hotkey_name().split("+")) 
    
    if "f9" in keysPressDown and "ctrl" in keysPressDown:
        fancyFont = False
        spaces = False

    elif "f10" in keysPressDown and "ctrl" in keysPressDown:
        fancyFont = True
        spaces = False
    
    elif "f11" in keysPressDown and "ctrl" in keysPressDown:
        fancyFont = False
        spaces = True

    if fancyFont:
        for eachKeypress in keysPressDown:
            if eachKeypress.lower() in alphabet:

                if eachKeypress != "space":
                    keyboard.press_and_release('backspace')
                    
                    if eachKeypress.isupper():
                        keyboard.write(fancyAlphabetUpper[alphabet.index(eachKeypress.lower())])
                    
                    else:
                        keyboard.write(fancyAlphabetLower[alphabet.index(eachKeypress)])
    elif spaces:
        for eachKeypress in keysPressDown:
            if eachKeypress.lower() in alphabet:
                keyboard.write(" ")