input_tensor = torch.rand(3, 3)
index = torch.tensor([0, 1, 2])
source = torch.tensor([1, 2, 3])
torch.Tensor.put_(input_tensor, index, source, accumulate=False)