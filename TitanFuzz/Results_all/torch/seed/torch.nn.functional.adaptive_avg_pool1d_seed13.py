input_data = torch.tensor(np.random.random((1, 1, 10)), dtype=torch.float32)
output_data = torch.nn.functional.adaptive_avg_pool1d(input_data, 2)