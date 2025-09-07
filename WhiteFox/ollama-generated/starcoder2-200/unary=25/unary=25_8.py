
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.linear(x1) > 0 
        v3  = -v2.float() * negative_slope + v2.float() 
        v4  = torch.where(v2 == True , v2 != False )
        return v4

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3) # input tensor with shape (batch size x number of features), which is required by the model's linear transformation layer
