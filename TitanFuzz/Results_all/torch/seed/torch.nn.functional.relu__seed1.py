input_data = Variable(torch.randn(5, 3))
output = torch.nn.functional.relu_(input_data)