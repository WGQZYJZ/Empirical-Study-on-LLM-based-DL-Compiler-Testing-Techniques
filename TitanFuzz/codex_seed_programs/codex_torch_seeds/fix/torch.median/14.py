'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
output = torch.median(input, dim=(- 1), keepdim=False, out=None)
print('input: \n', input)
print('output: \n', output)
'\ninput: \n tensor([[-1.0731,  0.1704, -0.8479,  0.7692],\n        [ 0.7707, -0.9082, -0.0292,  0.8367],\n        [-0.4289, -0.0372,  0.5493, -0.5333]])\noutput: \n tensor([-0.8479, -0.0292, -0.0372])\n'