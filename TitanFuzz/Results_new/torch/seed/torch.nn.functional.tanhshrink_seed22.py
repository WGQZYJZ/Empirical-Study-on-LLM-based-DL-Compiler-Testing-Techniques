input_data = torch.randn(3, 3)
output = torch.nn.functional.tanhshrink(input_data)