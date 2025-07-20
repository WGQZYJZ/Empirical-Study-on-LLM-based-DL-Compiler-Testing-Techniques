input = torch.rand(1, 3, 4, 4)
output = torch.nn.functional.pixel_unshuffle(input, 2)