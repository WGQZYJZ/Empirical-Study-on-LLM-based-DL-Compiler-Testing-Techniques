'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 2.0)
print(x.grad)