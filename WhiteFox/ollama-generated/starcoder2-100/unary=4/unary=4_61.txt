
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5 
        return v6

# Initializing the model with different initialization weight and bias
m  = Model()


# Inputs to the model for initializing the model, and a valid input tensor. These inputs should be different from those in the previous task.

x1_init = torch.randn(243)

x1_valid = torch.randn(105)

__output__  = m(x1_valid)

