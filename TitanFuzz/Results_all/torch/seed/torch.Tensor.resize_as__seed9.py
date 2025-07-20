input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor()
torch.Tensor.resize_as_(output_tensor, input_tensor)
input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor()
torch.Tensor.resize_