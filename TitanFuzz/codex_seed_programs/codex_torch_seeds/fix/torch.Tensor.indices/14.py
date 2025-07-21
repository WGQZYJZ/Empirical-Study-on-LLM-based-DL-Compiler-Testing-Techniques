'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.indices\ntorch.Tensor.indices(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
indices = input_tensor.indices()
print(indices)