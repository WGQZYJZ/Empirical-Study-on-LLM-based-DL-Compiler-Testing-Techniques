input_data = torch.randn(3, 3)
output_data = torch.nn.functional.logsigmoid(input_data)
input_data = torch.randn(3, 3)
output_data = torch.nn.functional.logsigmoid(input_data, out=None)