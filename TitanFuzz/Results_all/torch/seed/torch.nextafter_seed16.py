input = torch.tensor([1.0, 1.0, 1.0, 1.0, 1.0], dtype=torch.float32)
other = torch.tensor([2.0, 2.0, 2.0, 2.0, 2.0], dtype=torch.float32)
torch.nextafter(input, other)