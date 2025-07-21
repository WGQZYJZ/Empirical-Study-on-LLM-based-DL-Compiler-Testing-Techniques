'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(_input_tensor)
print(_input_tensor.int_repr())