input_data = torch.rand(3, 3)
torch.testing.assert_close(input_data, input_data, rtol=0.0001, atol=0.0001)