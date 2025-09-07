
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2): # both input tensors have 3 dimensions and the 3rd dimension is equal to 4
        v0 = torch.randn([1])
        v1 = x1.permute((0, 1)) + v0 * y2[:, 0] 
        v2 = torch.bmm(v1.reshape(-1, 1), v1) # or you can use torch.matmul for more efficiency on CPU
        return v2


# Initializing the model