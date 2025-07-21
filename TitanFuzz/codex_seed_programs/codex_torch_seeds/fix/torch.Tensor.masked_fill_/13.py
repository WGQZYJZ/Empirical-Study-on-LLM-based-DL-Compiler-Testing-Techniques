'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randint(0, 10, (3, 4))
print('Input tensor: ', input_tensor)
mask = (input_tensor > 5)
print('Mask: ', mask)
output_tensor = input_tensor.masked_fill_(mask, 0)
print('Output tensor: ', output_tensor)