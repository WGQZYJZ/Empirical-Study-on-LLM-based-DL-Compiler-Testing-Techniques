
class Model(torch.nn.Module):
    def __init__(self, hidden_size=512):
        super().__init__()

        self.query = torch.nn.Linear(hidden_size // 4 * 7*7 , hidden_size)
        self.key = torch.nn.Linear(hidden_size // 4 * 7*7, hidden_size)
        self.value = torch.nn.Linear(hidden_size // 4 * 7*7, hidden_size)

        self._hidden_size = hidden_size

    def forward(self):
        attn_mask = torch.full((512//4, 30, 30), float('-inf'), device='cuda') # Create a full attention mask with dimensions (512/4, 30, 30) using the constant negative infinity (-inf)
        attn_mask.diagonal(-1).fill_(0.) # Fill the diagonal of the mask to zeros
        query = self.query(torch.randn(hidden_size // 8 * 7*7)) # Generate a random query vector with size (hidden_size/4*7,30)
        key = self.key(torch.randn(hidden_size//4 * 7*7)) 
        value = self.value(torch.randn(hidden_size // 8 * 7*7))
        v1 = query @ key.transpose(-2,-1)/ math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it using sqrt
        v2 = v1 + attn_mask # Add the attention mask to the scaled dot product
        v3 = torch.softmax(v2) # Apply softmax to the result
        v4 = torch.dropout(v3, 0.5, True)#Apply dropout to the softmax output with probability 0.5
        v6 = v4 @ value # Compute the dot product of the dropout output and the value

        return v1

# Initializing the model
model_0 = Model()


__output__= model_0()
