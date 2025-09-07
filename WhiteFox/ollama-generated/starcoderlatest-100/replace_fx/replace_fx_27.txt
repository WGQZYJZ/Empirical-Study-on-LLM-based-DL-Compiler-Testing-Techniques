
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(input_tensor, p=0.5)
        v2 = torch.rand_like(x1) * (1 - 0.5) + 0.5
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 3)
