
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*64*64, 512)
 
    def forward(self, x1):
        v1  = self.linear(x1.reshape(-1)) 
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(43, 32, 64, 64) # Generate random inputs of size [N=43][C=32][H=64][W=64] for the input tensor with 512 units in the final layer 

