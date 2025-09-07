
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v  = torch.split(x1, [256], dim=0) # split along dimension 0 
        res = []
        for tensor in v:
            res += torch.split(tensor, [34], dim=1)# split along dimension 1
        return tuple([torch.cat((x, y), 0) for x,y in zip(res[::2], res[1::2])])


# Initializing the model
m = Model()
 
# Inputs to the model: 48 3 channel tensors of shape [batch_size=1; 65; 256] 
x1s = []
for i in range(48):
    tensor = torch.randint(0, 9, size=(1, 65, 256), dtype=torch.int32) 
    x1s += [tensor]
x1 = torch.stack(x1s).view(-1, 3, 64, 64)# Viewing the input as a single 8-D tensor

__output__  = m(x1)

