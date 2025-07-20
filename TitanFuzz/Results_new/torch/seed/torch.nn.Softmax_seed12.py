input_data = torch.randn(2, 3)
output_data = torch.nn.Softmax(dim=0)(input_data)