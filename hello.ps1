#Write a function Get-FileSize that does the following:
#Takes a file path as input
#Uses try { } catch { }
#If file exists → return size------->how to return size?
#If file does not exist → show a friendly error message

function Get-FileSize{
    param(
        [parameter(Mandatory=$true)]
        [string]$filepath,
        [parameter(Mandatory=$true)]
        [string]$filename
    )
     try{
    $path = Get-ChildItem -path $filepath\$filename -ErrorAction SilentlyContinue
    $size = [math]::Round($path.Length / 1KB, 2)

    if(-not $path){
        return "file doesnt exist!"
       
    }

    elseif($path){
         write-output "file exists"
        return "$size KB is the size of the file!"
         
    }
    
    }
    catch{
        return "path $filepath or $filename doesnt exists!"
    }
}
Get-FileSize

##to check the order of writing for try catch method and flow of the program:
