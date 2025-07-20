np_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
tensor = torch.from_numpy(np_array)
tensor_strided = torch.empty_strided(tensor.size(), tensor.stride())