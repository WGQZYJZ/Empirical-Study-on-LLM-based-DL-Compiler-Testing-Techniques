
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        k1 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        v1 = value  # The attention mask is not needed here
        attn_weight = torch.softmax(k1, dim=-1) @ v1  # Compute the dot product of the attention weights and the value
        output = attn_weight @ self.conv(x1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        return output


# Initializing the model
m = Model()


