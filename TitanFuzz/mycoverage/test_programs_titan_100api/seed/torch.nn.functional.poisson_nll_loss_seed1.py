input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
output = torch.nn.functional.poisson_nll_loss(input, target)