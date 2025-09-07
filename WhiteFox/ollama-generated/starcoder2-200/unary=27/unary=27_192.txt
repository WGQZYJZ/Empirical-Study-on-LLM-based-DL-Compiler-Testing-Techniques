
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
         v1  = self.conv(x1) 
         v2 = clamp_min(v1, -0.75)
         return clamp_max(v2,  0.99)


# Initializing the model and setting min value for clamping and max value for clamping in the forward function of the model's forward method is specified as 3.349
m = Model()
m(x1)  # Initialize input tensor with the model m


# Initializing the model and setting min value for clamping and max value for clamping in the forward function of the model's forward method is set to -0.75, and then we call the forward method on this model. The result of calling the forward method should be 3.2918

m = Model()


# Inputs to the model (same as above)
__output__  = m(x1)


