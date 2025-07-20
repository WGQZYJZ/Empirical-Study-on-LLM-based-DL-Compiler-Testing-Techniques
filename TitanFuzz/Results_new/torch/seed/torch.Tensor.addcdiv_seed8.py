input_tensor = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
output_tensor = torch.Tensor.addcdiv(input_tensor, tensor1, tensor2)