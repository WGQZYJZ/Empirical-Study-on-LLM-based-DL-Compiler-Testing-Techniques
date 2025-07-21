'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
output_tensor = input_tensor.sub(other)
print(input_tensor)
print(other)
print(output_tensor)