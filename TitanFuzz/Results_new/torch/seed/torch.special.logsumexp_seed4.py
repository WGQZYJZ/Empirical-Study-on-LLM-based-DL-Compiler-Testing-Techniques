input_data = torch.randn(1, 2)
output_data = torch.special.logsumexp(input_data, dim=1, keepdim=False)