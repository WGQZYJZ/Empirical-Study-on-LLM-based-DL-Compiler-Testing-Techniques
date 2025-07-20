input_data = torch.rand(1, dtype=torch.float64)
result = torch.acos(input_data)
input_data_numpy = input_data.numpy()
result_numpy = np.arccos(input_data_numpy)