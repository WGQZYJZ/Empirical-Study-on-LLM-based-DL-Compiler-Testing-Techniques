
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2048, 1536)
        self.linear2  = torch.nn.Linear(1536, 792)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = self.linear2(v1) + other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
__other__  = torch.randn(792, 5184).requires_grad_() # Create a tensor for input data that requires gradient and is of shape (792, 5184)
x1  = torch.randn(3, 2048)

