input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_tensor = torch.tensor(input_data, dtype=torch.float32)
torch.nn.init.constant_(input_tensor, val=10)