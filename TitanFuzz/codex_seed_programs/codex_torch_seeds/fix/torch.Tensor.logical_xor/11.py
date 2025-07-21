'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
other_tensor = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
output_tensor = input_tensor.logical_xor(other_tensor)
print('input_tensor: ', input_tensor)
print('other_tensor: ', other_tensor)
print('output_tensor: ', output_tensor)