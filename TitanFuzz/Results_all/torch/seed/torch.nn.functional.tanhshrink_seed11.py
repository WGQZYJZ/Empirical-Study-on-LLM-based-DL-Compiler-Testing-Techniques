input = torch.randn(1, 3, 4, 4)
output = torch.nn.functional.tanhshrink(input)