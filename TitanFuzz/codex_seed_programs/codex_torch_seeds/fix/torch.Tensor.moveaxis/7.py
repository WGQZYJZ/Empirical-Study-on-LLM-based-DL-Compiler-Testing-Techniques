'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
print(input_tensor)
out_tensor = input_tensor.moveaxis(0, (- 1))
print(out_tensor)