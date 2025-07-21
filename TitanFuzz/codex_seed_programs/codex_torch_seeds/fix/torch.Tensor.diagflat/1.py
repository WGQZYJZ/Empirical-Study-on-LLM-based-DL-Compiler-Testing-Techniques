'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagflat\ntorch.Tensor.diagflat(_input_tensor, offset=0)\n'
import torch
input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.diagflat(input_tensor, offset=0)
print(output_tensor)