'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift_\ntorch.Tensor.bitwise_right_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int32)
print('Input Tensor:\n', input_tensor)
other = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int32)
print('Other Tensor:\n', other)
torch.Tensor.bitwise_right_shift_(input_tensor, other)
print('Result of bitwise_right_shift_: \n', input_tensor)