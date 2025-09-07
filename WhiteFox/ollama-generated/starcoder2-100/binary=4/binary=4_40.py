
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(32, 1024) # Shape of input is (batch size, number of input features)

# Creating another tensor that we will add to our model output
other = torch.ones([32, 512])

 __output__  = m(x1).add_(other)

