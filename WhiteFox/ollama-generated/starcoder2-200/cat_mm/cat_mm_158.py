
class Model(torch.nn.Module):
    def __init__(self, n_hidden):
        super().__init__()
        self.linear1 = torch.nn.Linear(32 * 64, n_hidden)
 
    def forward(self, x1, x2):
        v1  = x1 @ x2 # Matrix multiplication of two input tensors 
        v2  = torch.cat([v1 for i in range(n_layers)], dim=0) # Concatenation of the result tensor along a specified dimension
        return v2


# Initializing the model and specifying the value for n layers parameter, which is different from the previous one
m = Model(4)
 
# Inputs to the model
x1  = torch.randn(32, 64)
x2  = torch.randn(32 * m.n_layers, 32)

