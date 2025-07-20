input_data = torch.randn(1, 3, 3, 3)
output = torch.nn.functional.tanhshrink(input_data)