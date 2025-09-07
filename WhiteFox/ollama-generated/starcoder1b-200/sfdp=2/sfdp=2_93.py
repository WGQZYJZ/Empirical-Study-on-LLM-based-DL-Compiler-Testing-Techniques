This pattern characterizes scenarios where a query is computed, then scaled by an inverse scale factor (the mean of the squared term in equation 3), then softmax is applied, then dropout is applied, and finally a dot product of the dropout output and a value is computed. This is a typical pattern found in the attention mechanism of Transformer models.


# Reference
1. [https://arxiv.org/pdf/2004.00900.pdf](https://arxiv.org/pdf/2004.00900.pdf)
