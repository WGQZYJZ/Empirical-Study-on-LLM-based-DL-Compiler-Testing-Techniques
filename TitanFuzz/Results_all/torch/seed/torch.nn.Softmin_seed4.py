input_tensor = torch.randn(2, 3)
output_tensor = torch.nn.Softmin(dim=1)(input_tensor)