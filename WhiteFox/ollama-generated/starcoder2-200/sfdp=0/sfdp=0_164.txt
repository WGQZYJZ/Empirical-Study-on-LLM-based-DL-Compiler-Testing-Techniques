
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(840, 96) # Initialize the first Linear layer with input dimensionality of 840 and output dimensionality of 96
        self.layer2 = torch.nn.Linear(96, 37)
 
    def forward(self, x1):
        x = self.layer1(x1) # Perform a matrix multiplication between the input tensor and the first Linear layer
        x = F.relu(x) 
        x = self.layer2(x) # Perform another matrix multiplication between the output of the previous layer and the second Linear layer with 37 output units (since this model expects an output dimensionality of 37 for its outputs)
        return x


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(64, 840)
__output__  = m(x1)

