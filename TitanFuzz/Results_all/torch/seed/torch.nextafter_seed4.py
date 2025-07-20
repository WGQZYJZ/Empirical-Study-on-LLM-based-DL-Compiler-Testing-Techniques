input = torch.tensor([0.5, 0.5, 0.5, 0.5])
other = torch.tensor([1.0, 1.0, 1.0, 1.0])
result = torch.nextafter(input, other)