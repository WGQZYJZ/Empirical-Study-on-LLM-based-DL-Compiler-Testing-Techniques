input_data = torch.randn(10, 5)
output_data = torch.logsumexp(input_data, dim=1)