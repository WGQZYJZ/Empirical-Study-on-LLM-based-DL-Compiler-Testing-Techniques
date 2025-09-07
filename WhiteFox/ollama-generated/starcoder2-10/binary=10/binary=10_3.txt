
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 1)
 
    def forward(self, x0):
        v1  = self.linear(x0.reshape(-1))
        v2  = v1 + torch.randn(v1.shape).to(torch.float32) # Add the noise tensor to the output of the linear transformation (specified by the keyword argument "other") 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x0  = torch.randn(1, 32 * 64 * 64) # Note: Do not change the shape of x0!


