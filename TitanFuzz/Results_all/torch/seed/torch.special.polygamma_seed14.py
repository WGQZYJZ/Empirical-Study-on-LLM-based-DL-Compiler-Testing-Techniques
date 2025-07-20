input = torch.rand(3, 4, 5, dtype=torch.float64)
output = torch.special.polygamma(3, input)
output = torch.special.polygamma(3, input, out=torch.empty(3, 4, 5, dtype=torch.float64))