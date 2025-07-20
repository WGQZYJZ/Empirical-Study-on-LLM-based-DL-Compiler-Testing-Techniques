input_tensor = torch.arange(0, 12).reshape(3, 4)
torch.Tensor.index_copy_(input_tensor, dim=0, index=torch.tensor([0, 2]), tensor=torch.tensor([100, 200]))