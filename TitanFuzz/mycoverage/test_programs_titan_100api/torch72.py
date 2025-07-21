import torch
input = torch.randn(5, 10)
target = torch.randn(5, 10)
torch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')
input = torch.randn(5, 10)
torch.nn.functional.pdist(input, p=2)