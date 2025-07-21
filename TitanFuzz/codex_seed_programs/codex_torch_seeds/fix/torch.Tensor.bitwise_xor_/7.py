'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor_\ntorch.Tensor.bitwise_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False], [True, True]], dtype=torch.bool)
other = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
output = torch.Tensor.bitwise_xor_(input_tensor, other)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('output: ', output)