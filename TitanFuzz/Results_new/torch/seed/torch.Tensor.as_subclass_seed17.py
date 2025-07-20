input_tensor = torch.randn(4, 3)
sub_class_tensor = torch.Tensor.as_subclass(input_tensor, torch.FloatTensor)