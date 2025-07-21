'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(_input_tensor.bool())