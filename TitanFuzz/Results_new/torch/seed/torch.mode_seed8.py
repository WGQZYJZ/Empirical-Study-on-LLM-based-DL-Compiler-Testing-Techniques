input = torch.randn(100, 5)
(mode, indices) = torch.mode(input, dim=(- 1), keepdim=False)