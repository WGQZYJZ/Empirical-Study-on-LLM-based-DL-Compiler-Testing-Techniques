'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 4)
_input_tensor_int = torch.randint(0, 10, (3, 4))
print(torch.Tensor.int_repr(_input_tensor))
print(torch.Tensor.int_repr(_input_tensor_int))