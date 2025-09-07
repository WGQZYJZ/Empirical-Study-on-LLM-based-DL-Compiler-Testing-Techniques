
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 256)
 
    def forward(self, x1):
        v1  = self.linear(x1.reshape(-1)) # Flatten the input tensor and apply a linear transformation to it
        v2  = v1 + other
        return v2


# Initializing the model
m  = Model()


# Inputs to the model (assuming the initial input shape of [N,3,64,64])
x1  = torch.randn(50, 3, 64, 64)
__output__  = m(x1)
