
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(3, 2)
        self.dropout_p   = 0.5
        self.value        = torch.randn(8, 16, 48, 90, 72)
        self.dropout      = torch.nn.Dropout(self.dropout_p)
 
    def forward(self, x):
        v1    = self.qk(x)
        v3  = v1.div(5.)
        v4   = self.value
        v6  = v2 * v3 + v4
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(1, 90, 72)
