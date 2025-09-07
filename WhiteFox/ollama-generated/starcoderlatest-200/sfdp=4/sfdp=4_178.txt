
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_head = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
 
    def forward(self, qk, v):
        attn_weight = qk @ v / math.sqrt(qk.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = attn_weight + 0  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(attn_weight, dim=-1) # Apply softmax to the result
        output = attn_weight @ v  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(2, 3, 64, 64)  # Query tensor of shape [L_q, N, C] where L_q is length of query and N is batch size
k = torch.randn(2, 8, 64, 64)  # Key tensor of shape [L_k, N, H, W] where L_k is length of key and H and W are height and width of the feature map in each layer of the encoder
        attn_mask = torch.randn(2, 1, 64, 64)  # Attention mask for the softmax calculation


# Outputs from the model
        output = m(q, k)
        