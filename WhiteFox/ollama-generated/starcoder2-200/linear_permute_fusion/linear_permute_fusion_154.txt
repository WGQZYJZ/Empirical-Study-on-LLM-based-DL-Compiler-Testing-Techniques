

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48, 1)

    def forward(self, x0, x2, x3):
       return torch.nn.functional.sigmoid(
            torch.nn.functional.tanh(
                (x0 * x2) + (((((-0.97655)) * x2) - ((-(-0.14481))) - 5) - x3)
            )
        ).permute(
            0, 1, 3, 2
        )


# Initializing the model