'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.indices\ntorch.Tensor.indices(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
indices = input_tensor.indices()
print(indices)