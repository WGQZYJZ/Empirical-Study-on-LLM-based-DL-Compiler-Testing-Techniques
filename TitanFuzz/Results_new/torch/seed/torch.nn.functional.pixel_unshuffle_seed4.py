input_data = torch.randn(2, 3, 4, 4)
output = torch.nn.functional.pixel_unshuffle(input_data, 2)