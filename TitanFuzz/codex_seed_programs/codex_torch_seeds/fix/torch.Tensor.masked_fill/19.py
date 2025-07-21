'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(3, 3)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
value = 3.1415926
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)
print(output_tensor)