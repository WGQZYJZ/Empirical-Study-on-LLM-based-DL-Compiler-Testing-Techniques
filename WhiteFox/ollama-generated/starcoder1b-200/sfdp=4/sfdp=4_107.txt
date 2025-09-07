
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
 
    def forward(self, x1, x2, attn_mask):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1).reshape((-1, v1.shape[-1] * v1.shape[-1]))
        v3  = torch.erf(v2) + 1
        v4 = x2 * v3 + attn_mask  # Scale the dot product by the attention mask to prevent computation of attention weights on certain positions
        return torch.tanh(v4)


# Initializing the model
m = Model()


