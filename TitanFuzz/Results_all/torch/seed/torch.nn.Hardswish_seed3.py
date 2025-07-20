input_data = torch.randn(1, 3, 224, 224)
hardswish = torch.nn.Hardswish(inplace=False)
output = hardswish(input_data)