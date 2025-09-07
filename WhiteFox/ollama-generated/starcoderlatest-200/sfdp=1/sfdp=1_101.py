
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256, 384)
        self.linear2 = torch.nn.Linear(384, 256)
 
    def forward(self, qk_feature, v_feature):
        h1 = self.linear1(qk_feature) + self.linear2(v_feature) # Compute the attention output
        return torch.nn.functional.softmax(h1, dim=-1)  # Apply softmax to the output of the attention layer


# Initializing the model
att = Attention()

# Inputs to the model
qk = torch.randn(256, 384)
v_feature = torch.randn(100, 384)
qk_feature = torch.randn(256, 384)
