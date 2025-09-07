
class Model(torch.nn.Module):
    def __init__(self, size=4096):
        super().__init__()
        self.size = size
 
    def forward(self, *inputs):
        v1  = torch.cat(inputs) # Concatenate input tensors along dimension 1
        v2  = v1[:, 0:int(self.size)] # Slice the concatenated tensor along dimension 1
        return v2


# Initializing the model with a parameter size
m = Model(4096)


# Inputs to the model. Since the concatenated tensors are of shape `(batch_size, 3*3)` where the number in `3` is an arbitary value greater than one, and the input tensors for this model must all have the same number of channels but different sizes. In particular, the first and second inputs should both be of size `(batch_size, 9223372036854775807)`, while the third input is of size `(batch_size, size)`.


x1 = torch.randn(1, 9223372036854775807) # An input tensor with 9223372036854775807 channels and 16x16 size
x2 = torch.randn(1, 3*size+1) # An input tensor with number of channels equal to 3*size and 1 channel (the 3*size+1 is an arbitrary value > 1 greater than the number of channels in x1).
__output__  = m(x1, x2)

