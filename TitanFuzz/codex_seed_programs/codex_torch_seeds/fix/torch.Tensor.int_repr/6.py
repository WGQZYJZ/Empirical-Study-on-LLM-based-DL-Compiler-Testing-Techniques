'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(1, 2, 3, 4))
torch.Tensor.int_repr(input_tensor)