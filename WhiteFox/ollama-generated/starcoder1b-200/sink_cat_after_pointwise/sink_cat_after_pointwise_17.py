
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @torch.jit._overloadable
    def forward(self, x1, *args, **kwargs):
        pass  # TODO: add a description of overloadable function

    @torch.jit._overloadable
    def forward(self, x1, *args, **kwargs):
        pass  # TODO: add a description of overloadable function


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3)
