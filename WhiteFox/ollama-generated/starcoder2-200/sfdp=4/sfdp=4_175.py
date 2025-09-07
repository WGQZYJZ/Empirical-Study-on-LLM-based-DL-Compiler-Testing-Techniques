
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.randn([32, 768]) # Embedding of a key vector
        self.query = torch.randn([1024, 768]) # Embedding of a query vector
 
    def forward(self):
        qk  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, and scale it by dividing each entry in the resulting tensor by the square root of its size (-1).
        qk  = qk + attn_mask # Add the attention mask to the scaled dot-product attention weights,
        attn_weights  = torch.softmax(qk) # Apply softmax to the result
        output  = attn_weights @ value # Compute a weighted sum of the values using the attentions
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn([1,2])
key = torch.randn([32,768])
value =  torch.randn([512,768])
attn_mask = torch.randn([4096, 3072],dtype=torch.float) # Attention mask. 
