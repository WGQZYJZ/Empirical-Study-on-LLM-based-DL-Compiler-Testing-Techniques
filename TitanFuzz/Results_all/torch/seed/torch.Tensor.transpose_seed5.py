input_tensor = torch.randn(3, 4, 5)
output_tensor = torch.Tensor.transpose(input_tensor, 0, 1)
input_tensor = torch.randn(3, 4, 5)
output_tensor = torch.Tensor.flip(input_tensor, [1])