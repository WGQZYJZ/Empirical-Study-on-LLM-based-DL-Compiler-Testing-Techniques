
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x1):
        v1  = torch.nn.functional.relu(x1) # The relu function will replace all of the dropout nodes
        v2  = self.dropout(v1)
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 50, 100)
