tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
tensor3 = torch.randn(3, 3)
torch.Tensor.addcdiv_(tensor1, tensor2, tensor3, value=1)