input_tensor = torch.rand(1, 3, 224, 224)
logit_tensor = torch.Tensor.logit_(input_tensor)