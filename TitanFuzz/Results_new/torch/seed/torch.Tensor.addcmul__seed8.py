input_tensor = torch.randn(3, 3, requires_grad=True)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2, value=1)