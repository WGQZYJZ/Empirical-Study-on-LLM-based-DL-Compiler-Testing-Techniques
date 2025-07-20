input = torch.randn(2, 3)
index = torch.argmax(input, dim=1)
index = torch.argmax(input, dim=1, keepdim=True)