
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu1 = torch.nn.ReLU()

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0) # This line triggers `sink_cat_after_pointwise` optimization.
        v2 = self.relu1(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 2, 2)
