'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.uint8)
other = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.uint8)
output_tensor = torch.Tensor.bitwise_xor(input_tensor, other)
print('Input:')
print(input_tensor)
print('Output:')
print(output_tensor)