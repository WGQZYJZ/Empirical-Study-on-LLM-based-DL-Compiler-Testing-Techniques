input_data = torch.randn(1, 2, 3)
output = torch.logcumsumexp(input_data, dim=1)