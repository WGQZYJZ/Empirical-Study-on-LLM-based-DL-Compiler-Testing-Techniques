
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64 **2, 3)

    def forward(self, x1):
        v1 = self.linear(x1) # Applies a linear transformation to the input tensor
        v2 = (v1 > 0).float() 
        v3 = v1* negative_slope # Multiplies each element in t1 by a negative slope. If an element is greater than 0, this will be zero. Otherwise, it will multiply the negative of that element instead. This is the equivalent of Leaky ReLU
        v4 = torch.where(v2, v3 ,v1) # For each element in v2, if that element is True (greater than 0), choose the corresponding element from v1; otherwise, choose the corresponding element from v3
        return v4

# Initializing the model
m = Model()
negative_slope = .5

# Inputs to the model
x1 = torch.randn(128, 8*64**2)
