
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3 
        v2  = v1.clamp_min_(0).clamp_max_(6) # clamp_min_: Clamp the value or values in a Tensor to at least a minimum value and at most a maximum value.
                                            # clamp_max_: Clamp the value or values in a Tensor to at least a minimum value and at most a maximum value.
        v3  = v2 * v1 
        return v3 / 6


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

