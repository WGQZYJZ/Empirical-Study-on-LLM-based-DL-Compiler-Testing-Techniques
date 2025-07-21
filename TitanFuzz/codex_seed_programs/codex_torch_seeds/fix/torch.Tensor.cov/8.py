'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cov\ntorch.Tensor.cov(_input_tensor, *, correction=1, fweights=None, aweights=None)\n'
import torch
_input_tensor = torch.randint(10, (3, 3))
print(_input_tensor)
torch.Tensor.cov(_input_tensor, correction=1)