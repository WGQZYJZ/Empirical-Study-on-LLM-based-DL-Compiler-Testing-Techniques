input_data = torch.randn(3, 4)
log_cumsum_exp_data = torch.logcumsumexp(input_data, dim=0)
log_cumsum_exp_data = torch.logcumsumexp(input_data, dim=1)