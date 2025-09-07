
class Model(torch.nn.Module):
    def __init__(self, sink_cat_after_pointwise=True):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self._sink_cat_after_pointwise = sink_cat_after_pointwise

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        if self._sink_cat_after_pointwise:
            v2 = torch.cat([v1, v1], dim=3)
        else:
            v2 = torch.cat([v1, v1], dim=2)
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
