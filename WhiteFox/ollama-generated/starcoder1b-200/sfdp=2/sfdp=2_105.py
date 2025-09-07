
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 512)
 
    def forward(self, x1):
        v1 = self.attn(x1)
        return v1


# Initializing the model
m = Model()


