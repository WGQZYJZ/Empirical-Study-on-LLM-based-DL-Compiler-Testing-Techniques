matrix = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
vector = torch.tensor([5, 6], dtype=torch.float32)
torch.Tensor.addmv_(matrix, matrix, vector)