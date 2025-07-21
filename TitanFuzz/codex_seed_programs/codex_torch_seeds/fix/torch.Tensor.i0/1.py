'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.i0\ntorch.Tensor.i0(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = torch.Tensor.i0(input_tensor)
print('The input tensor type is: ', type(input_tensor))
print('The output tensor type is: ', type(output_tensor))