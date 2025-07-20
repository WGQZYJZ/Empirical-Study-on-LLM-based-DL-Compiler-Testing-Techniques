input = torch.randn(1, 3)
(value, indices) = torch.mode(input, dim=1)