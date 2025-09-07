
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.weight[0], self.bias[0])
        v2 = torch.cat([v1], dim=1)
        return v2
 
 # Initializing the model
m = Model()
 
# Weights of a linear layer
self.weight 0: Tensor
# Bias terms of a linear layer
self.bias 0: Tensor


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
