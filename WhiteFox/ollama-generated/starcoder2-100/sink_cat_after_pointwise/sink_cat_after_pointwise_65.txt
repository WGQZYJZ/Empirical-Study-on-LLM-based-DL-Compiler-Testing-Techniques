
class Model(torch.nn.Module):
    def __init__(self, hidden1=42, hidden2=37):
        super().__init__()

    def forward(self, x0):
       return torch.cat([
            torch.relu(
                torch.view(
                    torch.concat([
                        torch.permute_dimensions(),
                        torch.transpose()
                        ]
                    ), 2, 1)
        ], dim=3)


# Initializing the model
m = Model()


# Inputs to the model
x0 = torch.randn(5, 84)
x1 = torch.randn(72)
x2 = torch.randn(96)
