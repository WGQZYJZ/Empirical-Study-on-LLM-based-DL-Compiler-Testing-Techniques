'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
print(torch.Tensor.neg_(input_tensor))