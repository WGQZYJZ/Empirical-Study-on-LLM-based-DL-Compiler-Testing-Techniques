
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1


# Initializing the model and setting it to train mode
m = Model()
m.train()
 
# Input to the model (initialized with zeros in this example).
x1 = torch.zeros((3, 8))

 # Output of the model after forward pass. 
 __output__  = m(x1)