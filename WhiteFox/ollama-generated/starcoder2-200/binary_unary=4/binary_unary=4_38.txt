
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if not isinstance(other,torch._C.TensorBase):
            raise RuntimeError('Expected argument "other" to be torch.*Tensor.')
        else:
            v2  =v1 + other
        v3  = F.relu(v2) 
        return v3

# Initializing the model
m = Model()

