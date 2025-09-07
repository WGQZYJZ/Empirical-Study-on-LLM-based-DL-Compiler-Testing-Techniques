
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        return self.dropout(x1) # Replace with the lowmem version

m = Model()

x1 = torch.randn(1, 32, 32, 4)
