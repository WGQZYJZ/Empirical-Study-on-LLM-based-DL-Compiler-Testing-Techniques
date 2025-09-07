
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.randn(2, 3) 
        self.query = torch.randn(4, 7)
        self.value = torch.randn(1, 5, 8)
 
    def forward(self, attn_mask=None, dropout_p=0):
        k = self.key # Take the key from the input module parameters
        q = self.query 
        v = self.value 
        d = torch.einsum('ij, abjk->aibj', [q,k]) / math.sqrt(3)  # Compute the dot product of query and key, and scale it with sqrt(dim(-1))
        if attn_mask is not None:
            d += attn_mask # Add the attention mask to scaled dot-product output
        w = torch.softmax(d, dim=-2) # Apply softmax to dot product output 
        w = torch.dropout(w, p=dropout_p, training=self.training)  # Apply dropout to softmax output
        o = torch.einsum('aibj, abjk->aikj', [w, v]) # Compute the dot product of attention weights and value
        return o


# Initializing the model
m  = Model() 

 # Inputs to the model
attn_mask1  = None 
 attn_mask2  = torch.randn(4,7) + -5 # random mask, mask value is between (-inf,-5]
x = torch.ones(3, 3), torch.rand(6, 8, 9)

 __output__  = m(attn_mask1, x[0])
 __output2__  = m(attn_mask2, x[1])

 # If you find any other model with the correct output, please use the following code to run the test:
 # m(attn_mask=x[0])
 # m(attn_mask=x[1])


