'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flipud\ntorch.Tensor.flipud(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor)
flipped_tensor = torch.Tensor.flipud(input_tensor)
print(flipped_tensor)