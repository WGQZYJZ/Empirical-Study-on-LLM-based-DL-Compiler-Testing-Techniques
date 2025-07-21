'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
print('Input tensor:', x)
print('Negative of the input tensor:', torch.neg(x))
print('Negative of the input tensor:', torch.Tensor.negative_(x))
print('Input tensor after calling negative_:', x)