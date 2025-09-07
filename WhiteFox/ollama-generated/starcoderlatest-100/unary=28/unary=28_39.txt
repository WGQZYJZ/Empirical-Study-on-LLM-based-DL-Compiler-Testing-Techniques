
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048, 2) # The dimension of the input tensor is (N x D) where N is a number and D is a number of features
x2 = torch.randn(2048, 5) # The dimension of the second input tensor is (M x E) where M is a number and E is another number of features
