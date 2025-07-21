'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.rand(3, 3)
mask = torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
value = (- 1)
output_tensor = input_tensor.masked_fill(mask, value)
print(output_tensor)