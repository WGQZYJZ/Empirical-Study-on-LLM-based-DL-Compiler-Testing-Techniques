input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.prod(input, dim=0, keepdim=True)