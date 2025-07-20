input_tensor = torch.rand(3, 3)
output_tensor = torch.min(input_tensor, dim=0, keepdim=False)