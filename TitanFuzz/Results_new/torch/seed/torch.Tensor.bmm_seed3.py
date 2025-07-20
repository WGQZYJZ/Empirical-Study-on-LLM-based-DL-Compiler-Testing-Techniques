_input_tensor = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
torch.Tensor.bmm(_input_tensor, batch2)