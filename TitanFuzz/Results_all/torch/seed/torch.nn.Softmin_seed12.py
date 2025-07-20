input_data = torch.randn(2, 3)
softmin_output = torch.nn.Softmin(dim=0)(input_data)