
class Model(torch.nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model
 
    def forward(self, x1):
        x1_conv = self.model.conv(x1)
        v = self.model.attention(x1_conv) * 0.5
        v2 = v + self.model.attention(x1_conv)  # Add attention mask to scaled dot product
        w = torch.softmax(v, dim=-1)  # Apply softmax on output
        return w @ x1
