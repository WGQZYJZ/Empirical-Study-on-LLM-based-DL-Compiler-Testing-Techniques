
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = (v1*v1*v1)*0.47963 + v1
        v4  = torch.tanh(v3)*0.839075

        v5  = v2 + v4 
        return v5
# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(1, 3)

