'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
input_tensor = torch.rand(5, 7)
output_tensor = torch.Tensor.tensor_split(input_tensor, 3, dim=1)
print(output_tensor)