input_data = np.array([1.0, 1.5, 2.0, 2.5])
input_data_tensor = torch.tensor(input_data)
output_data_tensor = torch.acosh(input_data_tensor)