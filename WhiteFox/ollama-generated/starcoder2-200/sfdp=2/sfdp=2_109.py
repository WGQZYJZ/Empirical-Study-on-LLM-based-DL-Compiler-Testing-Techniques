
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, query):
            return torch.matmul(query, key.transpose(-2,-1))
 
