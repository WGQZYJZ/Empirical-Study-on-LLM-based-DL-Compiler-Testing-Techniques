'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril\ntorch.Tensor.tril(_input_tensor, diagonal=0)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input tensor:\n', _input_tensor)
_result_tensor = torch.Tensor.tril(_input_tensor, diagonal=0)
print('Result tensor:\n', _result_tensor)
_result_tensor = torch.tril(_input_tensor, diagonal=0)
print('Result tensor:\n', _result_tensor)