input = torch.tensor([1.0, 2.0, 3.0, 4.0])
other = torch.tensor([2.0, 3.0, 4.0, 5.0])
torch.nextafter(input, other)