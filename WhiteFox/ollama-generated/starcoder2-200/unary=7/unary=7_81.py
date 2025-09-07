
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.clamp(min=0, max=6, input=v1 + 3) # Clamp the output of the linear transformation added with `3` to a value between `0` and `6`. This pattern is typically seen in models implementing a form of scaled exponential linear unit (SELU).
        v3 = v2 / 6  # Divide the clamped output by `6`, yielding a result that ranges from -1.57894 to +1.0 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(2, 10)
__output__  = m(x1)

