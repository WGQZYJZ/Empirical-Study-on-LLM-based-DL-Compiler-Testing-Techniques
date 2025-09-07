
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 32, 512)
        self.sigm = torch.nn.Sigmoid()
 
    def forward(self, x): 
        v1  = self.linear(x)
        v2 = v1 * v1
        v3 = v1 * v3
        return v2


# Initializing the model and input tensor to the model. The input is initialized with 514 random numbers between -10 and 10, which matches the shape of the model's weight parameters.

m = Model()
x1  = torch.randn(64*32) * 10

