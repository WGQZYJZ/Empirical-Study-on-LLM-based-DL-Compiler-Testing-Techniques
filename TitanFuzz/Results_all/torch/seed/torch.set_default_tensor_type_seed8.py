input_data = Variable(torch.randn(2, 3, 3))
target_data = Variable(torch.randn(2, 3, 3))
torch.set_default_tensor_type(torch.FloatTensor)