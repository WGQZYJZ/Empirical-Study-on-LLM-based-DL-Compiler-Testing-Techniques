input_data = np.array([(- 1), (- 0.5), 0, 0.5, 1])
input_data = torch.tensor(input_data, dtype=torch.float32)
output_data = torch.nn.functional.softsign(input_data)