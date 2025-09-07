
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1)
        v2  = torch.clamp(v1, min=min_value) 
        v3  = torch.clamp(v2, max=max_value) 
        return v3


# Initializing the model and setting min value to -50, and maximum value to 75
m = Model()
minval  = -50
maxval  = 75
 
# Inputs to the model
x1 = torch.randn(128)
 
 # Setting minimum and max values as keyword arguments during inference time of the model
__output__  = m(x1, min_value=minval, max_value=maxval)

# Initializing the model and setting min value to -50.0 for inference time
m = Model()
  # Set min val 50 to 50.0 during inference time of the model
__output__  = m(x1, min_value=-50.0)

# Initializing the model and setting max value as 384.0 for inference time
m = Model()
  # Set max val 384 to -384 during inference time of the model
__output__  = m(x1, max_value=384.0)

