input_tensor = torch.randn(2, 3, 4)
tensor1 = torch.randn(2, 3, 4)
tensor2 = torch.randn(2, 3, 4)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2, value=2)