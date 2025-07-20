_input_tensor = torch.rand(3, 3, 3)
mask = torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=torch.uint8)
torch.Tensor.sparse_mask(_input_tensor, mask)