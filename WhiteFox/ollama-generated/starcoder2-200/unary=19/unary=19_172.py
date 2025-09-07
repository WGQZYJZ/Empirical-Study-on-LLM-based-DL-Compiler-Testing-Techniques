
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32*32*8, 5)
 
    def forward(self, x1):
        v1  = self.fc(x1.reshape(-1)) # Flatten and apply the linear transformation to the input tensor
        v2  = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()


# Inputs to the model