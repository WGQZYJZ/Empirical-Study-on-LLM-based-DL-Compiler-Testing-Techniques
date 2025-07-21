'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
input_tensor = torch.rand(10, 10)
torch.Tensor.tensor_split(input_tensor, indices_or_sections=5, dim=0)