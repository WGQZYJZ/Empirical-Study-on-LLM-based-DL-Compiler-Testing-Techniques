_input_tensor = torch.arange(0, 24).view(2, 3, 4)
_splits = torch.Tensor.split(_input_tensor, split_size=2, dim=0)
_splits = torch.Tensor.split(_input_tensor, split_size=2, dim=1)
_splits = torch.Tensor.split(_input_tensor, split_size=2, dim=2)