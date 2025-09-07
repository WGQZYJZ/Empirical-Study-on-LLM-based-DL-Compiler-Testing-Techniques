
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x2], dim=0) # Concatenate a constant tensor (x2) with the input tensor `v1` along 0-dimension.
        v2 = v1.view(-1, 3, 4).relu() # ReLU is used as a pointwise unary operation on v1 after it is reshaped to 3 x 4.
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8) + 100 # random tensor with some fixed value of 100 added onto it.
x2 = torch.randn(7,4) # random input tensor with the size (7 x 4).
__output__  = m(x1)

