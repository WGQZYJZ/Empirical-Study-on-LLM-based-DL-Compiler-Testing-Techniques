input_data = Variable(torch.randn(1, 3, 224, 224))
output = torch.nn.functional.hardshrink(input_data, lambd=0.5)