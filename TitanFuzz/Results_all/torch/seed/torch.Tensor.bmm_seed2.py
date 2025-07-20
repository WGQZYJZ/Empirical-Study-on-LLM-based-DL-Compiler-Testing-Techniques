input_tensor = torch.rand(3, 5, 4)
batch2 = torch.rand(3, 4, 6)
torch.Tensor.bmm(input_tensor, batch2)