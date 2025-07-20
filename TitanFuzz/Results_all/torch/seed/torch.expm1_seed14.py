input_data = np.random.rand(3, 4)
input_data = torch.tensor(input_data)
output = torch.expm1(input_data)