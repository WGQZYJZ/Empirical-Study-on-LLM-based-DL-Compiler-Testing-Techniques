
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(8, 8)
 
    def forward(self, x, k, v):
        bsz, c, h, w = x.shape
        qk = (x @ k.transpose(-2, -1)) / math.sqrt(h * w) + attention_mask
        attn_weights = torch.softmax(qk, dim=-1)
        output = attn_weights @ v  # Compute the dot product of the attention weights and the value
        return self.fc(output)


# Initializing the model
m = Model()


