
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(784, 32)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.fc1(x1) # Applying linear transformation to the input tensor
        v2 = self.relu(v1) # Apply ReLU activation function to output of linear transformation 
        return v2

# Initializing model
m  = Model()


# Inputs to the model
x1=torch.randn(3,784)

 