input_data = torch.rand(3, 3)
output = torch.unbind(input_data, dim=0)