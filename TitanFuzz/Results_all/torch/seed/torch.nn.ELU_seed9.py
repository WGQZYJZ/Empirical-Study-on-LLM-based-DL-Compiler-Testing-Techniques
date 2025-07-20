input_data = Variable(torch.randn(5, 3))
elu = torch.nn.ELU(alpha=1.0, inplace=False)
output_data = elu(input_data)