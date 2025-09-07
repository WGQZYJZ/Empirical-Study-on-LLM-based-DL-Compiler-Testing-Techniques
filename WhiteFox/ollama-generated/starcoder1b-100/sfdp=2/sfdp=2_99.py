This pattern characterizes scenarios where a sequence is broken up into chunks and each chunk contains two tensors `q1` and `k1`. Then these two sequences are concatenated together along the first dimension with the concatenation axis set to `-1`, so that they are aligned according to the length of their respective input tensors. These two tensors are then used in a dot product, which is then multiplied by an inverse scale factor to get the `qk` matrix (see above), and softmax is applied on it to get the `softmax_qk` matrix, which is then multiplied with the dropout output (`dropout_qk`) to get the output. Then the last tensor of these two matrices are concatenated together along the second dimension in a way that corresponds to their respective lengths.

# TODO
- 1) Make it faster.
