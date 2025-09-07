
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.permute(x1, 0, 2, 1)
        v2 = torch.permute(x2, 0, 2, 1)
        v3 = torch.bmm(v1, v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model (inputs have to be different from each other). Please change the values of x1 and x2 in the code block below when you run the model.
x1  = torch.randn(2, 5)
x2  = torch.randn(3, 4)
