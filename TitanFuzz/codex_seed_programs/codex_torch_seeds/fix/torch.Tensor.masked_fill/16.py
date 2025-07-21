'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 5))
print('Input tensor:', input_tensor)
mask = torch.tensor([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0], [0, 1, 0, 1, 1], [1, 1, 1, 0, 0]])
print('Mask:', mask)
output_tensor = input_tensor.masked_fill(mask, (- 1))
print('Output tensor:', output_tensor)