'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
_input_list = [1, 2, 3]
_input_tensor = torch.Tensor(_input_list)
print('The dimension of input tensor is: ', _input_tensor.ndimension())