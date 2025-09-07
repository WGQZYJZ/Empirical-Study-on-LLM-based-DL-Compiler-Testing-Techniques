
class Model(torch.nn.Module):
    def __init__(self, inv_scale=1024):
        super().__init__()
        self.inv_scale = torch.tensor([inv_scale])
 
    def forward(self, x1):
        v3  = torch.matmul(x1, x1.transpose(-2, -1)) / self.inv_scale #scaled dot product
        v4  = v3.softmax(dim=-1)
        v5  = v4 * x1
        return v5

# Initializing the model
m  = Model()

