input_data = torch.randn(2, 3)
output_data = torch.nn.Softmin(dim=1)(input_data)