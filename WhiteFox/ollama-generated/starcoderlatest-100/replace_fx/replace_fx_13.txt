
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.35)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.20)
        v2 = torch.rand_like(v1)
        return v2

# Initializing the model
m = Model()


