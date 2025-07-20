input_data = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=np.float32)
input_tensor = torch.from_numpy(input_data)
output_tensor = torch.fft.fftfreq(8, d=1.0)