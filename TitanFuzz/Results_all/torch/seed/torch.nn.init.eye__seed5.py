input_data = torch.Tensor(2, 3).normal_(0, 1)
torch.nn.init.eye_(input_data)