input_data = np.random.randn(5, 2)
input_data = torch.from_numpy(input_data)
input_size = torch.LongStorage(input_data.size())