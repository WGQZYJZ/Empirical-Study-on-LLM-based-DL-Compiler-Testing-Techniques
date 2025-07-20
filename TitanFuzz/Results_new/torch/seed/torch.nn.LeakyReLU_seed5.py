input_data = Variable(torch.randn(5, 3))
leaky_relu = torch.nn.LeakyReLU(0.2)
output_data = leaky_relu(input_data)