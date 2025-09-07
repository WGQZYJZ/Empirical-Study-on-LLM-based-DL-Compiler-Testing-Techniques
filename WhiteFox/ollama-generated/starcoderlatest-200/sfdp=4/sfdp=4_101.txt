
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 8) # input: [batch_size, 256] output: [batch_size, 8]
        self.key = torch.nn.Linear(256, 8) # input: [batch_size, 256] output: [batch_size, 8]
 
    def forward(self, x1):
        qk = self.query(x1).view(-1, 8, 4, 4) @ self.key(x1).transpose(-2, -1) / math.sqrt(self.query.out_features) # input: [batch_size, 8, 4, 4] output: [batch_size, 8, 4, 4]
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 256)
attn_mask = torch.zeros(4).bool()
attn_mask[0] = True # Make sure only the first sample has attention enabled
