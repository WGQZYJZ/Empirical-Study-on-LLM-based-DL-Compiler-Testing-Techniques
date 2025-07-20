input_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
input_data = torch.tensor(input_data, dtype=torch.float32)
output_data = torch.subtract(input_data, input_data)