
class Model(torch.nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.emb = torch.nn.Embedding(len(vocab), emb_dim)
        self.emb.weight.data.uniform_(-1e-3, 1e-3) # Set embeddings to zero, so the training procedure is simple and deterministic
        self.conv1 = torch.nn.Conv2d(emb_dim, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 32, 1, stride=1, padding=0)
        self.pool = torch.nn.MaxPool2d((16, 16))
 
    def forward(self, x):
        v1 = self.emb(x)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = self.pool(v3)
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
__input__ = torch.randn(1, 64, 64)
x2 = m(__input__)
