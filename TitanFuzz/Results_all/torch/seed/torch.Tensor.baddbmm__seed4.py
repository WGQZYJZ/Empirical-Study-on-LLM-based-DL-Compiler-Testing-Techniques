batch_size = 3
input_size = 2
output_size = 4
input_tensor = torch.randn(batch_size, input_size)
batch1 = torch.randn(batch_size, input_size, output_size)
batch2 = torch.randn(batch_size, output_size, input_size)
output_tensor = torch.Tensor(batch_size, input_size, input_size)
torch.Tensor.baddbmm_(output_tensor, batch1, batch2)