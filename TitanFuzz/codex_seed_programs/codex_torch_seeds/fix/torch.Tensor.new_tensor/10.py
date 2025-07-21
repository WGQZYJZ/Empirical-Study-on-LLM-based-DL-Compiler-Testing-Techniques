'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
tensor_new = torch.Tensor.new_tensor(input_tensor, input_tensor)
print(tensor_new)