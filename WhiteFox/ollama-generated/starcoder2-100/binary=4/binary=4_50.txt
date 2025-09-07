
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5120, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn_like(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(50, 3 * 64  * 64) # Replace "64" with your actual input size.


# Inferencing on the model