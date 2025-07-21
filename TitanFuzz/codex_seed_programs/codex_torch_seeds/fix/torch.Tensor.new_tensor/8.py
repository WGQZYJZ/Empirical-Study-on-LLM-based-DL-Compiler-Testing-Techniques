'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.rand(4, 4)
new_tensor = torch.Tensor.new_tensor(input_tensor, data=None, dtype=None, device=None, requires_grad=False)
print(input_tensor)
print(new_tensor)