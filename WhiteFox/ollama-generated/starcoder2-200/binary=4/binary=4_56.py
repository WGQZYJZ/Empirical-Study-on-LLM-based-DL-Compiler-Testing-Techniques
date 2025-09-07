class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3200, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) + v2  # v2 is a tensor that will be initialized to None or randomly generated.
        return v1
