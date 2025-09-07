
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 5, stride=2, padding=2)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.matmul(v1, x1) / math.sqrt(self.num_attention_heads * 8)
        v3 = torch.softmax(torch.matmul(v2, v2), dim=-1)  # Apply softmax to the attention weights from Scaled Dot-Product Attention
        v4 = torch.einsum('bijd,kcd->bcd', v3, self.key_projection)
        return v4


# Initializing the model
m = Model()


