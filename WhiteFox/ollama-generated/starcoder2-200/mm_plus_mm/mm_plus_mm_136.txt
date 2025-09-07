
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: Tensor) -> Tensor:  # Addition of the results of two matrix multiplications
        res = torch.mm(x1, self._a_tensor) + \
            torch.mm(self._b_tensor, x2)

        return res

# Initializing the model
m = Model()


# Inputs to the model