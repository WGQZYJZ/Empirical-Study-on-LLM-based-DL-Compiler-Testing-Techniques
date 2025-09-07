
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1.view(-1, 4)
        return v3

    # sink_cat_after_pointwise: Apply the pattern on a set of linear models
    @sink_cat_after_pointwise()
    def sink_cat_after_pointwise(self):
        v1 = torch.cat([x1, x2], dim=1)
        return self.linear(v1)


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 2, 2)
