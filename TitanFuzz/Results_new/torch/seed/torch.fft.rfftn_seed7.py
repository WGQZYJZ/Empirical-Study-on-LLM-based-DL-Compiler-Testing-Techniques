input_data = np.random.randn(3, 4, 5)
input_data = torch.from_numpy(input_data)
output_data = torch.fft.rfftn(input_data, 3, 0)