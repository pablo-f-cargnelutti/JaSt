# JaSt - JS AST-Based Analysis Replication

This work is based on [DIMVA'18 paper: "JaSt: Fully Syntactic Detection of Malicious (Obfuscated) JavaScript"](https://swag.cispa.saarland/papers/fass2018jast.pdf).  
The original intention of this project was to fulfill the the requirement for the final project of 
CAP 6135: Malware and Software Vulnerability Analysis of University of Central Florida. 

## Reproduce classification experiment
- Besides Python 3, run the given in `install.sh` (if you are under Windows make sure you install those dependencies)
- Unzip `dataset.zip`
- We will use the provided trained model under `Classification/model_full`
- For Benign sample classification: 
- - `python3 clustering/classifier.py --d dataset/test/benign --l benign --m Classification/model_full`
- For Malicious sample classification: 
- - `python3 clustering/classifier.py --d dataset/test/malicious --l malicious --m Classification/model_full`

### Outputs
You should see the list of files and its classification result i.e.(benign or malicious) and a summary 
with accuracy of the classification and False Positive (FP), False Negative (FN) and True Negative (TN) rates.  
Example output of malicious classification execution:
```
...
dataset/test/malicious/20160215_b0025224eb9c4aa78ff1226a8624fa3d.js: benign
dataset/test/malicious/20160428_182868cad5bcb428e1b2fbdb5a440e2d.js: malicious
> Name: labelPredicted
Detection: 0.9563409563409564
TP: 460, FP: 0, FN: 21, TN: 0

```

### Crawler
This is a tool able to extract and store all the JS files that are in a website. 
The crawler takes two inputs, a .txt file with the list of websites and the folder name to store the extracted JS files.

Here an example of how to use it with a provided test file (crawler_test_websites.txt).

`python3 crawling/crawler.py crawling/crawler_test_websites.txt crawling/crawler_test_js`

You should see the js files from those sites under `crawling/crawler_test_js` created folder. 