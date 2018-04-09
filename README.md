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

### timidity++ => 2.13.1

windows :  
[download timidity++ windows](https://sourceforge.net/projects/timidity/files/TiMidity%2B%2B/TiMidity%2B%2B-CVS/)  
After download, add timidity folder to %PATH%

ubuntu :  
```sudo apt-get install timidity```

mac :  
install homebrew if you haven't installed:  
```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```  
install timidity++  
```brew install timidity```

### ffmpeg

windows :  
[download ffmpeg](https://ffmpeg.zeranoe.com/builds/)  
After download, add ffmpeg folder to %PATH%

ubuntu :  
```sudo apt-get install ffmpeg```

mac :  
```brew install ffmpeg```

## install mimi
```git clone https://github.com/exeex/mimi.git```  
```cd mimi```  
```python setup.py install```

if you wish not to install this package into the site-package folder,  
rather than link the package to the folder you just download, you can install in this way:  
```python setup.py develop```

如果你有修改程式的需求，可以用develop方式安裝，安裝後檔案會透過關聯的方式，關聯到你下載的那個資料夾，而不是裝到site-packages裡面
以便直接修改



