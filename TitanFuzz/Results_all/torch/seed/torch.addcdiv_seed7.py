input = torch.randn(4, 4)
tensor1 = torch.randn(4, 4)
tensor2 = torch.randn(4, 4)
output = torch.addcdiv(input, tensor1, tensor2, value=1)