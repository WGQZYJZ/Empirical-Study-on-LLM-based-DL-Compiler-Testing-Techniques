
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.linear(x1).permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, p=0.) # This node will not trigger the optimization of replace_fx.
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
