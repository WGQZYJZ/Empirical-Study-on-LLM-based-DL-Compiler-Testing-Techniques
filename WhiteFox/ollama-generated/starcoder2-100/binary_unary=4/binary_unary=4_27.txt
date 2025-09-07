
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(48, 10)
 
    def forward(self, x2, other=None):
        v7  = self.linear(x2)
        v8  = v7 + (other if isinstance(other, torch.Tensor) else None) # added
        v9  = F.relu(v8) 
        return v9


# Initializing the model and setting `other` keyword argument to a random tensor:
m10  = Model()
rand_tensor  = torch.randn(256, 48)
__output__   = m10(rand_tensor, other=rand_tensor)

