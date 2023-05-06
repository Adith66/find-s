# find-S algorithm
This repository consists of find-S code in python.

Introduction : 
The find-S algorithm is a basic concept learning algorithm in machine learning. The find-S algorithm finds the most specific hypothesis that fits all the positive examples. We have to note here that the algorithm considers only those positive training example. The find-S algorithm starts with the most specific hypothesis and generalizes this hypothesis each time it fails to classify an observed positive training data. Hence, the Find-S algorithm moves from the most specific hypothesis to the most general hypothesis. 

Important Representation : 
 
1.? indicates that any value is acceptable for the attribute.
2.specify a single required value ( e.g., Cold ) for the attribute.
3.ϕindicates that no value is acceptable.
4.The most general hypothesis is represented by: {?, ?, ?, ?, ?, ?}
5.The most specific hypothesis is represented by: {ϕ, ϕ, ϕ, ϕ, ϕ, ϕ}

Steps Involved In Find-S : 
1.Start with the most specific hypothesis. 
 h = {ϕ, ϕ, ϕ, ϕ, ϕ, ϕ}
2.Take the next example and if it is negative, then no changes occur to the hypothesis.
3.If the example is positive and we find that our initial hypothesis is too specific then we update our current hypothesis to a general condition.
4.Keep repeating the above steps till all the training examples are complete.
5.After we have completed all the training examples we will have the final hypothesis when can use to classify the new examples.

algorithm:

1. Initialize h to the most specific hypothesis in H
2. For each positive training instance x
    For each attribute constraint a, in h
        If the constraint a, is satisfied by x
        Then do nothing
        Else replace a, in h by the next more general constraint that is satisfied by x
3. Output hypothesis h 
