input_data = Variable(torch.randn(1, 3, 224, 224))
output = torch.nn.functional.hardswish(input_data)