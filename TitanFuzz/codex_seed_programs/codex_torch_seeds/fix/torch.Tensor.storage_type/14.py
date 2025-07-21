'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage_type\ntorch.Tensor.storage_type(_input_tensor)\n'
import torch
input_data = torch.rand(1, 2, 3, 4, 5)
print(torch.Tensor.storage_type(input_data))