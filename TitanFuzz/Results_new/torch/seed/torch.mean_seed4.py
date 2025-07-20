input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.mean(input, dim=1)
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.mean(input, dim=1, keepdim=True)