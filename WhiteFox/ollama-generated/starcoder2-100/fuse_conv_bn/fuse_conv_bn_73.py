
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        conv  = torch.nn.ConvXd(x1) # X can be 1,2 or 3 representing the dimensiob
        bn = torch.nn.BatchNormXd(conv) # X should match with ConvXd

        return bn


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 8, 50)
__output__  = m(x1)

