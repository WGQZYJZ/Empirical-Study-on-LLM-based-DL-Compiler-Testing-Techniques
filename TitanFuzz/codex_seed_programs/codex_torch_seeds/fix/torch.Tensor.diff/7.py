'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
data = torch.randn(10)
print(data)
data_diff = data.diff()
print(data_diff)
data_diff_2 = data.diff(2)
print(data_diff_2)
data_diff_3 = data.diff(3)
print(data_diff_3)
data_diff_4 = data.diff(4)
print(data_diff_4)