_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[0, 0, 0], [4, 5, 6]])
torch.Tensor.gt_(_input_tensor, other)