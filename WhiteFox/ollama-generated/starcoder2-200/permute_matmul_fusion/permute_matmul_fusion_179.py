
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v2  = torch.randn(50)
        v4  = torch.bmm(x1[:, None], torch.expm(-v2[None, :])@y1)
        return v4


# Initializing the model
m  = Model()

# Input to the model with tensor A
__input_tensorA1__, __input_tensorA2__  = torch.randn(30), torch.randn(50)
__input_tensorA1__[:, None]
x1, y1 = m(__input_tensorA1__, __input_tensorA2__)

# Input to the model with tensor B
__input_tensorB1__, __input_tensorB2__  = torch.randn(30), torch.randn(50)
__input_tensorB1__[:, None]
x2, y2 = m(__input_tensorB1__, __input_tensorB2__)

