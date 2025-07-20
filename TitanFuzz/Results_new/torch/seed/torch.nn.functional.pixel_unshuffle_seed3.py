input = torch.randn(1, 2, 4, 4)
output = torch.nn.functional.pixel_unshuffle(input, 2)