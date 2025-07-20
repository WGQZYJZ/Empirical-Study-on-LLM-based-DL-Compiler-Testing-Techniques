input_data = Variable(torch.randn(1, 3, 4, 4))
unshuffle = torch.nn.PixelUnshuffle(2)
output = unshuffle(input_data)