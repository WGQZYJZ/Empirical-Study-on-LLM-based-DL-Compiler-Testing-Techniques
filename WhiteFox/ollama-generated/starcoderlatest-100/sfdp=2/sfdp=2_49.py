
class Attention(torch.nn.Module):
    def __init__(self, num_heads: int = 4, dim_head: int = 64):
        super().__init__()
 
        self.num_heads = num_heads
        self.dim_head = dim_head
 
        self.query_layer = torch.nn.Linear(256, dim_head * num_heads)
        self.key_layer = torch.nn.Linear(256, dim_head * num_heads)
        self.value_layer = torch.nn.Linear(256, dim_head * num_heads)
 
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def transpose_for_scores(self, x):
        new_x_shape = x.size()[:-1] + (self.num_heads, self.dim_head)
        x = x.view(*new_x_shape)
        return x.permute([0, 2, 3, 1])
 
    def forward(self, x):
 
        # Take the transpose of each layer output and apply a linear transformation to obtain a series of context vectors
        query = self.transpose_for_scores(self.query_layer(x))
        key = self.transpose_for_scores(self.key_layer(x))
        value = self.transpose_for_scores(self.value_layer(x))
 
        # Apply a multi-head attention layer to obtain the output of our model and then apply dropout to prevent overfitting
        # The input is the transposed key, query, value so that the shape for the attention layer will match that required by torch.matmul().
        x = torch.matmul(self.dropout(query), self.dropout(key))
 
        # Scale the dot product so we get values between -1 and 1.
        x = x / (math.sqrt(float(self.dim_head)))
        x = torch.nn.functional.softmax(x, dim=-1)
        
        output = torch.matmul(self.dropout(value), self.dropout(x))
 
        # Apply linear transformation back to obtain the final representation of the query.
        x = torch.matmul(output, x.transpose(-2, -1)).squeeze()
 
        return x
