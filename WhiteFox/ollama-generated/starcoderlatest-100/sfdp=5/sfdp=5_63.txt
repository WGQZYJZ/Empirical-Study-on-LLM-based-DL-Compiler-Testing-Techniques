
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.randn((16, 32))
        self.query = torch.randn((16, 32))

    def forward(self, x1, x2):
        k_v = torch.bmm(x1, x2) # Dot product between q and k. 
        return (k_v + attn_mask).softmax()
