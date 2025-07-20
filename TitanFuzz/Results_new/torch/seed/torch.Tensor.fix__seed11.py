_input_tensor = torch.randint(low=0, high=255, size=(1, 3, 224, 224), dtype=torch.float)
torch.Tensor.fix_(_input_tensor)