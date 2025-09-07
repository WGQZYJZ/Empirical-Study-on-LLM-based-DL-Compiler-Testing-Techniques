
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        # Split input tensor into 4 tensors along dimension `2`. Note that for all splits of the same size, they will be concatenated in the order of their original split order.
        t1 = torch.split(x1, 4, dim=2)  
        # Concatenate tensors along dimension `2` from left to right (i.e., starting from tensor `0`).
        x6 = torch.cat([t1[0], t1[1], t1[2], t1[3]], dim=2)
        return x6


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)  
