input_data = torch.rand(10, 3)
torch.quantile(input_data, 0.5, dim=1, keepdim=True)