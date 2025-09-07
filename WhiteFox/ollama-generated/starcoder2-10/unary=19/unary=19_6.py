
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 8 * 8, 10)
 
    def forward(self, x):
        v1  = self.linear(x) 
        v2  = torch.sigmoid(v1)  
        return v2


# Initializing the model
m  = Model()

# Inputs to the model 
__input_tensor__ = torch.randn(30 * 8, 256 * 8 * 8)
 
# Run forward function and get output from the model
