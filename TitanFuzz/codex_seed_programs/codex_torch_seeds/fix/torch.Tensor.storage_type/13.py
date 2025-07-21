'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage_type\ntorch.Tensor.storage_type(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor.storage_type())