input = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
torch.addcmul(input, tensor1, tensor2)
input = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
torch.addcdiv(input, tensor1, tensor2)