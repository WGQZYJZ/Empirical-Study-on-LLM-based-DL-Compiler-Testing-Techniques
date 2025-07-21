'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
torch.Tensor.dsplit(input_tensor, 2)