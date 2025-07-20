input_data = torch.randn(1, 1, 5, 5)
output_data = torch.nn.Tanhshrink()(input_data)
input_data = torch.randn(1, 1, 5, 5)
output_data = torch.nn.Softshrink()(input_data)