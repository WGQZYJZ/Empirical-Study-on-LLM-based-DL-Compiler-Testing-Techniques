input_data = Variable(torch.randn(10, 10))
output = torch.nn.functional.tanhshrink(input_data)