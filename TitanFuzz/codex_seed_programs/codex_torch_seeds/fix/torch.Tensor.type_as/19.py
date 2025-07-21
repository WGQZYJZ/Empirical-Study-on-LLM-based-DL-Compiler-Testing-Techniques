'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
torch.Tensor.type_as(_input_tensor, torch.FloatTensor)
print(_input_tensor.type())
print(_input_tensor)
torch.Tensor.type_as(_input_tensor, torch.DoubleTensor)
print(_input_tensor.type())
print(_input_tensor)
torch.Tensor.type_as(_input_tensor, torch.IntTensor)
print(_input_tensor.type())
print(_input_tensor)