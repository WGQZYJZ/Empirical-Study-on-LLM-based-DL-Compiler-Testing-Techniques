
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(16384, 75)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2 # The output of the linear transformation is multiplied by the output of the sigmoid function
        return v3


# Initializing the model
m = Model()
 
# Input to the model (e.g., batch size = 8)
x1 = torch.randn(8, 16384)
 
