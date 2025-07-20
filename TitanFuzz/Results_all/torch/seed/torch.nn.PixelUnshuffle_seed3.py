input = np.random.rand(1, 1, 4, 4)
input = Variable(torch.from_numpy(input))
pixel_unshuffle = torch.nn.PixelUnshuffle(2)
output = pixel_unshuffle(input)