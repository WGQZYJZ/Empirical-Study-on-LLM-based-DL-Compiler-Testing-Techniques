input_data = Variable(torch.randn(10, 10))
output = torch.frexp(input_data)
input_data = np.random.randint(1, 10, (5, 5))
output = torch.from_numpy(input_data)