input_tensor = torch.randn(1, 3, 1, 1)
tensor2 = torch.randn(1, 3, 1, 1)
output_tensor = torch.Tensor.matmul(input_tensor, tensor2)