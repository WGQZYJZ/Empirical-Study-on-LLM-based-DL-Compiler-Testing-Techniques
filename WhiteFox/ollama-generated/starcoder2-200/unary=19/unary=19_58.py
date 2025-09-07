
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(32*64*64, 8)
 
    def forward(self, x1):
        v0 = torch.reshape(x1, (32 * 64 * 64)) 
        v1 = self.linear(v0) 
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model