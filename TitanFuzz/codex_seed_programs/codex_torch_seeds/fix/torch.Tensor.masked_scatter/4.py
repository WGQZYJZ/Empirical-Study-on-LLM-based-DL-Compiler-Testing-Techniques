'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 4))
mask = torch.tensor([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 1]], dtype=torch.bool)
tensor = torch.randint(0, 10, (3, 4))
print('Input Tensor:')
print(input_tensor)
print('Mask:')
print(mask)
print('Tensor:')
print(tensor)
print('Result:')
print(torch.Tensor.masked_scatter(input_tensor, mask, tensor))