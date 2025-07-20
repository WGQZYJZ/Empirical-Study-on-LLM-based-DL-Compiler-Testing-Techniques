input_data = np.random.randn(10, 5)
input_data = torch.tensor(input_data, dtype=torch.float32)
output_data = torch.nn.functional.gelu(input_data)