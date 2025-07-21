'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frexp\ntorch.Tensor.frexp(_input_tensor, input)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print(input_tensor)
torch.Tensor.frexp(input_tensor)