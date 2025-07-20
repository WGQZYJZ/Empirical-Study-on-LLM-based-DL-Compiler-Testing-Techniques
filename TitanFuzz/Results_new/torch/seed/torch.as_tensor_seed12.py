a_list = [1, 2, 3]
a_numpy_array = np.array([1, 2, 3])
a_tensor = torch.tensor([1, 2, 3])
tensor_from_list = torch.as_tensor(a_list)
tensor_from_numpy = torch.as_tensor(a_numpy_array)
tensor_from_tensor = torch.as_tensor(a_tensor)