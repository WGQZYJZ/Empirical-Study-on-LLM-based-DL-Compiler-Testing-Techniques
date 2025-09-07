
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Here, the batch size is not fixed
        conv = torch.nn.Conv2d(20, 30, kernel_size=5)
        bn = torch.nn.BatchNorm2d(30)

        output  = bn(conv(x))


# Initializing the model: m  = Model()

# Inputs to the model
x1 = torch.randn(4, 20, 8, 8) # batch size is fixed but not set with the value 4 here 

