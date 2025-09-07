
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 250)
        self.key = torch.nn.Linear(768, 431)
        self.value = torch.nn.Linear(768, 798)
 
    def forward(self, input):
        vq = self.query(input).transpose(-2, -1) / math.sqrt(self.query(input).size(-1))
        vk = self.key(input).transpose(-2, -1) / math.sqrt(self.key(input).size(-1))
        qk = vq @ vk  # Computation of the scaled dot product
        attn_mask = torch.ones((798, 431), device='cuda', dtype=torch.bool) 
        # Set up a fixed mask for demonstration purposes in this example only
        attn_mask[0][-2] = False
 
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)  # Compute the softmax of the scaled dot product and add the attention mask to it
        out = attn_weight @ self.value(input)  # Perform a weighted sum with the value tensor and the attention weights as the weights
        return out

# Initializing the model
model  = AttentionModel()

# Inputs for the model 
inputs = torch.randn(798, 250).cuda().requires_grad_(True)

# Output of the model with respect to input tensor, 'v' denotes the outputs from the hidden states of BERT
