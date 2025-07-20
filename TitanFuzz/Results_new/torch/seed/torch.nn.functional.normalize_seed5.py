x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
y = torch.nn.functional.normalize(x, p=2, dim=1)