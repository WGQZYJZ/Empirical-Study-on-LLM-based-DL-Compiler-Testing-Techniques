
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv  = torch.nn.Linear(32, 64)
        self.scalef = math.sqrt(10.)
 
    def forward(self, x):
        v1  = self.qkv(x).transpose(-1, -2)
        v2  = v1.div_(math.sqrt(v1.size()[-1]))
        v3  = torch.nn.functional.dropout(v2, p=0.5, training=self.training)
        return (torch.bmm(v3, v2))


# Initializing the model
m  = Model()


# Inputs to the model