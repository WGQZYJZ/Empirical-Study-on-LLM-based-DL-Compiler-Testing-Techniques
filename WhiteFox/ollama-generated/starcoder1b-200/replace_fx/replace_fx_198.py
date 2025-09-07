
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @torch.jit._recursive_trace()
    def forward(self, x1):  # Only the first input is used in the model.
        pass


# Inputs to the model
x1 = torch.randn(1, 2, 2)
