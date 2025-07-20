input_tensor = torch.randn(2, 3)
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2)