'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil\ntorch.Tensor.ceil(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
input_data = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]]
input_tensor = torch.Tensor(input_data)
output = input_tensor.ceil()
print('input_tensor:')
print(input_tensor)
print('output:')
print(output)