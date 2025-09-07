
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if min_value is not None and max_value is not None:
            self._min_value = torch.tensor(min_value).type(torch.get_default_dtype())
            self._max_value = torch.tensor(max_value).type(torch.get_default_dtype())
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, self._min_value)
        v3  = torch.clamp_max(v2, self._max_value)
        return v3


# Initializing the model with keyword arguments min_value=0 and max_value=-1
m = Model(min_value=0, max_value=-1)
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
# Initializing the model with keyword arguments min_value and max_value as None and -5 respectively
m2  = Model()
 
 
# Initializing the model with keyword arguments min_value=0 and max_value=-1
m3  = Model(min_value=0, max_value=-5)

 # Inputs to the model for m2.forward()
x2  = torch.randn(1, 3, 64, 64)
 
 
 
# Inputs to the model for m2.forward() and m3.forward(), respectively
x2  = torch.randn(1, 3, 64, 64)

 # Inputs to the model for m3.forward(), as previously defined in m2.forward() above is not provided here;
x3  = torch.randn(1, 3, 50, 50)
 
 
 
 
