'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch
x = torch.tensor(data=[(- 1.0), 1.0, (- 1.0), 1.0], requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)
print(x.grad)