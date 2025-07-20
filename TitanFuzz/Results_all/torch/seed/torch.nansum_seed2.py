input = torch.tensor([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]], dtype=torch.float32)
output = torch.nansum(input, dim=1)