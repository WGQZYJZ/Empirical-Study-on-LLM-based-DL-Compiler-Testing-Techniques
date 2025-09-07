
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v3  = torch.relu(v1 + 0.) 
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(56, 512) # input tensor

# Predicting from the model using an output tensor of zeros that has shape [56, 10]
__output__  = m(x1)

