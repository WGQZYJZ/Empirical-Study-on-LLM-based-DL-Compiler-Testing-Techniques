_input_tensor = torch.randn(3, 4)
_mask = torch.tensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
_source = torch.tensor([[(- 1), (- 1), (- 1), (- 1)], [(- 1), (- 1), (- 1), (- 1)], [(- 1), (- 1), (- 1), (- 1)]])
torch.Tensor.masked_scatter_(_input_tensor, _mask, _source)