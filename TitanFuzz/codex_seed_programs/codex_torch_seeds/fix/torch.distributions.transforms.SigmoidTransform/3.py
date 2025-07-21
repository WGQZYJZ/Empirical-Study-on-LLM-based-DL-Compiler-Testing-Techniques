'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SigmoidTransform\ntorch.distributions.transforms.SigmoidTransform(cache_size=0)\n'
import torch
import torch.distributions as dist
input_data = torch.rand(10)
print(input_data)
sigmoid_trans = dist.transforms.SigmoidTransform()
print(sigmoid_trans(input_data))
'\nTask 4: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
exp_trans = dist.transforms.ExpTransform()
print(exp_trans(input_data))
'\nTask 5: Call the API torch.distributions.transforms.AffineTransform\ntorch.distributions.transforms.AffineTransform(loc, scale, cache_size=0)\n'
affine_trans = dist.transforms.AffineTransform(loc=2, scale=2)
print(affine_trans(input_data))