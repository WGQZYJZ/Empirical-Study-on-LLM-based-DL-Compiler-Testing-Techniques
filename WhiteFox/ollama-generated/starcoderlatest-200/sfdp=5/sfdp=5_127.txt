
class Model(torch.nn.Module):
    def __init__(self, dim_key=64, dim_value=32, dropout=0.1, attn_mask=None, num_heads=8):
        super().__init__()
        self.dim_key = dim_key
        self.dim_value = dim_value
        self.dropout = dropout
        self.attn_mask = attn_mask
 
        # Create a set of multi-head attention layers with the specified number of heads and their dimension settings
        self.layers = torch.nn.ModuleList()
        for _ in range(num_heads):
            self.layers.append(
                MultiHeadAttention(dim_key=dim_key, dim_value=dim_value, dropout=dropout, attn_mask=attn_mask)
            )
 
    def forward(self, query, key, value):
        # Apply multiple heads attention layers to the inputs
        for layer in self.layers:
            query = layer(query, key, value)
 
        return query  # Return the output of the last head

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_key, dim_value, dropout=0.1, attn_mask=None):
        super().__init__()
        self.dim_key = dim_key
        self.dim_value = dim_value
        self.attn_dropout = torch.nn.Dropout(dropout)
 
        # Create the linear layers with dimension settings specified by the constructor
        self.q = torch.nn.Linear(dim_key + dim_value, dim_key, bias=False)
        self.k = torch.nn.Linear(dim_key + dim_value, dim_key, bias=False)
        self.v = torch.nn.Linear(dim_key + dim_value, dim_value, bias=False)
 
        # Create a linear layer with dimension settings that matches the last dimension of the output of the convolutions and the value input
        self.o = torch.nn.Linear(dim_key * 2, dim_value)
 
    def forward(self, query, key, value):
        attn_weight = self._attention_score(query, key)  # Compute the attention weights
        attn_weight = self.attn_dropout(attn_weight)  # Apply dropout to the computed attention weights
 
        output = torch.matmul(attn_weight, value)  # Multiply the attention weights by the values
        output = torch.cat([query, output], dim=1)  # Concatenate the query and the concatenated values together
        output = self.o(output)  # Compute the output of a linear layer
        
        return output  # Return the output of the final linear layer
 
    def _attention_score(self, query, key):
        # Perform two convolutional layers that match dimension settings with dimension settings from the last input
        q1 = self.q(query)
        q2 = torch.nn.Conv2d(key, 64, kernel_size=3, stride=1)(key)
 
        # Concatenate the output of the convolutions and then scale them by a factor of 0.5 for the attention score computation
        x = torch.cat([q1 * 0.5, q2], dim=-1)
        
        # Apply dropout to the linear input and then multiply it by `1 / math.sqrt(dim_key)`
        x = self._attention_score_linear_dropout(x) * (1 / math.sqrt(self.dim_key))  # Divide by sqrt(dimension of keys) to prevent exploding gradients

        return x
 
    def _attention_score_linear_dropout(self, x):
        x = torch.nn.Dropout(p=self.dropout)(x)  # Apply dropout before applying the linear transformation
        return self.attn_mask + F.linear(x, self.k(key), bias=None)  # Add the attention mask to the output of a linear layer
 

# Initializing the model
m = Model(dim_key=64, dim_value=32, dropout=0.1, attn_mask=attn_mask, num_heads=8)

# Inputs to the model
query  = torch.randn(1, 64, 192, 192)
key = torch.randn(1, 32, 192, 192)
value = torch.randn(1, 8, 192, 192)


# ___________________________________________________________________________________________________________________
