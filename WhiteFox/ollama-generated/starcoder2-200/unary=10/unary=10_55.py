
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 512)
        # torch.nn.init.uniform_(self.linear.weight, a=0, b=3/6) # Alternative
        self.linear_w1  = torch.nn.Parameter(torch.Tensor(512).normal_(mean=0, std=3/6))
        self.linear_b1  = torch.nn.Parameter(torch.zeros(512, requires_grad=True))
 
    def forward(self, x):
        v1  = self.linear(x) + 3 # Add the parameter self.linear_w1 to the result of the linear transformation applied to the input tensor and add another parameter named self.linear_b1. 
        v2  = torch.clamp_min(v1, min=0)
        v3  = torch.clamp_max(v2, max=6)
        return v3 / 6


# Initializing the model
m  = Model()
 
# Input to the model
x = torch.randn(8, 784)
__output__  = m(x).mean()

