
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        # Option 1
        v0 = x1.permute(0, 2, 1)
        v1 = torch.bmm(v0, x2)
        return v1


# Initializing the model
m = Model()

# Inputs to the model