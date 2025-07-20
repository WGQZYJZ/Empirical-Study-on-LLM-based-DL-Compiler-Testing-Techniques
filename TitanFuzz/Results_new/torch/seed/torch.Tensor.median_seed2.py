input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
input_tensor_median = torch.Tensor.median(input_tensor)
input_tensor_median_dim = torch.Tensor.median(input_tensor, dim=0)
input_tensor_median_dim_keepdim = torch.Tensor.median(input_tensor, dim=0, keepdim=True)