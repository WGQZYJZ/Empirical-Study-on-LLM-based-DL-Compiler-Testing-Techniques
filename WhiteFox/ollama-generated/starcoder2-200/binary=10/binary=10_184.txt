
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn(v1.shape).to(device="cuda") 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(10, 3, device='cuda') # Input tensor to the model with shape (10, 3) and 10 data points.
