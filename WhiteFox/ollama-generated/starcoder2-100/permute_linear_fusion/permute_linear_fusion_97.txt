
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(2) # generate a new vector with the same shape as the original one
        v2  = torch.nn.functional.linear(v1, self.weight)

        return None


# Initializing the model
m = Model()


# Inputs to the model
x1 = np.random.randn(30).reshape((5,6)) # shape: (5, 6)
__output__  = m(v2)