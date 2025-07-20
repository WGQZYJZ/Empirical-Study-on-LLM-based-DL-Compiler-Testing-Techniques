input_tensor = torch.rand(3, 3)
output_tensor = torch.cumsum(input_tensor, dim=0)
output_tensor = torch.cumsum(input_tensor, dim=1)