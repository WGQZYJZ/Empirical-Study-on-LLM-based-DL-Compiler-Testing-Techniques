_input_tensor = torch.randn(3, 4, 5)
batch2 = torch.randn(3, 5, 4)
torch.Tensor.bmm(_input_tensor, batch2)