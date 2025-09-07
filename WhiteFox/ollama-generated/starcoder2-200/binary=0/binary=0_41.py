
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.__other__
        return v2


# Initializing the model with a random tensor as other variable to be added
m_initialized  = Model()
 
# Inputs to the model that will be passed into forward pass function
input_to_model  = torch.randn(1, 3, 64, 64)

 # Random tensor for "other" parameter in addition operator
other = torch.randn(2, 8, 5, 5).cuda()
 
# Initializing the model with a random tensor as other variable to be added
m_initialized._modules['conv'].weight = other
 
 
