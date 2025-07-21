'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.int32)
print('Input Tensor:')
print(input_tensor)
other = torch.tensor(2)
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, other)
print('Output Tensor:')
print(output_tensor)