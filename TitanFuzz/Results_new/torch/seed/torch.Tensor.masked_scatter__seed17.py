_input_tensor = torch.randint(10, (3, 3))
mask = torch.ByteTensor([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
source = torch.randint(10, (3,))
torch.Tensor.masked_scatter_(_input_tensor, mask, source)