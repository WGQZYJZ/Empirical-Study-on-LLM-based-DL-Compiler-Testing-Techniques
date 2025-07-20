input = torch.tensor([1.0, 2.0, 3.0, 4.0])
other = torch.tensor([1.0, 2.0, 3.0, 4.0])
result = torch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)