input_data = torch.randn(2, 4)
output_data = torch.logsumexp(input_data, dim=1)