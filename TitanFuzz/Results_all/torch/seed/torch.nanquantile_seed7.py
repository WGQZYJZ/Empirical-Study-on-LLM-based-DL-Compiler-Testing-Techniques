input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
result = torch.nanquantile(input, 0.5, dim=0, keepdim=False)