tensor1 = torch.rand(4, 3)
tensor2 = torch.rand(4, 3)
tensor3 = torch.rand(4, 3)
torch.addcdiv(tensor1, tensor2, tensor3, value=1)