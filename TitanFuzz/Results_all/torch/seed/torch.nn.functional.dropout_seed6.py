input_data = torch.tensor(np.random.rand(3, 3), dtype=torch.float32)
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True)