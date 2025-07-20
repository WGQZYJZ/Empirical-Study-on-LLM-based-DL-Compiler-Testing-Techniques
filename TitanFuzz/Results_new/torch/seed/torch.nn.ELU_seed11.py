input_data = torch.randn(1, 3)
elu = torch.nn.ELU(alpha=1.0, inplace=False)
output_data = elu(input_data)