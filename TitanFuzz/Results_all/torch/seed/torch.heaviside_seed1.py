input = torch.randn(3, 3)
values = torch.tensor([0.5, 1.0, 2.0])
output = torch.heaviside(input, values)