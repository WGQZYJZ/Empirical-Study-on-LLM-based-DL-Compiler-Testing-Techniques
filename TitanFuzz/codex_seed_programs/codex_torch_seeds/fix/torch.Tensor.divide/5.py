'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.FloatTensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.divide(2))
print(input_tensor.div(2))
print(torch.div(input_tensor, 2))
print(torch.div(2, input_tensor))