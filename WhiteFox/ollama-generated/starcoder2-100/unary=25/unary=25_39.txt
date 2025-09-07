
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v0   = self.linear(x1)
        v1  = v0 > 0
        v4  = negative_slope 
        v5  = v0 * v4
        v6  = torch.where(v1, v0, v5) # where(a, b, c) returns elements from tensor a where the corresponding element in the boolean mask is True and elements from tensor b elsewhere; elements from c are chosen when the mask is False.
        return v6

# Initializing the model 
m = Model()

# Inputs to the model 
x1 = torch.randn(20, 3)

# Initial call to forward function without any input
v_0   = m(x1)

# Call forward function with input value of 5.0 for the first 4 columns and -5.0 otherwise in v6 
v_7 = torch.where(v_1, x1[:, :4], 5*x1[:, :3] + 2*x1[:, 4:])

