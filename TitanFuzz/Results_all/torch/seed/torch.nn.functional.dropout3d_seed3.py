input_data = np.random.randn(2, 3, 4, 5, 6)
input_data = torch.tensor(input_data, dtype=torch.float32)
output = torch.nn.functional.dropout3d(input_data, p=0.5, training=True)