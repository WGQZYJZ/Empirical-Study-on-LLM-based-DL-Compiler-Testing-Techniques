
class Model(torch.nn.Module):
    def __init__(self, t1_, t2_):
        super().__init__()
        self.linear = torch.nn.Linear(t1_.shape[-1], 3)

    def forward(self, x1_, x2_=None):
        v1 = x1_.permute((0,) + tuple(range(-1, len(x1_.shape)-1)) + (len(x1_.shape)-1,))

        # Handle the situation where there is no tensor B. In this case, x2_ will be None and the following line will throw an error
        v3 = torch.bmm(v1, x2_)  # or torch.matmul(v1, x2_) if torch.bmm is not available on the device.

        # Handle the situation where there is a tensor B, in this case we swap the shape from (a0, b0) to (b0, a0). The permute method can handle 3D tensors of dimension 1 or higher
        v2 = x2_.permute((0,) + tuple(range(-1, len(x2_.shape)-1)) + (len(x2_.shape)-1,))

        # If we don't do the above swap, then the permute method will throw an error. The permute method can handle 3D tensors of dimension 1 or higher
        v4 = torch.bmm(v1, x2_)  # or torch.matmul(v1, x2)

        return self.linear(self.linear(v1), self.linear(x1_))


# Initializing the model with some tensor values. Do not change these initializations and do not generate a new input in order to make the example deterministic. You may generate a new input but it must be different from x1, or x2 for the output to be correct
x1 = torch.randn(3)
x2  = None
if True:
    x1, t1_, t2_ = torch.randn(4), torch.randn(5), torch.randn(6)
    t1_.permute((0,) + tuple(range(-1, len(t1_.shape)-1)) + (len(t1_.shape)-1,))

# Inputs to the model
if True:
    x2  = torch.randn(4)
else:
    x2  = None
__output__  = m(x1_, x2_)

