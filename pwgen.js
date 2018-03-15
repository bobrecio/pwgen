    var reader; //GLOBAL File Reader object for demo purpose only
    var fileText;
    var pwFormat = "%5w.%5w@%3d.%3d"; //  = words.lives@558.742

//TODO:
/*
1. parse the pwFormat
2. create functions for creating parts of the pw

% = delimiter

N = number of characters

w = word
d = digit
a/A = alpha
s = symbol

*/

    //* Check for the various File API support.
    function checkFileAPI() {
        if (window.File && window.FileReader && window.FileList && window.Blob) {
            reader = new FileReader();
            return true; 
        } else {
            alert('The File APIs are not fully supported by your browser. Fallback required.');
            return false;
        }
    }


    //* read text input
    function readText(filePath) {
        var output = ""; //placeholder for text output
        if(filePath.files && filePath.files[0]) {           
            reader.onload = function (e) {
                fileText = e.target.result;
            };//end onload()
            reader.readAsText(filePath.files[0]);
        }//end if html5 filelist support
        else if(ActiveXObject && filePath) { //fallback to IE 6-8 support via ActiveX
            try {
                reader = new ActiveXObject("Scripting.FileSystemObject");
                var file = reader.OpenTextFile(filePath, 1); //ActiveX File Object
                fileText = file.ReadAll(); //text contents of file
                //displayContents(output);
                file.Close(); //close file "input stream"
            } catch (e) {
                if (e.number == -2146827859) {
                    alert('Unable to access local files due to browser security settings. ' + 
                     'To overcome this, go to Tools->Internet Options->Security->Custom Level. ' + 
                     'Find the setting for "Initialize and script ActiveX controls not marked as safe" and change it to "Enable" or "Prompt"'); 
                }
            }       
        }
        else { //this is where you could fallback to Java Applet, Flash or similar
            return false;
        }       
        return true;
    }   

    //* display content using a basic HTML replacement
    function displayContents() {
        
        var thisFile = fileText;
        var txt = "";
        var wordLen = parseInt(document.getElementById("WordLength").value) + 1;
        
        var fileLength = thisFile.split("\n").length;
        
        if (wordLen > 0){
            for (i = Math.round(Math.random() * 100);i < fileLength; i = i + 100){
                document.getElementById('wait').innerHTML = i;
                console.log(i + ": " + thisFile.split("\n")[i]);
                txt += (thisFile.split("\n")[i].length == (wordLen)) ? thisFile.split("\n")[i] + "\n" : "";
            }
            console.log(txt);
        }
        else {
            txt = thisFile;
        }
        
        var txtLength = txt.split("\n").length;
        var rndWord = Math.round(Math.random() * txtLength);
        
        var el = document.getElementById('main');
        el.innerHTML = rndWord + " / " + txt.split("\n")[rndWord]; //display output in DOM
        
        
        
        
    }
