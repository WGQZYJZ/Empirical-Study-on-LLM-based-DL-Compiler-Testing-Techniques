

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1, attn_mask=None):
        qk = torch.bmm(q1 / math.sqrt(q1.size(-1)),  k1.transpose(-2,-1)) # Compute the dot product of the query and key tensor. The result is scaled.
        if not (attn_mask is None):
            attn_weight = qk + attn_mask
        else:
            attn_weight = torch.softmax(qk, dim=-1)
        output  = v1 @ attn_weight # Compute the dot product of the value tensor and the attention weights
        return output


m  = Model()

# Inputs to the model
k1=torch.randn(50,4,256).view(-1, 4 , 8)
q1= torch.randn(32,4,256).view(-1,4 ,8)
v1 = q1.clone()
attn_mask = k1 @ k1.transpose(-2,-1) + 0.001 * torch.rand(k1.size()).to('cuda') # Compute the attention mask with a random value

__output__  = m(q1, k1, v1, attn_mask=attn_mask)


