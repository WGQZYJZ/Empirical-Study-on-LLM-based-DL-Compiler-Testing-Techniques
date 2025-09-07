
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):
        return self.dropout(x1)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(100, 2048, 512, dtype=torch.float64)
