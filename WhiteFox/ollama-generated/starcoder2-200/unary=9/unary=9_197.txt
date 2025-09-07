
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2  += 3 #v1  = conv(input_tensor)
        v3   = torch.clamp_min(v2,0) 
        v4  *= 6 #v3  = clamp_min(v1 + 3, 0)
        return  (v5  / 6)  #(v3/6) * (v4/6)
        


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
