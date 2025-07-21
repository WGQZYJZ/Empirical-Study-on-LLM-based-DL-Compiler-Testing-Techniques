'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sigmoid_\ntorch.Tensor.sigmoid_(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(3, 3)
print(input_tensor)
torch.Tensor.sigmoid_(input_tensor)
print(input_tensor)
print(torch.sigmoid(input_tensor))
torch.sigmoid_(input_tensor)
print(input_tensor)
print(torch.sigmoid(input_tensor))