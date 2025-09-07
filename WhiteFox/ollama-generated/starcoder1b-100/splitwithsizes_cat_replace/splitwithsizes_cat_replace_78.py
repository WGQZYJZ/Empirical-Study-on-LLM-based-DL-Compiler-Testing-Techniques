
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        return True if torch.split(input_tensor=x1, split_sizes=[400], dim=1)[0] == x2 and torch.cat([x2, x3]) == x3 else False

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 400)
x2  = torch.randn(400, 400)
x3  = torch.randn(400, 400)
