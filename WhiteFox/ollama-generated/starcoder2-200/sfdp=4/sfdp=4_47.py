
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, qk1, kq2):

        # Compute the dot product of the query and key
        dot = torch.einsum('ij..., jk... -> ijk...', qk1, kq2)
    
        # Add the attention mask to the scaled dot product
        mask  = torch.tensor([[[0., -math.inf], [torch.tensor(0.), math.inf]]])
        dot += mask

        # Compute softmax of the scaled dot product
        weight = F.softmax(dot, dim=2)
    
        # Compute dot product of attention weights and value
        v  = torch.einsum('ijk..., jkl -> ilk...',weight, vq1_2)

        return v


# Initializing the model with input and masking masks. 

m  = Model()
 
q1  = torch.randn(32, 5000)
k1  = torch.randn(32, 8000)
qk_1 = m(q1 , k1 ) # Initializing the model with input and masking masks. 

m  = Model()
 
qk_2  = m(q1 .to('cuda') , k1 .to('cuda'))


# The initial value of the attn_mask tensor is -inf, and torch.softmax(-inf) results in nan. Hence it would be better to initialize it as 0 instead of -inf.