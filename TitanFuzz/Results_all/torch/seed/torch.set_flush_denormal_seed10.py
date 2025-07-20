input_data = np.random.randn(3, 3).astype(np.float32)
torch.set_flush_denormal(True)
input_data = torch.from_numpy(input_data)
output_data = input_data.numpy()