input_data = torch.rand(1, 32, 32, 32)
torch.nn.functional.pixel_unshuffle(input_data, 2)