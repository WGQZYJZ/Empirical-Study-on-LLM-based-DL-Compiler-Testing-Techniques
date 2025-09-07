
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 * torch.clamp(min=0., max=6., input=v1+3.) # the output of the clamp function is then used to define a new variable (here v2). This pattern is typically seen in models implementing a form of scaled exponential linear unit (SELU) activation function, where the multiplication by `6` is not applied.
        v3 = v2 / 6. # the output of the division by 6 is then used to define another new variable (here v3). This pattern is typically seen in models implementing a form of scaled exponential linear unit (SELU) activation function, where the multiplication by `6` is not applied.
        return v1


# Initializing the model
m = Model()
 
 # Inputs to the model
x  = torch.randn(2048, 64)

 ##  # Initializing and running the model
 
 