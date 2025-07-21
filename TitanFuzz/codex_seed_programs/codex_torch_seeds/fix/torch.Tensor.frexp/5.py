'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frexp\ntorch.Tensor.frexp(_input_tensor, input)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor.frexp())