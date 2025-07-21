'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.register_hook\ntorch.Tensor.register_hook(_input_tensor, hook)\n'
import torch
import torch
x = torch.rand(2, 3)
print(x)
x.register_hook(print)
y = x.sum()
print(y)