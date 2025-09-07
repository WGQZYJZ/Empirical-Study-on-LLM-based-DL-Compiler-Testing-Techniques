
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_value=-65849) # clamping the minimum value to -65849 for "linear" layer in this example
        v3  = torch.clamp_max(v2, max_value=70000) 
        return v3

# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(485, 32) # The size of this input tensor is 399*32. "399" is 399, and "32" is the size of the vector that is used as an input for the model
__output__  = m(x1)

