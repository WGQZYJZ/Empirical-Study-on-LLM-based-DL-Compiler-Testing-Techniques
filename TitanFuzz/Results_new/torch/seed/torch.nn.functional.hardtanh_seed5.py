input_data = np.random.randn(1, 3, 3, 3)
input_data = torch.tensor(input_data, dtype=torch.float32)
output = torch.nn.functional.hardtanh(input_data)