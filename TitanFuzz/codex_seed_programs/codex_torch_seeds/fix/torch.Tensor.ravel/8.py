'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
_output_tensor = _input_tensor.ravel()
print(_output_tensor)
'\nExpected output:\ntensor([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])\n'