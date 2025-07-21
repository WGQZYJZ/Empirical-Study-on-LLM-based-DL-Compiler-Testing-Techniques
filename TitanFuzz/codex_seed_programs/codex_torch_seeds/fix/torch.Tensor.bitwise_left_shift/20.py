'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.int8)
input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.int8)
print('Input Tensor:\n', input_tensor)
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, 2)
print('Output Tensor:\n', output_tensor)