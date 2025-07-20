input_data = np.array([[1, 2], [3, 4]])
input_data = torch.from_numpy(input_data)
angle = torch.angle(input_data)