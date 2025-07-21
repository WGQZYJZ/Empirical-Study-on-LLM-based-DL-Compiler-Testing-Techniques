input = torch.randn(2, 2)
target = torch.randn(2, 2)
loss = torch.nn.functional.poisson_nll_loss(input, target)