input_data = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
torch.addcdiv(input_data, tensor1, tensor2)