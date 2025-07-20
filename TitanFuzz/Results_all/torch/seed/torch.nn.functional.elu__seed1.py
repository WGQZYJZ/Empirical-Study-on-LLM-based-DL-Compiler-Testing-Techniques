input_data = torch.randn(10)
input_data
torch.nn.functional.elu_(input_data)
torch.nn.functional.elu(input_data)
torch.nn.functional.elu(input_data, alpha=0.5)