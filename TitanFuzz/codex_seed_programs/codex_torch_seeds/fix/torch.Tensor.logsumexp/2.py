'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logsumexp\ntorch.Tensor.logsumexp(_input_tensor, dim, keepdim=False)\n'
import torch
x = torch.randn(3, 4)
print('x: ', x)
print('torch.Tensor.logsumexp(x): ', torch.Tensor.logsumexp(x))
print('torch.Tensor.logsumexp(x, dim=0): ', torch.Tensor.logsumexp(x, dim=0))
print('torch.Tensor.logsumexp(x, dim=1): ', torch.Tensor.logsumexp(x, dim=1))
print('torch.Tensor.logsumexp(x, dim=1, keepdim=True): ', torch.Tensor.logsumexp(x, dim=1, keepdim=True))