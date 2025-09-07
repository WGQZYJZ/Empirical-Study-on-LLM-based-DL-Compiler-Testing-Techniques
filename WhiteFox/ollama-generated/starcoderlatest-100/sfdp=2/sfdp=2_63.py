
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout1 = torch.nn.Dropout2d(p=0.5)
 
    def forward(self, x1, x2):
        v1  = self.dropout1(x1) @ x2.transpose(-2, -1)
        return v1
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 32, 64, 64)
x2 = torch.randn(4, 32, 64, 64)
