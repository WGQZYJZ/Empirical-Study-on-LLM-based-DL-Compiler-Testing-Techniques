

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.dropout(torch.nn.functional.linear(v1, self.linear.weight))
        return v2


# Initializing the model
m = Model()
