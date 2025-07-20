input_data = Variable(torch.randn(10, 10))
output_data = torch.nn.functional.mish(input_data)