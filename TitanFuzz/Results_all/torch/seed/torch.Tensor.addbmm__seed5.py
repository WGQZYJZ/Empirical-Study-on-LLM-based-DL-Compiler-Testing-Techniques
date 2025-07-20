input_tensor = torch.rand(2, 3, 4)
batch1 = torch.rand(10, 2, 3)
batch2 = torch.rand(10, 3, 4)
torch.Tensor.addbmm_(input_tensor, batch1, batch2)