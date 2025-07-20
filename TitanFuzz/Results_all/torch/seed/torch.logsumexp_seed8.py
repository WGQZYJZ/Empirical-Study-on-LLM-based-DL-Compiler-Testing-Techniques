input = torch.randn(2, 3)
output = torch.logsumexp(input, dim=0, keepdim=False)
output = torch.logsumexp(input, dim=1, keepdim=False)