input_data = torch.randn(2, 3, 4)
output_data = torch.nn.functional.logsigmoid(input_data)