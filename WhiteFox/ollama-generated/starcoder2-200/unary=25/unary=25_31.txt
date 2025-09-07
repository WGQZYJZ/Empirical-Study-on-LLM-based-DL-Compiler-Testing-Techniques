
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * negative_slope
        v4 = torch.where(v2 == 1., v1, v3)
        return v4


# Initializing the model
m = Model()
__init_weight__ = m().requires_grad_() # We don't want the initial weights to be fixed when we fix our objective function. The purpose is to learn an adversarial example, not a good initialization for training.

# Inputs to the model 
x1 = torch.randn(64, 784)
__output__  = m(x1)

