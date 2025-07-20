input = torch.randn(3, 3)
input = (input @ input.t())
output = torch.cholesky(input)