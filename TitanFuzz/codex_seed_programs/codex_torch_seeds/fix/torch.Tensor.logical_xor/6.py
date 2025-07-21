'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.tensor([[True, False], [True, False], [False, True], [True, False]])
result = input_tensor.logical_xor(other)
print(result)