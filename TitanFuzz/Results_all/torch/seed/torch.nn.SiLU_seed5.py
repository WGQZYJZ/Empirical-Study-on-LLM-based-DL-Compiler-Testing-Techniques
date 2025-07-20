input_data = torch.randn(1, 3, 224, 224)
output_data = torch.nn.SiLU(inplace=False)(input_data)