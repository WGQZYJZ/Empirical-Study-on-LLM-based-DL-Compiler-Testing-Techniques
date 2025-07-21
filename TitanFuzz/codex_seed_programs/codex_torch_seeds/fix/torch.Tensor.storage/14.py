'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage\ntorch.Tensor.storage(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(torch.Tensor.storage(input_tensor))