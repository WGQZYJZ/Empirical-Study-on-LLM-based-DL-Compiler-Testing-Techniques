data = [[1, 2], [3, 4]]
tensor_data = torch.as_tensor(data, dtype=torch.float32)
data = np.array([[1, 2], [3, 4]])
tensor_data = torch.from_numpy(data)