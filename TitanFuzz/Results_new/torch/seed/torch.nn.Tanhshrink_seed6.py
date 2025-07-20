input_data = torch.randn(1, 3, 3, 3)
output_data = torch.nn.Tanhshrink()(input_data)