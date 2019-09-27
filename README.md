# Image Reconstruction
Using optimization algorithms for reconstructing an image from a set of basic shapes. 

Currently supported algorithms: Genetic Algorithm
Currently supported shapes: Circle, Triangle

Tested on Ubuntu 18.10 & python 3.7.3
## Usage

###Create and use virtual env:
```$xslt
virtualenv -p `which python3` venv
source venv/bin/activate
```

###Install dependencies:
```$xslt
pip install -r requirements.txt
```

###test:
```$xslt
pytest
```

###Install as package
```$xslt
pip install -U .
```

###Run
```$xslt
reconstruct --help
reconstruct GeneticAlgo --help
reconstruct --image ./data/monaliza.jpg --shape Triangle GeneticAlgo --max-generations 10000 --number-of-shapes 50
```
