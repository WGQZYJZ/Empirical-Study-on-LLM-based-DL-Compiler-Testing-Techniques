input = torch.randn(2, 3)
result = torch.logsumexp(input, dim=1, keepdim=True)