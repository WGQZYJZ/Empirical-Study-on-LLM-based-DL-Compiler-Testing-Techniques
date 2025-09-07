
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # 6-4
        v1 = x1.permute(0, 2, 1) 
        v3 = torch.bmm(v1, x2)  # 7-5, 8-9
        v2 = x2.permute(0, 2, 1) 
        v4 = torch.bmm(x1, v2) # 6-7 (same as 7-5 in previous pattern)
        return v3 + v4

# Initializing the model
m = Model()

