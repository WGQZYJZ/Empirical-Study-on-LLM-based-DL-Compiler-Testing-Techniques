'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 2)
print(input_tensor)
output_tensor = torch.Tensor.add(input_tensor, input_tensor)
print(output_tensor)