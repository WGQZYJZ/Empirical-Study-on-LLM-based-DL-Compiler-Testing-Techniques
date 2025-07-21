'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage\ntorch.Tensor.storage(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(_input_tensor.storage())