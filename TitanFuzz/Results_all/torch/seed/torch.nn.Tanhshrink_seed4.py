input_data = torch.randn(1, 2, 3)
tanhshrink = torch.nn.Tanhshrink()
output = tanhshrink(input_data)