input_data = torch.randn(3, 4)
logsumexp_output = torch.logsumexp(input_data, dim=1)