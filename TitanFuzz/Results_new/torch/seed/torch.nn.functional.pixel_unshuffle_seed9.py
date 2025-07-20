input = torch.randn(1, 1, 4, 4)
output = torch.nn.functional.pixel_unshuffle(input, 2)