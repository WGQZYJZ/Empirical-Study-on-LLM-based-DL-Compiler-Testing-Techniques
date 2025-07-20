_input_tensor = torch.randint(0, 10, (3, 3))
mask = torch.tensor([[0, 1, 0], [0, 1, 0], [1, 1, 1]], dtype=torch.bool)
source = torch.tensor([[0, 0, 0], [0, 0, 0], [1, 1, 1]], dtype=torch.int)
torch.Tensor.masked_scatter_(_input_tensor, mask, source)