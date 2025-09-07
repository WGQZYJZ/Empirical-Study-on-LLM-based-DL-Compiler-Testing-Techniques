
class Model(torch.nn.Module):
    def __init__(self, dim1=2, dim2=8, num_heads=4):
        super().__init__()
        self.attend = torch.nn.MultiheadAttention(dim1, dim2, num_heads)
 
    def forward(self, x1, key, value):
        v1, attn  = self.attend(x1, key, value)
        return v1, attn


# Initializing the model
m = Model()


