input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.from_numpy(input_data)
output = torch.Tensor.new_full(input_data, size=(2, 3), fill_value=1)