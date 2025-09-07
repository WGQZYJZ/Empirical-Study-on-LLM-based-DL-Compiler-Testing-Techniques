
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*8 * 8 ,10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 256*8*8))
        v2 = v1 + other # Other is an arbitary tensor, specified by the user
        return v2

# Initializing the model
m = Model()

 # Inputs to the model