'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = [1, 2, 3, 4, 5]
output_tensor = torch.Tensor.new_tensor(_input_tensor, data=_input_tensor, dtype=None, device=None, requires_grad=False)
print('output tensor = ', output_tensor)