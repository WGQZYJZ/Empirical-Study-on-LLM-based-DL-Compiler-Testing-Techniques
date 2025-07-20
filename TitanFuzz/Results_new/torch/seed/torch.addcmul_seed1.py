tensor1 = torch.rand(3, 3)
tensor2 = torch.rand(3, 3)
output = torch.addcmul(tensor1, tensor2, tensor1)