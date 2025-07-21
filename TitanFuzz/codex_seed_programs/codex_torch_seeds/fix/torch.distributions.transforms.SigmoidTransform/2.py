'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SigmoidTransform\ntorch.distributions.transforms.SigmoidTransform(cache_size=0)\n'
import torch
import torch.distributions as dist
import torch.distributions.transforms as trans
x = torch.randn(1)
print(x)
sigmoid_transform = trans.SigmoidTransform(cache_size=0)
print(sigmoid_transform)
y = sigmoid_transform(x)
print(y)
print(sigmoid_transform.inv(y))
'\nTask 4: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
x = torch.randn(1)
print(x)
exp_transform = trans.ExpTransform(cache_size=0)
print(exp_transform)
y = exp_transform(x)
print(y)
print(exp_transform.inv(y))