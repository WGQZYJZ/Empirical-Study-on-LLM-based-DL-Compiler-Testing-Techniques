
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        return torch.cat([input1, input2], dim=0).view(-1)


# Initializing the model
m  = Model()

# Inputs to the model
__input1__  = torch.randn(5)
__input2__  = torch.randn(3)

__output__  = m(__input1__, __input2__)
