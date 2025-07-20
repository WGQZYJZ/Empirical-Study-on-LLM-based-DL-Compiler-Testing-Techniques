input_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
input_data = torch.from_numpy(input_data)
output_data = torch.flip(input_data, [0])