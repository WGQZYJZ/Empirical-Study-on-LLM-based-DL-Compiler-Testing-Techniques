
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=1024, num_heads=8)
 
    def forward(self, qk_tensors):
        output = self.attention(qk_tensors[0],
                                qk_tensors[1],
                                qk_tensors[2])
        return output


# Initializing the model
m = Model()
q_tensor = torch.randn(4, 8, 512, 64) # Query tensors
k_tensor = torch.randn(4, 8, 512, 64) # Key tensors
v_tensor = torch.randn(4, 8, 512, 64) # Value tensor
