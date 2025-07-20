input = torch.randn(3, 4)
output = torch.logsumexp(input, dim=1)
output = torch.logsumexp(input, dim=1, keepdim=True)
output = torch.logsumexp(input, dim=1, keepdim=True, out=torch.FloatTensor())