'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(3, 3)
mask = torch.tensor([[False, False, True], [True, False, False], [False, True, False]])
value = torch.tensor([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
out_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)
print('Input tensor: \n', input_tensor)
print('Output tensor: \n', out_tensor)