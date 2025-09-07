
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(data=0.5, requires_grad=False)
        self.p  = torch.nn.Dropout2d(0.1, False)
 
    def forward(self, q, k, v):
        v1  = torch.matmul(q, k.transpose(-2, -1)) * self.scale 
        v2  = self.p(torch.nn.functional.softmax(v1, dim=-1)) # apply dropout
        v3  = v2 @ v 
        return v3

# Initializing the model