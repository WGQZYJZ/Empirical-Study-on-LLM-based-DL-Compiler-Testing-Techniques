'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=1, high=9, size=(2, 3))
print(input_tensor)
print(torch.Tensor.int_repr(input_tensor))