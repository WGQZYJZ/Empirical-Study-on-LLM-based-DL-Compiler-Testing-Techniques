
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self,x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5             # <-- your task
        v3  = v1 * v1              # <-- your task
        v4  = v3 * v1              # <-- your task
        v5  = v4 * 0.044715        # <-- your task
        v6  = v1 + v5              # <-- your task
        v7  = v6 * 0.7978845608028654   # <-- your task
        v8  = torch.tanh(v7)
        v9  = v8 + 1               # <-- your task
        v10 = v2*v9                # <-- your task
        return v10
