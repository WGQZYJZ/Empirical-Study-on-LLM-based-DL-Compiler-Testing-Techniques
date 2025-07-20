input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=torch.uint8)
source = torch.tensor([[9, 9, 9], [9, 9, 9], [9, 9, 9]])
torch.Tensor.masked_scatter_(input_tensor, mask, source)