
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout(0.5)

    def forward(self, x1): 
        v2  = torch.nn.functional.dropout(x1, self.dropout.p) # Call the dropout function
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
