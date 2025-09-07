
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).to(torch.float32) # .to(torch.float32) is to convert the tensor into a float type
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) 
        return v4

# Initializing the model
m = Model()
 
# Inputs to the model 
x1 = torch.randn(50, 3) # Note that this is different from the previous one!
__output__  = m(x1)

