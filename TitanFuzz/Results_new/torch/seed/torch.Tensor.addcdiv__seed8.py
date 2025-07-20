tensor1 = torch.rand(2, 3, dtype=torch.float32)
tensor2 = torch.rand(2, 3, dtype=torch.float32)
tensor3 = torch.rand(2, 3, dtype=torch.float32)
torch.Tensor.addcdiv_(tensor1, tensor2, tensor3, value=1)