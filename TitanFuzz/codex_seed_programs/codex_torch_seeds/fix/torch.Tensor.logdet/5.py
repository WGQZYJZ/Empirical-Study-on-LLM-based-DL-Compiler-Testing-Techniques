'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(torch.Tensor.logdet(_input_tensor))