input_data = np.random.uniform(0, 1, (10, 5))
input_data = torch.from_numpy(input_data)
output_data = torch.nn.functional.tanh(input_data)