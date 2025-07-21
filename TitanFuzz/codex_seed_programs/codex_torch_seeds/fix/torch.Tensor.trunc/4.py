'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
_input_tensor = torch.rand(4, 4)
print(torch.Tensor.trunc(_input_tensor))