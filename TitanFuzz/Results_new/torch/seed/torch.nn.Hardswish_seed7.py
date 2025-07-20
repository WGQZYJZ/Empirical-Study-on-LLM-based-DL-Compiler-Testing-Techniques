input_data = np.random.randn(1, 3, 3, 3)
input_data = Variable(torch.Tensor(input_data))
hardswish = torch.nn.Hardswish()
output = hardswish(input_data)