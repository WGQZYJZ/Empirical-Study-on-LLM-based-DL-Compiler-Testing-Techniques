
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) 
        v1 += attn_mask # Add the attention mask to the scaled dot product
        v3  = torch.softmax(v1, dim=-1) # Apply softmax to the result
        v4  = v3 @ value # Compute the dot product of the attention weights and the value
        return v4


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2, 80)
key  = query + 1
attn_mask  = torch.zeros([2,80]) - float('Inf')
attn_mask[0][0]  = 0
attn_mask[1][1] = 0
value  = key * math.sqrt(query.size(-1))

 # Initializing the model
m  = Model()
 
# Inputs to the model
x2 = torch.randn([5,4])

# Input to model for generating valid inputs and initializations
input_tensor  = x2
