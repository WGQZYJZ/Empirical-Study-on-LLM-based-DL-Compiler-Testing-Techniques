
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
        # Implementation of scaled dot-product attention
        
        k  =   torch.einsum('...bij,...bj->...bij', [query]) # Compute the dot product of the query and key tensors

        q_s  =  torch.einsum('...bij,...bj->...bij', [query, k])  / math.sqrt(query.size(-1)) # Compute the scaled dot-product of the query and key tensors
 

        attn_mask= torch.nn.ZeroFillDropout(p=0)(torch.ones([key.shape[2],key.shape[3]])) 
        attn_mask[:, :, -1, :] =  float('-inf')
 
        q_s+=attn_mask 

        attention_weights  =  torch.softmax(q_s)

        return  torch.einsum('...bij,...bj->...bj', [attention_weights])

# Initializing the model
m  = Attention()

 # Inputs to the model
query = torch.randn(4, 16, 28, 50).to('cuda:1')
key = torch.randn(4, 16, 7, 30)
