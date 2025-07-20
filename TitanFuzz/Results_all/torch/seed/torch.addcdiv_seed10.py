tensor1 = torch.randn(2, 2)
tensor2 = torch.randn(2, 2)
tensor3 = torch.randn(2, 2)
tensor4 = torch.addcdiv(tensor1, tensor2, tensor3, value=1)