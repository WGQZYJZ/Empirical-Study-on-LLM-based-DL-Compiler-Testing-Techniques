input_data = np.array([[1, 2, 3], [4, 5, 6]])
tensor = torch.tensor(input_data)
torch.nn.init.zeros_(tensor)