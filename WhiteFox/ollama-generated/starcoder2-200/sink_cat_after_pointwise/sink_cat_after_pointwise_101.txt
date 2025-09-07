
class Model(torch.nn.Module):
    def __init__(self, **args):
        super().__init__()

        self.linear1 = torch.nn.Linear(*args)

    def forward(self, x1):

        return [
            (
                torch.cat([x1], dim=0),
                torch.nn.functional.relu(
                    self.linear1.weight @
                    torch.randn(2, 5).view(-1, 5) +
                    self.linear1.bias
                ),
                42,
            )
        ]

# Initializing the model
m = Model()


# Inputs to the model