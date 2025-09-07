
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(32, 500)
        self.lin2 = torch.nn.Linear(500, 487)
 
    def forward(self, x1):
        v1  = self.lin1(x1)
        v2  = v1 - other
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
other = torch.randn(487).abs() * 0.5 # random float with absolute value


# Inputs to the model: a random input tensor, and the above 5-d one. 
x1 = torch.randn(239, 62, 255) # 1-d, 2-d or higher dimension tensors
x2 = torch.randn(487, 500, 457)


# Outputs from the model: a random output tensor (of shape 1-d), and another random tensor of shape 3-d (not necessarily different from x2). 
__output_from_model1 = m(x1) # Shape is 1-d, 2-d or higher dimension. 
__output_from_model2 = m(x2)

