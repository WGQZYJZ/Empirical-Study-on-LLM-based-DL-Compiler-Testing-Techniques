
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.Tensor([200])
 
    def forward(self, x1):
        v1  = x1 * 3
        v2  = v1 + 5
        v4 = torch.matmul(v1 , v2)
        return v4


# Initializing the model