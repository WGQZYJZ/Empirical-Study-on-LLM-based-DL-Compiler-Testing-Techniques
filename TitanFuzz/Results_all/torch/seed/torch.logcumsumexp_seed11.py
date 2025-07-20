input_data = torch.randn(1, 2, 3)
torch.logcumsumexp(input_data, dim=1)
torch.logcumsumexp(input_data, dim=1, out=None)