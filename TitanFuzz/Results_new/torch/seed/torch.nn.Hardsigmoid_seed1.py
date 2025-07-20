input_data = Variable(torch.randn(1, 3), requires_grad=True)
input_data = Variable(torch.randn(1, 3), requires_grad=True)
hardsigmoid = torch.nn.Hardsigmoid(inplace=False)
output = hardsigmoid(input_data)