input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
output = torch.nn.functional.cross_entropy(input, target)