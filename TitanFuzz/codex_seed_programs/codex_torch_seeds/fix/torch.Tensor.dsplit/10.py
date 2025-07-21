'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
import torch
input_tensor = torch.randn(4, 6)
print(torch.Tensor.dsplit(input_tensor, 2))
print(torch.Tensor.dsplit(input_tensor, [2, 4]))