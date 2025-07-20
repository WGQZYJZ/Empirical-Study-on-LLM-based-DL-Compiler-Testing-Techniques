input_data = np.random.randn(4, 4)
input_data = torch.tensor(input_data, dtype=torch.float32)
output = torch.erf(input_data)