input_size = (1, 1, 4)
input_data = torch.tensor(np.arange(1, 5, dtype=np.float32).reshape(input_size))
avg_pool_1d = torch.nn.AdaptiveAvgPool1d(output_size=2)
output = avg_pool_1d(input_data)