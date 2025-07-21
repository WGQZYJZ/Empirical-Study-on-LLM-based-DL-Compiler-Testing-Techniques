'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift_\ntorch.Tensor.bitwise_right_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
print('Input Tensor:')
print(input_tensor)
print('\n')
output_tensor = torch.Tensor.bitwise_right_shift_(input_tensor, 2)
print('Output Tensor:')
print(output_tensor)
print('\n')
print('Input Tensor after inplace operation:')
print(input_tensor)