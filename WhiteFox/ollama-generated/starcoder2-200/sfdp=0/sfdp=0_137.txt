

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, v1, v2, v3):
        v4 = torch.matmul(v1, v2.transpose(-2, -1)) / 5000.0
        v5 = v4.softmax(dim=-1) 
        v6 = v5.matmul(v3)
        return v6


# Initializing the model