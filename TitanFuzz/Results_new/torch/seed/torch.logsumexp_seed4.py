input_data = torch.randn(2, 3)
output_data = torch.logsumexp(input_data, dim=1)