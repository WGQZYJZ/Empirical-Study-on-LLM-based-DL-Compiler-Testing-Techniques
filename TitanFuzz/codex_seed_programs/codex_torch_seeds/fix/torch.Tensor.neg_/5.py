'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
print('Negative of Input Tensor: ', input_tensor.neg())
print('Negative of Input Tensor in place: ', input_tensor.neg_())