'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
data = torch.randn(2, 3)
output_tensor = torch.Tensor.new_tensor(input_tensor, data)
print(output_tensor)