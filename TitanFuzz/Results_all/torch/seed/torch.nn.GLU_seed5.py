input_data = torch.randn(2, 3, 4)
glu_module = torch.nn.GLU(dim=(- 1))
output_data = glu_module(input_data)