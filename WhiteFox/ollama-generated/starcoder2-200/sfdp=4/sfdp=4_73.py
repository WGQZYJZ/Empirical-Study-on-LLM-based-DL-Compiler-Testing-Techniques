
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        qk  = (q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))) + attn_mask 
        attention_weights  = torch.softmax(qk, dim=-1)
        return attention_weights @ v
 

# Initializing the model
m = Model()

 # Input tensors to the model
query  = torch.randn(64, 80, 512)
key = query.clone().detach().requires_grad_(False).transpose(-2, -1) 
value  = torch.randn(64, 80, 512)
 
 # Inputs to the model
query, key, value  = query[3:7], key[:1] + query[7:], value[:, :3].sum(dim=1)

 # Run the model on the inputs
__output__  = m(query, key, value)

