input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.to_sparse(input_tensor, sparse_dims=1)