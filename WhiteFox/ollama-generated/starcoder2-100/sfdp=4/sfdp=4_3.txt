
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        vq  = (q @ k.transpose(-2, -1)) / math.sqrt(v.size(-1)) 
        attn_mask  = torch.ones((k.shape[-2], k.shape[-1]), device=v.device)  # Create a mask to prevent attention between positions
        vq  += attn_mask
        
        attn_weight  = torch.softmax(vq, dim=-1) 
        attn_output  = attn_weight @ v
        return attn_output


# Initializing the model
m  = Model()

# Inputs to the model: 3 tensors q, k and value with shape (256, 4096), (256, 1) and (256, 768). 
v.shape  = (256, 768)
k.shape  = (256, 4096)

