

class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.linear  = torch.nn.Linear(3 * 64  * 64 , 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(64 * 64, 3).reshape(-1, 3, 64, 64) 
 