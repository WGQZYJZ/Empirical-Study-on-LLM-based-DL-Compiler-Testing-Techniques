input = torch.randn(1, 1, 4, 4)
output = torch.nn.PixelUnshuffle(2)(input)