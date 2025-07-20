input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.from_numpy(input_data).float()
torch.nn.init.xavier_normal_(input_data)