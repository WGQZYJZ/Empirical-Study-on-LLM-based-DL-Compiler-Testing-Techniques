input_data = torch.randn(10, 10)
tanhshrink = torch.nn.Tanhshrink()
output_data = tanhshrink(input_data)