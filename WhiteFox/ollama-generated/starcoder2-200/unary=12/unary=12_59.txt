
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.activation = torch.nn.Sigmoid()
 
    def forward(self, x1):
         v1 = self.conv(x1)
         v2 = self.activation(v1) 
         v3 = v1 * v2
         return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
# Initializing the input tensor for the model
__input_tensor__ = torch.ones(2, 80, 32, 32).to('cuda')
