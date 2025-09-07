
class Model(torch.nn.Module):
    def __init__(self, inputSize = 6400, numClasses=132):
        super().__init__()
        self.linear1 = torch.nn.Linear(inputSize , 512)
        self.linear2 = torch.nn.Linear(512,numClasses )
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the linear transformation 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model