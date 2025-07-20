input_data = Variable(torch.Tensor(np.random.randn(5, 3)))
selu = torch.nn.SELU(inplace=False)
output_data = selu(input_data)