
class Model(torch.nn.Module):
    def __init__(self, sink_cat_after_pointwise=False):
        super().__init__()
        if sink_cat_after_pointwise:
            self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = x1.view(-1, 3).permute(0, 2, 1)
        v2 = torch.relu(v1 @ self.linear.weight)
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(2, 4)
x2 = torch.randn(2, 3, 4)
