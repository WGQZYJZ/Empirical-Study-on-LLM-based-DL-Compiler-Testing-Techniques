input_tensor = torch.rand(2, 3)
tensor1 = torch.rand(2, 3)
tensor2 = torch.rand(2, 3)
result = torch.Tensor.addcmul_(input_tensor, tensor1, tensor2)