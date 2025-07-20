input_tensor = torch.randn(3, 3)
torch.Tensor.sgn_(input_tensor)
if torch.equal(input_tensor, torch.sign(input_tensor)):
    print('Output is correct')
else:
    print('Output is incorrect')