
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = torch.addmm(v1, v1, v1) # Perform a matrix multiplication of the input tensor by itself (in this case, it's done twice)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
