'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq\ntorch.Tensor.eq(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 4))
other = torch.randint(0, 10, (3, 4))
print('input_tensor:', input_tensor)
print('other:', other)
result = input_tensor.eq(other)
print('result:', result)