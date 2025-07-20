batch1 = torch.rand(10, 3, 4)
batch2 = torch.rand(10, 4, 5)
torch.Tensor.addbmm(batch1, batch2, beta=1, alpha=1)