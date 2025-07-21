'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq\ntorch.Tensor.eq(_input_tensor, other)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 2, 3, 4, 5])
equal_tensor = x.eq(y)
print('The result of tensor x.eq(y) is: ', equal_tensor)