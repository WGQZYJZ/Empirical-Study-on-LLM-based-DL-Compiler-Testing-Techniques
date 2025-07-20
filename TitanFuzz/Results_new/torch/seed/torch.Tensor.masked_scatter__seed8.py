input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
source = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_tensor = torch.Tensor.masked_scatter_(input_tensor, mask, source)