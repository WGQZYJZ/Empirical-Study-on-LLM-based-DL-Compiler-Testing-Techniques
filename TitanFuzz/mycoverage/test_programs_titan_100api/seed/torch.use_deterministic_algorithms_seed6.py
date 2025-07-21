input_data = np.random.rand(100, 100)
input_data = torch.tensor(input_data, dtype=torch.float32)
torch.use_deterministic_algorithms(mode=True)
output = torch.sigmoid(input_data)