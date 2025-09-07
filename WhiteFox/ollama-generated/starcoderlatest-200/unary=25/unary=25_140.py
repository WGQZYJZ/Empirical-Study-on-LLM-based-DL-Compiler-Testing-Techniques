
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
        # The value of negative slope is different for each model and can be changed using set_negative_slope() function
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * self.negative_slope
        v3 = torch.where(v1, v1, v2)
 
        return v3


# Initializing the model
m = Model()

# Setting negative slope for this model (if this parameter is not specified, the default value will be used instead). Please set the negative slope to a value that corresponds to your specific needs.
negative_slope=0.1
m.set_negative_slope(negative_slope)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
