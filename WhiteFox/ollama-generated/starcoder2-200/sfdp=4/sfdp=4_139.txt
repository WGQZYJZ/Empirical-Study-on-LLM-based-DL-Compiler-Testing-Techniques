
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Linear(4096, 768)
        self.key = torch.nn.Linear(4096, 768)
 
    def forward(self, x1, x2):
        v1 = self.query(x1).transpose(-2, -1)
        v2 = self.key(x2).transpose(-2, -1)
        v3 = v1 @ v2 / math.sqrt(v1.size(-1)) + attn_mask  # Compute the dot product of the query and key, and scale it by the square root of the dimension size
        v4 = torch.softmax(v3, dim=-1) # Apply softmax to the result
        v5 = v4 @ x2
        return v5


m  = AttentionModel()
 
 # Inputs to the model
__input_tensor_1__ = torch.randn(1, 4096) 
 __input_tensor_2__= torch.randn(1, 4096) 
output = m(__input_tensor_1__, __input_tensor_2__)

