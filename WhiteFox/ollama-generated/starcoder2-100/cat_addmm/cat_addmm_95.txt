
class Model(torch.nn.Module):
    def __init__(self, in_channels=1024):
        super().__init__()
        self.fc = torch.nn.Linear(in_channels, 512)

    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) # Add the matrices mat1 and mat2 to a given input tensor
        v2 = torch.cat([v1], -3)
        return v2

# Initializing the model
m = Model()

# Inputs to the model 
input_tensor = torch.randn(5, 4096).cuda() # Generates a random matrix of size [5x4096] on GPU

