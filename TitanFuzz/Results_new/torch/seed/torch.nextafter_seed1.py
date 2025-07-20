input = torch.randn(1, 10)
other = torch.randn(1, 10)
output = torch.nextafter(input, other)