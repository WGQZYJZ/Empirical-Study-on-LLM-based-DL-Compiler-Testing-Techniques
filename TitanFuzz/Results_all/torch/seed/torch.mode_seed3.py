input = torch.randn(3, 5)
(mode, indices) = torch.mode(input, dim=1)