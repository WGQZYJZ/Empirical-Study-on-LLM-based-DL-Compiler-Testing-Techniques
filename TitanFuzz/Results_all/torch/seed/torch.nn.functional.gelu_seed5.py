input_data = np.random.randn(2, 3)
input_data = Variable(torch.from_numpy(input_data).float())
output_data = torch.nn.functional.gelu(input_data)