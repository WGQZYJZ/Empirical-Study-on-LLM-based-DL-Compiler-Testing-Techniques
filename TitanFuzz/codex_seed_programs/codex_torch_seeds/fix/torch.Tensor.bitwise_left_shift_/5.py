'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor:\n{}'.format(input_tensor))
left_shift_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, 2)
print('Tensor after left shift:\n{}'.format(left_shift_tensor))