_input_tensor = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=torch.float32)
_index = torch.tensor([0, 2], dtype=torch.long)
_tensor = torch.tensor([[9, 9], [9, 9]], dtype=torch.float32)
torch.Tensor.index_copy_(_input_tensor, dim=1, index=_index, tensor=_tensor)