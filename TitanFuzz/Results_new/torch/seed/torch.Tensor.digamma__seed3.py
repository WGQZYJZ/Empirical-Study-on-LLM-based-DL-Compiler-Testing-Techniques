input_tensor = torch.randn(8, 8)
output_tensor = torch.Tensor.digamma_(input_tensor)
input_tensor_1 = torch.randn(8, 8)
input_tensor_2 = torch.randn(8, 8)
output_tensor = torch.Tensor.dist(input_tensor_1, input_tensor_2, 2.0)