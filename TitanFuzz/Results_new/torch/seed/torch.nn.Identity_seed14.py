input_data = np.random.rand(10, 3)
input_data = torch.tensor(input_data, dtype=torch.float32)
identity = torch.nn.Identity()
output = identity(input_data)