input_tensor = ((torch.rand(4, 4) * 20) - 10)
torch.Tensor.clip(input_tensor, min=(- 5), max=5)
input_tensor = torch.rand(4, 4)
torch.Tensor.index_select(input_tensor, 0, torch.tensor([0, 2]))