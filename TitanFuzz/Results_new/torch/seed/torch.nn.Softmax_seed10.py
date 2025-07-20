input_data = torch.randn(2, 3)
output = torch.nn.Softmax(dim=1)(input_data)