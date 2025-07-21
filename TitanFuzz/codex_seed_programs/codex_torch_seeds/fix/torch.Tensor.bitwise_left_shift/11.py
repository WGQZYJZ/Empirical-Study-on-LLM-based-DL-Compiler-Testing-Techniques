'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
other = torch.Tensor([[1, 2, 3], [4, 5, 6]])
bitwise_left_shift_result = torch.Tensor.bitwise_left_shift(input_tensor, other)
print(bitwise_left_shift_result)