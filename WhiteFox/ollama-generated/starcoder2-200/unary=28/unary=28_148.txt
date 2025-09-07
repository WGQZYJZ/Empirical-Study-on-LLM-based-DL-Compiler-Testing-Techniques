
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.linear  = torch.nn.Linear(2401, 5)
        if min_value is not None:
            self.min_value = nn.Parameter(torch.tensor([min_value]))
        else:
            self.register_parameter('min_value', None)
 
        if max_value is not None:
            self.max_value = nn.Parameter(torch.tensor([max_value]))
        else:
            self.register_parameter('max_value', None)

    def forward(self, x1):
        v1  = self.linear(x1)
 
        if self.min_value is not None:
            v2  = torch.clamp_min(v1, min=self.min_value) # Clamp the output of the linear transformation to a minimum value
        else:
            v2  = v1
 
        if self.max_value is not None:
            v3  = torch.clamp_max(v2, max=self.max_value) # Clamp the output of the previous operation to a maximum value
        else:
            v3  = v2
        
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 5)


