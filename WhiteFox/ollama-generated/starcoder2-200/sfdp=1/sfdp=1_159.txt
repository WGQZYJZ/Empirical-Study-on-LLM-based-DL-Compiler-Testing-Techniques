
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.functional.linear(2048, 196)
 
    def forward(self, x):
        v1  = torch.matmul(x.reshape(-1, 25), self.matmul())
        return v1
