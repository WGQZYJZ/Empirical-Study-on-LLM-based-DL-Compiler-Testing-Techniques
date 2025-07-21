'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randint(10, (3, 3))
print('Input tensor: ', input_tensor)
result = input_tensor.diag()
print('Result: ', result)