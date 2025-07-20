x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.nextafter(x, torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0]))