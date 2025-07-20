input_data = np.random.randn(1, 3, 4, 4)
input_data = torch.tensor(input_data, dtype=torch.float32)
out = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(input_data)