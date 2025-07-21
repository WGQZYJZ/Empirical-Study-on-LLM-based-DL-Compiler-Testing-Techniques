'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print('input_tensor:', input_tensor)
print('torch.Tensor.qscheme(input_tensor):', torch.Tensor.qscheme(input_tensor))