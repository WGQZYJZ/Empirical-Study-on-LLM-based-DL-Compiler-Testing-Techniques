
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2=None):
        if inp2 is None:
            return self.conv(inp1)
        else:
            v1 = self.conv(inp1)
            v2 = v1  + inp2 # Add the result of matrix multiplication on 'v1' to 'inp2'
            return v2


# Initializing the model
m = Model()


