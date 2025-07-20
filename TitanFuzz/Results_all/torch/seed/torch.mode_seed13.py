input = torch.randn(1, 3, 4, 5)
mode = torch.mode(input, dim=(- 1), keepdim=False, out=None)