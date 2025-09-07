
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 25)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.sigmoid(v1) # Add code here: apply sigmoid function
        return v2


# Initializing the model
m = Model()
