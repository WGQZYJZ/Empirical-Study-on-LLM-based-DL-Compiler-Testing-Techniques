input = torch.randn(3, 5, requires_grad=True)
output = torch.nn.functional.normalize(input, p=2, dim=1)