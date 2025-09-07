
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_weight = torch.nn.Linear(768, 512)
 
    def forward(self, x1):
        kd  = self.attn_weight(x1) # Compute the dot product of the query and key with weights
        v = self.attn_bias + torch.einsum('bihd,bijdh->bijdh', (kd, x1)) # Compute the attention output by softmax
        return v


# Initializing the model
m = Model()
# Inputs to the model
x2  = torch.randn(1, 1920, 384, 512)
