
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128, 10)
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).to(torch.float32) * -1.0 
        v3  = v1 * negative_slope
        v4  = torch.where(v2 == True, v1, v3)
        return self.dropout(v4)

# Initializing the model