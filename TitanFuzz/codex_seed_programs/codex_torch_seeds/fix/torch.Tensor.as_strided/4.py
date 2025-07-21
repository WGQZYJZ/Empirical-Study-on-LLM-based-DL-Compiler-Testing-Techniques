'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_strided\ntorch.Tensor.as_strided(_input_tensor, size, stride, storage_offset=0)\n'
import torch
from torch.autograd import Variable
input_tensor = torch.rand(5, 7)
print(input_tensor)
output_tensor = torch.Tensor.as_strided(input_tensor, (3, 3), (4, 4))
print(output_tensor)