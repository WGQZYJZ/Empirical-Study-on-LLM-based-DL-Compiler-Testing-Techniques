'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
import torch
a = torch.randn(4, 4)
print(a)
print(a.tril_())
print(a.tril_((- 1)))
print(a.tril_(1))