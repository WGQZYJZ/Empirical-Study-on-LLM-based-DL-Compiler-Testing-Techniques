
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


# Initializing the model with 'other' as an argument to the __init__() function of the class Model()
m  = Model(torch.tensor([0., 1., 2.], device="cuda", dtype=torch.float32))


# Inputs to the model, with 'other' as a tensor for the model
x1  = torch.randn(1, 3, 64, 64)
