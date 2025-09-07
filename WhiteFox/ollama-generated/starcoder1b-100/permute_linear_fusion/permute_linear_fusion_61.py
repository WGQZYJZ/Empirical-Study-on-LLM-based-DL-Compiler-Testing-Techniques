This pattern characterizes scenarios where the tensor method 'permute' is invoked first, and then the `torch.nn.functional.linear` function is invoked on the permuted tensor.
The permute method is invoked on an input tensor with more than 2 dimensions, and it swaps the last two dimensions of this tensor. This modified tensor is then used as the main input for the linear function.

## References
[1] <NAME>, <NAME> (2020). [A New Deep Learning Model](https://arxiv.org/abs/1804.06537)

