# Implementation
In general, we first load the generated model into memory by `torch.jit.load`. Next, we get the model input by `torch.jit.trace`. For more details about how to implement this procedure, please refer to [this paper](https://arxiv.org/abs/1812.06475).
# Reference

