'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch
x = torch.ones(2, 2, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)
print(x.grad)