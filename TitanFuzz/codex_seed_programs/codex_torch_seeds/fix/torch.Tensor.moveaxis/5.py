'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randn(3, 4, 5, 6)
print(torch.Tensor.moveaxis(input_tensor, 0, (- 1)))