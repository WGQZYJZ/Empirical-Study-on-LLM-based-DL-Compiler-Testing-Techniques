

class Model(torch.nn.Module):
    def __init__(self, nin=32, nout=10):
        super().__init__()

        self.linear = torch.nn.Linear(nin, nout)

    def forward(self, input):

        v1 = self.linear(input)

        v2 = v1 > 0

        # Leaky ReLU activation function
        v3 = v1 * negative_slope 

        v4 = torch.where(v2, v1, v3)

        return v4


# Initializing the model