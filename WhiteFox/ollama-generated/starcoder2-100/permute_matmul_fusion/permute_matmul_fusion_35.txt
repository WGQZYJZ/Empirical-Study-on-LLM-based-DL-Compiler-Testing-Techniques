
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): # <-- this is a dummy model to check the code format
        v1  = x1.permute(0, 2, 1) 
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        t3  = torch.bmm(x2, v2) # <-- This is the permute and matmul combination.
        return t3


# Initializing the model
m = Model()


