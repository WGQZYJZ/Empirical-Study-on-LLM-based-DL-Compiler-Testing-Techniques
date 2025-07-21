'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
import torch
input_tensor = torch.arange(12).reshape(3, 4)
output_tensor = torch.Tensor.tensor_split(input_tensor, 2, dim=0)
print(output_tensor)