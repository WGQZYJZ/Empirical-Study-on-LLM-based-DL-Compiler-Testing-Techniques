
class Model(torch.nn.Module):
    def __init__(self, sink_cat=False):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

        # If `sink_cat` is set to True then sinking cat in the optimization will be performed.
        self.sink_cat = sink_cat

    def forward(self, x1, x2):
        if self.sink_cat:
            return torch.cat([x1, x2], dim=-1)

        v1  = x1.permute(0, 2, 1)
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return torch.cat([v1, v2], dim=0)


# Initializing the model
m = Model()


