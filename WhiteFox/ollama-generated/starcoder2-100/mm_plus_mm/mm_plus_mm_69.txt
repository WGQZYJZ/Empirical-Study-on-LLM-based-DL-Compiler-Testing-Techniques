
class Model(torch.nn.Module):
    def __init__(self, input1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2  = torch.nn.Conv2d(input1, 8, 1, stride=1, padding=0)

    def forward(self, x): # __input__  = input1, input2, input3, input4
        v1  = self.conv(x)
        v2  = torch.mm(v1, x) # __input__  = t1
        v3  = torch.mm(v2, x) # __input__  = t1, t2
        v4  = v1 + v3         # __input__  = t1
        return v4
# Initializing the model