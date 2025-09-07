
class Model(torch.nn.Module):
    def __init__(self, conv):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.convXd(x1)  # ConvXd
        v3 = torch.nn.functional.batch_normXd(v2) # BatchNormXd
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, xdim, 4)


