'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
other = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
torch.Tensor.logical_xor_(_input_tensor, other)
print(_input_tensor)