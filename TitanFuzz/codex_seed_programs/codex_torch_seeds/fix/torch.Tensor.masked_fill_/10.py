'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print('Input tensor: \n', input_tensor)
mask = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.uint8)
print('Mask: \n', mask)
value = torch.tensor(1)
print('Value: \n', value)
torch.Tensor.masked_fill_(input_tensor, mask, value)
print('Output tensor: \n', input_tensor)