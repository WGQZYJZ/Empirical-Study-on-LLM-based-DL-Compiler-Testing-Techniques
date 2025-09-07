
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.linear = torch.nn.Linear(128 * 7 * 7, 64)
        self.leakyrelu = torch.nn.LeakyReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        v5 = self.leakyrelu(v4) 
        return v5

# Initializing the model
m = Model()


Inputs to the model