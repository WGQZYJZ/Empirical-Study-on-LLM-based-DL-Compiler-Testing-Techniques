
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.linear  = torch.nn.Linear(**kwargs)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2)
        return v3
