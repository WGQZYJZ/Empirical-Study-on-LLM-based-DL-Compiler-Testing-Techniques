_input_tensor = torch.randn(3, 3, 3, 3)
mask = torch.tensor([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
output_tensor = torch.Tensor.sparse_mask(_input_tensor, mask)