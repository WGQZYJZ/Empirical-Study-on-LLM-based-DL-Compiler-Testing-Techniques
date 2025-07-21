'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq\ntorch.Tensor.eq(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(high=10, size=(2, 3))
other = torch.randint(high=10, size=(2, 3))
result = input_tensor.eq(other)
print(input_tensor)
print(other)
print(result)