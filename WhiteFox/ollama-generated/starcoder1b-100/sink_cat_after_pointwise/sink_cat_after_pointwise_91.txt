
class Model(torch.nn.Module):
    def __init__(self, sink_cat_after_pointwise=False):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.sink_cat_after_pointwise = sink_cat_after_pointwise

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, v1], dim=-1).view(-1, 4) # Concatenate the tensors along a dimension -1
        if self.sink_cat_after_pointwise:
            return v3 + t2
        else:
            return v3


# Initializing the model
m = Model(sink_cat_after_pointwise=True)

# Inputs to the model
x1 = torch.randn(1, 2, 2) # The input tensor should not contain two dimensions
