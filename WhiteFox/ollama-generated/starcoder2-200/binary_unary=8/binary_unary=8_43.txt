
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        t0 = torch.randn_like(x) # Generate a new input for the model using randomly generated tensor data with the same size of `x`
        v1 = self.conv(t0) 
        t2 = v1 + other
        t3 = torch.relu(t2)

        return t3

# Initializing the model and setting the values to the tensors in the model.
m  = Model()
t0, t1, t2 = (torch.randn((1,) + x1.shape[1:]) for _ in range(3)) # Generating three tensors
m.conv.weight = t1 
m.conv.bias   = t2 

# Inputs to the model. We use the input generated above to initialize `x`.
x_init  = torch.randn((1,) + x0.shape[1:])

