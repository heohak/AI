# Probabilistic Programming Analysis: Battery Pack

This project utilizes probabilistic programming to analyze scenarios involving a pack of AA batteries.
We employ generative models to estimate probabilities under certain conditions. The analysis was conducted using WebPPL, a probabilistic programming language.

#### Problem 1:
````
var genA = function () {
  var battery1 = flip(0.9);
  var battery2 = flip(0.9);
  var battery3 = flip(0.9);
  var battery4 = flip(0.9);
  
  // Ensure at least one battery is empty
  var atLeastOneEmpty = !battery1 || !battery2 || !battery3 || !battery4;
  condition(atLeastOneEmpty);

  // Count how many batteries are full
  var fullBatteries = battery1 + battery2 + battery3 + battery4;
  
  // We're interested in the cases where exactly three batteries are full
  return fullBatteries === 3;
}

viz(Infer({method: "enumerate"}, genA));

````

Result:

![img.png](img.png)

Probability of exactly three batteries being full: 84.79%




#### Problem 2:
````
var gen = function() {
    var battery2 = flip(0.9);
    var battery3 = flip(0.9);
    var battery4 = flip(0.9);
    var pack = [false, battery2, battery3, battery4];
    return _.countBy(pack, _.identity).false === 1;
};

viz(Infer({method: "rejection", samples: 10000}, gen));
````

Result:

![img_1.png](img_1.png)

Probability of the remaining three batteries being full: 73.41%

