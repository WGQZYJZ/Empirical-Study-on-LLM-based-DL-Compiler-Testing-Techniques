
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0 
        v3  = v1 * self.negative_slope
        v4  = torch.where(v2, v1, v3) # For each element in v2, if the element is True, choose the corresponding element from v1, otherwise choose the corresponding element from v3 (Leaky ReLU activation function).
        return v4


# Initializing the model and inputs to the model. Negative slope value: 0.5
m = Model(negative_slope=0.5)
x1  = torch.randn(2, 8, 32)
