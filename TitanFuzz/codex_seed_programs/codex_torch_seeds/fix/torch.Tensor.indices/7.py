'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.indices\ntorch.Tensor.indices(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4)
indices = torch.Tensor.indices(input_tensor)
print(indices)