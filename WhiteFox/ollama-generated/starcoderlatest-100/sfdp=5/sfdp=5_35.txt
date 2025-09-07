
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 32)
 
    def forward(self, qk_value):
        attn_weight = qk_value[0] @ torch.transpose(qk_value[1], -2, -1) / math.sqrt(qk_value[1].size(-1)) # Compute the dot product of query and key and scale it
        attn_weight = attn_weight + 1
        attn_weight = torch.softmax(attn_weight, dim=-1) # Apply softmax to the scaled dot product
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = attn_weight @ qk_value[1] # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk_value  = (torch.randn(3, 8, 2, 5), torch.randn(768, 1))
