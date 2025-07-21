input_tensor = torch.rand(3, 3)
result = torch.amin(input_tensor, 1, keepdim=True)
result = torch.amin(input_tensor, 1, keepdim=False)