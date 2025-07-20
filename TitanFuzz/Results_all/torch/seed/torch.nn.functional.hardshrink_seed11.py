input_data = Variable(torch.randn(100, 100))
output_data = torch.nn.functional.hardshrink(input_data, lambd=0.5)