'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ne_\ntorch.Tensor.ne_(_input_tensor, other)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
tensor_data = [[1, 2], [3, 4]]
tensor_data = torch.Tensor(tensor_data)
tensor_data.ne_(tensor_data)
print('tensor_data:', tensor_data)