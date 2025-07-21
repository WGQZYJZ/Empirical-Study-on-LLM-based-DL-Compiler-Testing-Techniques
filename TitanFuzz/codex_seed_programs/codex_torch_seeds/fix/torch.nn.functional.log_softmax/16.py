'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.log_softmax\ntorch.nn.functional.log_softmax(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=torch.float32)
y = torch.nn.functional.log_softmax(x, dim=1)
print('x = ', x)
print('y = ', y)
x_sum = torch.sum(torch.exp(x), dim=1)
y_sum = torch.sum(torch.exp(y), dim=1)
print('x_sum = ', x_sum)
print('y_sum = ', y_sum)