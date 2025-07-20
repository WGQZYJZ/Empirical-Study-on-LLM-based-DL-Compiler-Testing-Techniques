input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
torch.set_default_tensor_type(torch.FloatTensor)
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])