'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other=input_tensor)
print('Input:')
print(input_tensor)
print('Output:')
print(output_tensor)