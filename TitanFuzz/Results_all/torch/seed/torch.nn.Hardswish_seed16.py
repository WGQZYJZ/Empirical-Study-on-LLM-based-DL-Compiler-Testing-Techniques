input_data = torch.randn(10, 20, 30, 40)
hardswish = torch.nn.Hardswish()
output = hardswish(input_data)