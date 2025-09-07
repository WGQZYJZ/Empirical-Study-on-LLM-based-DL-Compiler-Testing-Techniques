
class Model(torch.nn.Module):
    def __init__(self, input1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear  = torch.nn.Linear(input1[0] * input1[0], 16)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.cat([v1 for _ in range(len(input1))]) 
        return v2


# Initializing the model