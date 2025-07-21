'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([[1, 2], [3, 4]])
print('Input tensor: ', input_tensor)
torch.Tensor.neg_(input_tensor)
print('Negative of input tensor: ', input_tensor)
print('Negative of input tensor: ', torch.Tensor.neg(input_tensor))
print('Negative of input tensor: ', torch.neg(input_tensor))