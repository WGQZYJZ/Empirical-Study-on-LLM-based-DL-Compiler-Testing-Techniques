input = torch.rand(1, 1, 3, 3)
output = torch.nn.functional.threshold(input, 0.5, 0.5)