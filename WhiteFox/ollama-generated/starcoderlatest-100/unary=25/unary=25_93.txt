
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        negative_slope = 0.1
        t1 = v1 > 0
        t3 = v1 * negative_slope
        t4 = torch.where(t1, v1, t3) # Use a boolean tensor to apply Leaky ReLU activation function if necessary
        return t4

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1024, 2)
