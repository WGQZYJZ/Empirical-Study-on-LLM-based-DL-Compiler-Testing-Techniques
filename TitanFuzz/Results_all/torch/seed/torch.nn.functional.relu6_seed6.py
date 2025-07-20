input_data = np.random.randn(2, 3)
input_data = torch.tensor(input_data)
output = torch.nn.functional.relu6(input_data)