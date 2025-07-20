input_data = torch.randn(2, 3, 4)
shrinked_output = torch.nn.functional.tanhshrink(input_data)