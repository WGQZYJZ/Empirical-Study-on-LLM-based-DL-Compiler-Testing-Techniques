input_data = np.random.rand(2, 3)
input_data = torch.tensor(input_data, dtype=torch.float32)
torch.nn.init.xavier_uniform_(input_data)