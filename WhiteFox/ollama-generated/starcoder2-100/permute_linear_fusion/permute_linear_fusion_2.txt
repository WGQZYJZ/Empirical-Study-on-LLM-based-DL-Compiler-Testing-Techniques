
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1): 
        v1  = torch.randn(30, 40) 
        v2 = torch.cat((v1[:, None], self.linear.weight), dim=1) 
        v3 = F.softmax(torch.matmul(v2, x1))
        return v3


# Initializing the model