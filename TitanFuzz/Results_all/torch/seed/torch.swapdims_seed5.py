input_data = torch.randn(1, 2, 3, 4)
output_data = torch.swapdims(input_data, dim0=2, dim1=3)