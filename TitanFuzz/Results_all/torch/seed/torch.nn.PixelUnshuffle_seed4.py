dtype = torch.FloatTensor
input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]).type(dtype), requires_grad=True)
pixel_unshuffle = torch.nn.PixelUnshuffle(2)
output = pixel_unshuffle(input)