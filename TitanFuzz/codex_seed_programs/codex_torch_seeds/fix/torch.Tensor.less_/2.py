'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_\ntorch.Tensor.less_(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.less_(input_tensor, 0)
print(input_tensor)
print(output_tensor)