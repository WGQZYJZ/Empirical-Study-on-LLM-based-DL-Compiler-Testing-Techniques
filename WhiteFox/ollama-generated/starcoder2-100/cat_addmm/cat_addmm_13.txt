
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        
        self.fc1  = torch.nn.Linear(784, 20) # Applying a fully connected layer with 784 inputs and 20 outputs
        self.relu = torch.nn.ReLU()           # ReLU activation function
        self.fc2  = torch.nn.Linear(20, 10)   # Applying another fully connected layer with 20 inputs and 10 outputs
    
    def forward(self, x):
        
        # Inputs to the first fully-connected layer 
        v1  = x.view(-1, 784)
        v2  = self.fc1(v1)
        v3  = self.relu(v2)
        
        # Concatenating the output of the first fully connected layer with the output of the second fully connected layer along a specific dimension
        v4  = torch.cat([v3, self.fc2(v3)], dim=0)

        return v4


# Initializing model
m = Model()

 # Input to the model
x1  = torch.rand(785).reshape(-1, 1, 29, 29)
 
 # Outputs of the model with two different inputs x1 and x2
y   = m(torch.ones([30], dtype=float)).shape
 
