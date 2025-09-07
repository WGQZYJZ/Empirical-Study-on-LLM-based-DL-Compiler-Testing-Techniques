
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512, 384)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = F.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(50, 4, 768) # a tensor with shape (batch_size, 1, 1)
__output__  = m(x1)

