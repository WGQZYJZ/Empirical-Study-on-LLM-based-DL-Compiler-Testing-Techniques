input_tensor = torch.randn(2, 3, 4)
input_tensor[(0, 0, 0)] = float('inf')
input_tensor[(1, 2, 3)] = float('-inf')
output_tensor = torch.Tensor.isinf(input_tensor)