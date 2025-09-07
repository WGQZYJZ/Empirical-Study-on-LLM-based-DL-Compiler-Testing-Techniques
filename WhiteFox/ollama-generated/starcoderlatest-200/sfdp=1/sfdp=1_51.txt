
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(1024, 1024)
 
    def forward(self, x):
        v  = self.matmul(x)
        return v


# Inputs to the model
query_embeds = torch.randn(256, 1024)
key_embeds = torch.randn(512, 1024)
