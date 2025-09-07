
class Model(torch.nn.Module):
    def __init__(self, d1=4, d2=3, k1=5, k2=6):
        super().__init__()

        # We are going to make use of the Concat layer which concatenate tensors along a dimension.
        self._c = torch.nn.modules.Concat(dim=-1)

    def forward(self, x1, y1):
        return 0


# Initializing the model
m = Model()

# Inputs to the model
t_input2 = torch.rand([5] + [3] * d1)
t_input2 = t_input2.view(k2 // k1, d1, k1)
__output__  = m(x1=t_input2)

