---
title: Huyen - Designing ML Systems (Ch1)
created: Feb 2023
---

This is a really excellent book, and I encourage folks working in data science to go and buy a copy! Some notes to aid my own learning below. 

**Chapter 1 - Overview of machine learning systems**

Overall ML systems are about the real world contexts, and we should think about how all the components fit together. 

- We should think about the systems within which models operate in the real world. 
- MLOps includes deploying, monitoring, and maintaining systems
- ML works best when you can learn patterns from lots of repetitive data
- ML in production is about navigating stakeholder requirements, shifting data, and fast inference with low latency
- ML different from SWE because it focuses more on data and models trained from data

Questions for revision: 

- What are the relevant considerations for implementing ML?
- When does ML work well or less well?
- How does SWE differ from ML?

**Chapter 2 - Introduction to ML Systems design**

Models should exist to support business objectives, so tie the model performance to a business outcome. There will be varying requirements, which come down to building robust and extensible systems, built iteratively. 

Definitions of requirements

- Reliability - performing correctly even in adversity from any possible source, flagging errors. 
- Scalability - bigger models/more users/ more models. Autoscaling avoids wasted resources.  
- Maintainability - make set up and code shared and understandable by others, e.g. SWEs 
- Adaptability - business requirements and data distributions can change over time 

The framing and approach to a problem makes a big difference!

- Framing ML problems - start with a business issue, then dig in, and this might suggest an ML solution, e.g. reducing call times was bottlenecked on predicting department 
- Some of the hardest problems are multi-class classification with high cardinality, and multi-label (varying number of labels) multi-class classification
- Combining multiple goals - you could use composite loss, e.g. $$loss = \alpha * quality loss + \beta * engagement loss$$, but it’s probably easier to train one model for each loss and aggregate their outputs, since then you can tweak $$\alpha, \beta$$ without retraining $$score = \alpha * quality score + \beta * engagement score$$
- Debates continue on whether large data sets or better architecture performs better - some argue lots of data creates bad learners, but most agree with Sutton’s ‘bitter lesson’

Questions for revision: 

- What should ML models optimise for?
    - Things linked to organisational outcomes
- Why should models be built in a maintainable way?
    - There will probably be iterative changes, additions, expansions
    - The code will likely be read and used by others, e.g. SWEs not ML experts
- Does more data mean better?
    - Sutton bitter lesson says yes, but could have inefficient learners
    - Also depends on data quality, and shifting distributions
