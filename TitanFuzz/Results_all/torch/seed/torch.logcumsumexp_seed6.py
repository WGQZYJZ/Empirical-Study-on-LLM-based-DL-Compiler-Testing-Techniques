input_data = torch.rand(100)
result = torch.logcumsumexp(input_data, dim=0)