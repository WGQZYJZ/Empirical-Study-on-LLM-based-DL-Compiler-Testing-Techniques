'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_equal\ntorch.Tensor.less_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
other = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output = torch.Tensor.less_equal(input_tensor, other)
print('Output: ', output)