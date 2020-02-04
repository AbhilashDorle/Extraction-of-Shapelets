# Extraction-of-Shapelets
Shapelets are Time series subsequences which are in a way maximally representative of class. Shapelets help us in classifying the Time series efficiently 

# Method

I perform Time Series Clustering before applying the TS learn package to extract the shapelets. Clustering is performed so as not to miss any important patterns in the dataset, which may be eventually extracted as shapelets.

Time Series Classification is performed with a little modification in the method provided in " Clustering of Time Series using Unsupervised-Shapelets, Zakaria et al."

Shapelets are extracted according to the tslearn package
