
class Model(torch.nn.Module):
    def __init__(self, sink_cat=True):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

        if sink_cat:
            self.sink_cat_after_pointwise = True

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.relu(torch.cat([v1, v1], dim=2))

        if self.sink_cat_after_pointwise:
            t1, t2 = v2.split(dim=1, sep=[1, 2], index=1)
            return t1 + t2
        else:
            return v2


# Initializing the model
m = Model()


