
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.1, training=True, inplace=False)
        return v1


# Inputs to the model
x1 = torch.randn(1, 2, 2)
m = Model()
