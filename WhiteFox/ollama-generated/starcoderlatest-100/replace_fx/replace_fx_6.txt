
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.3)
        v2 = torch.rand_like(v1, dtype=torch.float32, layout=x1.layout, device=x1.device, requires_grad=True)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 4, dtype=torch.float32, layout=torch.StridedLayout)
