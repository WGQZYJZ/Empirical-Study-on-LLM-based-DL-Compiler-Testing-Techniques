'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False], [True, True]])
other = torch.tensor([[True, True], [False, True]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other)
print(output_tensor)