'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage\ntorch.Tensor.storage(_input_tensor)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
print(type(input_data))
print(input_data.storage())
print(type(input_data.storage()))