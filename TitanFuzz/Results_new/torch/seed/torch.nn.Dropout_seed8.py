input_data = torch.randn(20, 16)
output_data = torch.nn.Dropout(p=0.5)(input_data)