
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.cat(x)
        v2 = v1[:, -90:]  # Select the last 90 elements of v1 along dimension 1
        size  = len(v2) // 4 if (len(v2) % 4 != 0) else int(len(v2)/4) 
        v3  = v2[:size] # Slice v2 with length 90/4 to 90/4
        v4  = torch.cat([v1, v3], dim=1)
        return v4
 
# Initializing the model
m = Model()
 
 # Inputs to the model
x = []
for _ in range(8):
    v1 = torch.randn(256, 4, dtype=torch.float32)
    x.append(v1)

 __output__  = m(x)