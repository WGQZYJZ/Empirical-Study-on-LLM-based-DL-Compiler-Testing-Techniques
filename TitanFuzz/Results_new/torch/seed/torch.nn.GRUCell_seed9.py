input_data = np.random.randn(2, 3)
gru = torch.nn.GRUCell(3, 2)
output = gru(torch.tensor(input_data, dtype=torch.float32))
input_data = np.random.randn(2, 3)