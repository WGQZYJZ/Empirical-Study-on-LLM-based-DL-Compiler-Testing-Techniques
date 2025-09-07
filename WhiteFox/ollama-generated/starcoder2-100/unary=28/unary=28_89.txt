
class Model(torch.nn.Module):
    def __init__(self, max_value=250, min_value=-10):
        super().__init__()
        self.linear = torch.nn.Linear(384, 96)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value) 
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with keyword arguments set to positive values
m  = Model() 

# Setting keyword arguments
m.__init__(max_value=70)
m.__init__(min_value=-15)

# Inputs to the model
x1  = torch.randn(2, 384)


# Initializing the model with keyword arguments set to negative values 
m  = Model() 

# Setting keyword arguments
m.__init__(max_value=0)
m.__init__(min_value=-50)

# Inputs to the model
x1  = torch.randn(2, 384)

