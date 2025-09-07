
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        conv  = torch.nn.Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2))
        bn = torch.nn.BatchNorm2d(conv)
        output = conv(bn)(x1)

        return output

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 64, 75, 75)
__output__  = m(x1)

