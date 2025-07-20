input = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
output = torch.special.polygamma(1, input)
output = torch.special.polygamma(3, input)