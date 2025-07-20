input_data = torch.randn(2, 3)
result = torch.logsumexp(input_data, dim=1, keepdim=True)