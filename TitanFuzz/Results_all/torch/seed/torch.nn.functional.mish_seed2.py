input_data = Variable(torch.randn(100, 100))
output = torch.nn.functional.mish(input_data)