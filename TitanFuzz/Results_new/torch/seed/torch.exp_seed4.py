input_data = torch.randn(2, 4)
exp_output = torch.exp(input_data)
exp_output = torch.empty(2, 4)
torch.exp(input_data, out=exp_output)