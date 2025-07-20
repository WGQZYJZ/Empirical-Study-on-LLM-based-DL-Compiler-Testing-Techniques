input_data = torch.tensor(np.random.randn(1, 1, 2, 3, 3), dtype=torch.float32)
pad_size = (1, 1, 1, 1, 1, 1)
output_data = torch.nn.ReplicationPad3d(pad_size)(input_data)