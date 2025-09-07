
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3072, 8)
 
    def forward(self, x1):
        v1  = self.fc1(x1) # Apply a linear transformation to the input tensor
        v2  = F.relu(v1)   # Apply the ReLU activation function to the output of the linear transformation
        return v2
 
# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(3, 3072)
 
# Initializing a PyTorch optimizer
optimizer = optim.Adam(params=m.parameters(), lr=0.05)
 
# Defining the loss function
criterion = nn.MSELoss()
__output__  = m(x1)


