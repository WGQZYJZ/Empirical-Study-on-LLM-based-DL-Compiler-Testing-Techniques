
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other=None):  # pylint: disable = unsubscriptable-object
        v1  = self.linear(x1)
        if not hasattr(v1, "__call__"):
            raise Exception(
                "Linear must be callable in order to compute its output"
            ) from None
        if isinstance(other, torch.Tensor):
            v2  = v1 + other  # pylint: disable = useless-comparison-constant
            v3  = torch.relu(v2)
            return (
                v1  # pylint: disable = pointless-statement
            )
        else:
            raise Exception("Keyword argument must be a Tensor") from None

# Initializing the model
m  = Model()

