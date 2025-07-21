'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor_1 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
input_tensor_2 = torch.Tensor([[7, 8, 9], [10, 11, 12]])
output_tensor = input_tensor_1.subtract(input_tensor_2)
print('Output tensor:', output_tensor)
output_tensor = input_tensor_1.subtract(input_tensor_2, alpha=2)
print('Output tensor with alpha = 2:', output_tensor)