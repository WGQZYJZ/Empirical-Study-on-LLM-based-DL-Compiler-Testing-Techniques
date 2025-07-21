import torch
input = torch.rand(10)
target = torch.rand(10)
loss = torch.nn.functional.poisson_nll_loss(input, target)