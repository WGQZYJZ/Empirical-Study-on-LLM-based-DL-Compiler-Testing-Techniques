input = torch.randn(5, 3, 4)
mean = torch.mean(input, dim=1)
mean = torch.mean(input, dim=1, keepdim=True)
mean = torch.mean(input, dim=1, keepdim=True, dtype=torch.float32)