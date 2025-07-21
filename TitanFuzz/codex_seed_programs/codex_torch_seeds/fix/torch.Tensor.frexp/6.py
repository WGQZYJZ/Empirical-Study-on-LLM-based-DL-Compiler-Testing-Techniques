'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frexp\ntorch.Tensor.frexp(_input_tensor, input)\n'
import torch
input_tensor = torch.Tensor([(- 1), 0, 1])
frexp_output = torch.Tensor.frexp(input_tensor)
print('The input tensor is: ', input_tensor)
print('The output of tensor.frexp is: ', frexp_output)