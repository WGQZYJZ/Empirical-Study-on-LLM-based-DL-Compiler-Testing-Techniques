
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
__input_1__  = torch.randn(30, 32 * 32 * 3) # input data with shape [30, 32*32*3]
 

# Output of the model on the input tensor x
__output__  = m(__input_1__)

