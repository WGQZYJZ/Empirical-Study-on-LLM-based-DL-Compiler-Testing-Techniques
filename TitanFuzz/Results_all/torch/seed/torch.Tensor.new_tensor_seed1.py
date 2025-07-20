_input_tensor = torch.randn(2, 3)
data = [[1, 2, 3], [4, 5, 6]]
torch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)