'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
import torch
data = torch.arange(1, 17).view(4, 4)
print('Input data:')
print(data)
result = torch.Tensor.tril_(data, diagonal=0)
print('Result:')
print(result)