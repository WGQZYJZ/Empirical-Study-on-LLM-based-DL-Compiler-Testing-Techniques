
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None, x3=None, x4=None):
        v1  = torch.cat([x1, x2, ...], dim=...)
        v2  = v1.view(...)
        v3  = torch.relu(v2)
        if x4 is not None:
            v4 = v2.permute(0, 2, 1).contiguous()
            v5 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
            return v5
        else:
            return v3


# Initializing the model
m = Model()


