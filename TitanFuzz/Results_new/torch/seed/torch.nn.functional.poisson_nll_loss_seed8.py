input = Variable(torch.randn(1, 3))
target = Variable(torch.randn(1, 3))
output = torch.nn.functional.poisson_nll_loss(input, target)