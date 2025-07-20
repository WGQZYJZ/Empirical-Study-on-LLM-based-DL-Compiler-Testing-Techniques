input_data = Variable(torch.randn(1, 1, 3, 3))
output_data = torch.nn.functional.gelu(input_data)