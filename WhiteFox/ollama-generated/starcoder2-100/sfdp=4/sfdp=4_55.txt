
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1 / math.sqrt(d) # Initialize the scale parameter for scaling the dot product
        self.query = torch.nn.Parameter(torch.rand([32, d])) # Create a trainable query parameter of size [32 x 768]
        self.key = torch.nn.Parameter(torch.rand([30, d])) # Create a trainable key parameter of size [30 x 768]
 
    def forward(self, key): 
        v1  = F.normalize(query)
        v2  = v1 @ F.normalize(key).transpose(-2,-1) * scale
        v3  = F.softmax(v2 + attn_mask) # Apply the scaled dot product attention mechanism to compute attention weights
        return (v3 @ value) # Compute a weighted sum of the values tensor


# Initializing the model and generating inputs for it:
m = Model()
qk1 = torch.randn([8, 768])
qk2 = torch.rand([9, d] * 30)) 
attn_mask = torch.randn([7, 7], device='cuda') # Generate an attention mask of size [7 x 7]

