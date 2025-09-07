
class Model(torch.nn.Module):
    def __init__(self, len1):
        super().__init__()
        self.len = len1
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v2  = torch.cat([v1] * self.len) # Please note that this line is only for demonstration purposes and that it does not appear in the final solution. The actual implementation uses one more line `self.len - 1` times.
        return v2


# Initializing the model
m = Model(4)
 
# Inputs to the model
x1, x2  = torch.randn(3, 5), torch.randn(5, 7)
__output__  = m(x1, x2)