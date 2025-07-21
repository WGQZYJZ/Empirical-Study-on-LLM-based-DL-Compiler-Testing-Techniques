'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(_input_tensor, other)\n'
import torch
input_data = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
result = torch.Tensor.logical_xor(input_data, input_data)
print(result)