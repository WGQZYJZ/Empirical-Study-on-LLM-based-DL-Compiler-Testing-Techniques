input_data = torch.randn(3, 4)
result = torch.amin(input_data, dim=0, keepdim=False)
result = torch.amin(input_data, dim=1, keepdim=False)
result = torch.amin(input_data, dim=1, keepdim=True)