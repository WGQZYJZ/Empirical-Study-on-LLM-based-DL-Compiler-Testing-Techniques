input_data = torch.randn(10, 10)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
output = prelu(input_data)