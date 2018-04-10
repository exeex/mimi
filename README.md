# mimi
a cross-platform python library for midi to wav, generation, visualization, which is design for machine learning  
一個跨平台的midi撥放器、轉檔器、產生器，並包含一個midi visualizer。 供機器學習使用。

features:
* midi to mp3
* midi to numpy array
* midi to json
* midi to png
* random midi generator
* visualization of midi (piano roll)

future works
* better midi generator
* midi to music xml & xml to midi
* mp3 to midi 

# installation

## install prerequisite
* timidity++ => 2.13.1
* ffmpeg

### Windows
[download timidity++](https://sourceforge.net/projects/timidity/files/TiMidity%2B%2B/TiMidity%2B%2B-CVS/)  
[download ffmpeg](https://ffmpeg.zeranoe.com/builds/)  
After download, add ffmpeg & timidity folder to %PATH%  
You can create a folder C:\bin, and put only ffmpeg.exe, ffplay.exe and timidity.exe inside  
Then set C:\bin to %PATH%  

### ubuntu
```sudo apt-get install timidity ffmpeg```  

### mac
Install homebrew if you haven't installed. In terminal, input:  
```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```  
install timidity++  & ffmpeg:  
```brew install timidity ffmpeg```  

## install mimi
 
 cd to mimi folder. in terminal, input:
```python setup.py install```  

if you wish not to install this package into the site-package folder,  
rather than link the package to the folder you just download, you can install in this way:  
```python setup.py develop```




