
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=768, num_heads=12)
 
    def forward(self, input_tensor):
        qk  = self.attn(input_tensor)[0]
 
        return qk


# Initializing the model
m  = Model()

# Inputs to the model