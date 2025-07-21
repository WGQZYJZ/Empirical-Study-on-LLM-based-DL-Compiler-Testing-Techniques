'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randint(0, 2, size=(2, 3))
print('Input Tensor:\n', input_tensor)
torch.Tensor.bitwise_left_shift_(input_tensor, 2)
print('Output Tensor:\n', input_tensor)