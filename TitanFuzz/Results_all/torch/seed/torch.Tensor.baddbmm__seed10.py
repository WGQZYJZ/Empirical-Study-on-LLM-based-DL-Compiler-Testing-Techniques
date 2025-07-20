batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
result = torch.Tensor.baddbmm_(batch1, batch1, batch2)