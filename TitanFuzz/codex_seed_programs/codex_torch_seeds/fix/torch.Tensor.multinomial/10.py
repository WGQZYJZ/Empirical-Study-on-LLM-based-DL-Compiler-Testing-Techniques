'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multinomial\ntorch.Tensor.multinomial(_input_tensor, num_samples, replacement=False, *, generator=None)\n'
import torch
input_tensor = torch.rand(4, 4)
print('input_tensor: ', input_tensor)
num_samples = 3
input_tensor.multinomial(num_samples, replacement=True)
print('multinomial: ', input_tensor.multinomial(num_samples, replacement=True))
print('multinomial: ', input_tensor.multinomial(num_samples, replacement=False))
print('multinomial: ', input_tensor.multinomial(num_samples, replacement=True, generator=None))
print('multinomial: ', input_tensor.multinomial(num_samples, replacement=False, generator=None))