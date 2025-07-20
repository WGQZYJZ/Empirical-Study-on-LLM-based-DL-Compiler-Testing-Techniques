input_tensor = torch.randn(2, 3, 4)
sum_to_size_result = torch.Tensor.sum_to_size(input_tensor, 3, 4)
input_tensor = torch.randn(2, 3, 4)
sum_to_size_result = torch.Tensor.sum_to_size(input_tensor, 3, 4, out=None)