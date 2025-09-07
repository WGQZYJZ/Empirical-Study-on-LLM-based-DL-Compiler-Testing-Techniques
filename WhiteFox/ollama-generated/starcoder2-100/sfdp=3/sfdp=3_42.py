
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, v103):
        v7 = torch.matmul(v104, v106.transpose(-2, -1))
        v8  = v7 * 5
        v9 = v8.softmax(dim=-1)
        v10 = torch.nn.functional.dropout(v9, p=3)
        return v10*v104


# Initializing the model
m = Model()
 
# Inputs to the model
v104  = torch.randn(256, 8, 8) # shape of the input query tensor, [256, 8, 8]
v103  = torch.randn(8*8, 7 * 8) # shape of the input key-value tensor for dot product attention, [7*8, 8*8]
 
