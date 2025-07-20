input_data = np.array([[[1, 2, 3, 4, 5]]])
input_data = torch.from_numpy(input_data)
input_data = input_data.float()
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=3, stride=1, padding=0)