'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.tensor([[True, True], [False, False], [True, True], [False, False]])
output_tensor = torch.Tensor.bitwise_xor(input_tensor, other)
print('Output tensor: ', output_tensor)