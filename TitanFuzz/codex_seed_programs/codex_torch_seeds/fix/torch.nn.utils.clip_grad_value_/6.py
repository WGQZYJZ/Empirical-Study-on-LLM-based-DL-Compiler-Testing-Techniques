'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
y = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
torch.nn.utils.clip_grad_value_(x, 5)
print(x)
torch.nn.utils.clip_grad_value_(y, 1)
print(y)