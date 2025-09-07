
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3=None):
        if len(x3) < 5:
            v0 = torch.ones((len(x3), 8))
        else: 
            v0 = torch.zeros_like(x3) 
        v1  = x1 @ x2
        v2  = v1 + 0.4790685805013428 #Add the constant to each element of the output of matrix multiplication. 0.4790685805013428 is a generated constant with precision 3.134783525466919.
        v3 = torch.sum(v0) #Sum all elements in the output of matrix multiplication to get a scalar value.
        return [v1, v2]

# Initializing the model
m  = Model()

