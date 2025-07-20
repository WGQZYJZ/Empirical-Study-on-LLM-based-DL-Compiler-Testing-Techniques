input = torch.randn(1, 3, 5, 5)
output = torch.flatten(input, start_dim=1)