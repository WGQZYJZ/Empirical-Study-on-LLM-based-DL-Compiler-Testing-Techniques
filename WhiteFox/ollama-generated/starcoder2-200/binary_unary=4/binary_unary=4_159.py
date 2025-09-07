
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x1): 
        v1  = self.linear(x1) #Apply a linear transformation to the input tensor
        v2  = v1 + other     #Add another tensor to the output of the linear transformation
        v3  = torch.relu(v2) #Apply the ReLU activation function to the result
        return v3

# Initializing the model and passing in arguments for forward method invocation (model should be different from the previous one).
m1 = Model()
__output__= m1(x1, other=torch.randn((10, 5)))

