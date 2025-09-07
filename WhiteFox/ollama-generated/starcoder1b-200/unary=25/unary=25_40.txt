
class Model(torch.nn.Module):
    def __init__(self, positive_slope=100):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.negative_slope = positive_slope
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).float() # Convert each element of the boolean tensor to a floating point value in [-1,1] range where True is mapped to 1 and False is mapped to -1
        v3 = torch.where(v2, v1, (-self.negative_slope * v2)).float() # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return v3


# Initializing the model
m = Model(positive_slope=10)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
