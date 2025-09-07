
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):

        return (
            torch.nn.functional.linear(
                torch.bmm(
                    x1.permute((0, 2, 1)), 
                    y1.permute((0, 2, 1))
                    )
        )
        )


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3,4)
y1 = torch.randn(3,5)
__output__  = m(x1, y1).sum().item()
