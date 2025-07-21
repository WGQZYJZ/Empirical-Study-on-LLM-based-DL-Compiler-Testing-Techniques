'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atan_\ntorch.Tensor.atan_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3, 3)
atan_input_tensor = torch.Tensor.atan_(input_tensor)
print(atan_input_tensor)