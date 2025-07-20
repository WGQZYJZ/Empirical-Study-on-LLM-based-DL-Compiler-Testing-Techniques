input_data = torch.Tensor(np.arange(16, dtype=np.float32).reshape(1, 4, 4))
torch.nn.functional.pixel_unshuffle(input_data, 2)