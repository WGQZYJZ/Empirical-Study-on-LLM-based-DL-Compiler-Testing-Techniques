
class Model(torch.nn.Module):
    def __init__(self, d1=50):
        super().__init__()
        self.fc = torch.nn.Linear(d1, 2)
 
    def forward(self, x):
        v1 = torch.addmm(x,  matA[:, :n], matB[0])  # Perform a matrix multiplication of matA and matB. Add it to the input 
        v2 = self.fc(v1)  # Apply fully connected layer with 50 units and 2 output dimensions
        return torch.cat([v2, v2], dim=dim)


# Initializing the model
m  = Model()
 
# Inputs to the model
x = torch.randn(16777216)
 
 
# Executing the model with a batch of size one
