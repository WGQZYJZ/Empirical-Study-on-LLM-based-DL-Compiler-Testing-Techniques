
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(p=0.5, inplace=False)

    def forward(self, x1):
        v1 = torch.nn.functional.relu6(x1 + 3, inplace=True)
        v2 = self.dropout(v1)
        return v2


# Initializing the model
m = Model()
m.eval() # Set model to evaluation mode

# Inputs to the model
x1 = torch.randn(5, 3, 64, 64) * (0.87 - 1.) + (1,)
