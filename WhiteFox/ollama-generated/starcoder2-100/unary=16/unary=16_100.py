
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3*64**2, 10)
 
    def forward(self, x):
        v1 = self.linear(x.reshape(-1)) # Flatten the input tensor and apply a linear transformation to it
        v2 = F.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3,64**2)
__output__  = m(x1).softmax(-1)

