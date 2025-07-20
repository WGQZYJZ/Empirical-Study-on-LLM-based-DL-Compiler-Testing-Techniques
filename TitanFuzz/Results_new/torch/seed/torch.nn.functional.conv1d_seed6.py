input = torch.tensor([[[1, 2, 3]]], dtype=torch.float32)
weight = torch.tensor([[[1, 2, 3]]], dtype=torch.float32)
conv_out = torch.nn.functional.conv1d(input, weight)