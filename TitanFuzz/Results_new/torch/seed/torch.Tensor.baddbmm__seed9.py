batch1 = torch.rand(2, 3, 4)
batch2 = torch.rand(2, 4, 5)
output_tensor = torch.Tensor.baddbmm_(batch1, batch1, batch2, beta=1, alpha=1)