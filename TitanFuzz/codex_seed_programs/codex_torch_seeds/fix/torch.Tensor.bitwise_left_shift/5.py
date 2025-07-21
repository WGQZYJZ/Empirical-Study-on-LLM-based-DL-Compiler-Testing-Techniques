'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.Tensor([[1, 2], [3, 4]])
other = torch.Tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, other)
print(output_tensor)