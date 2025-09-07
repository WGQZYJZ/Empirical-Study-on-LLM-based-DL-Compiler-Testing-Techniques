
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model<|end_of_code|>
m = Model()

# Inputs to the model<|end_of_code|>
x1 = torch.randn(64, 256)

