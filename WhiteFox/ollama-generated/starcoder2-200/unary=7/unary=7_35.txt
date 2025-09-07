
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(7, 3501)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(min=0, max=6, input=v1 + 3) # clamp() is the clamp operation that we are interested in
        v3 = (v2 / 6).to(torch.float32)
