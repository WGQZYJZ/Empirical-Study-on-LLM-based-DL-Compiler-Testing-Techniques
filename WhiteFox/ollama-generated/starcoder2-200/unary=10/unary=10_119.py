
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(32, 8)

    def forward(self, x1):
        v1 = self.l1(x1) 
        v2 = v1 + 3
        v3 = F.clamp_min(v2, 0.) # This line is used to clamp the result of addition operation with minimum value as zero
        v4 = F.clamp_max(v3, 6.) # This line is used to clamp the result of previous operation with maximum value as six. 
        v5 = v4 / 6.            # This line is used to divide the result of previous operation by 6. 
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1,32)
__output__  = m(x1)
