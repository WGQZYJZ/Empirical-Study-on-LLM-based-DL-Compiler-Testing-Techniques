
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 7 * 7, 3072)
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, x1, x2):
        v1 = self.linear(torch.cat((x1, x2), dim=-1))
        v2 = self.dropout(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
