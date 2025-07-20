input_tensor = torch.empty(2, 3)
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)
torch.Tensor.baddbmm(input_tensor, batch1, batch2)