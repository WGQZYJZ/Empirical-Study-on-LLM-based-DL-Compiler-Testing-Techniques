
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768 * 4 + 49, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1)
        return v2

m = Model()

 # Inputs to the model
    x = torch.randn(1024 * 65536)
    y_target = torch.zeros(1024, 8192)
    m(x)
