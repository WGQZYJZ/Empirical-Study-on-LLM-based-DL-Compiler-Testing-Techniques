
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.softmax = nn.Softmax()
 
    def forward(self, x1, x2, x3):
        attn_weights = torch.cat((x2, x3), dim=-1)
        attn_mask = ((attn_weights != 0).float()) # (1,) x float64 x N
        attn_weights = self.softmax(attn_weights / math.sqrt(attn_weights.size(-1)))
        output = self.conv(x1) * attn_weights
        return output


# Initializing the model
m  = Model()


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
output_tensor = m(input_tensor, input_tensor, input_tensor)
