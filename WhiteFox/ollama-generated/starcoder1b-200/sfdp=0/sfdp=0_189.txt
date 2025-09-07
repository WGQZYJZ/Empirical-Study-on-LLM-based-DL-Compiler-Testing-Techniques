
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # (Batch size, Sequence Length, Embedding Size)
        v1 = self.conv(x1)
 
        # Compute the Scaled Dot-Product Attention mechanism
        v2 = torch.matmul(v1, v1.transpose(-2, -1)) / torch.sqrt(torch.pow(self.embed_dim, 0.5).unsqueeze(-1)).unsqueeze(-1)
 
        # Compute a weighted sum of the value tensor
        output = torch.matmul(v2, x1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
