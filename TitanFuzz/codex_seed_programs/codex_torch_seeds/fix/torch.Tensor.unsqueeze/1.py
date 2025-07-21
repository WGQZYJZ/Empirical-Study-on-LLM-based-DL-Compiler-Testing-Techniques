'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
output_tensor = input_tensor.unsqueeze(dim=0)
print(output_tensor)