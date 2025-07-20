input_data = torch.randn(5, 4)
output_data = torch.nn.functional.tanhshrink(input_data)