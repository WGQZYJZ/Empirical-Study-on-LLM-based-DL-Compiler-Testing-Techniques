
class Model(torch.nn.Module):
    def __init__(self, d_model, heads, dim_feedforward=None, dropout=0.1):
        super().__init__()
 
        self.d_model = d_model
        self.heads = heads
        self.dim_feedforward = dim_feedforward
        self.fc1 = torch.nn.Linear(d_model, dim_feedforward)
        self.fc2 = torch.nn.Linear(dim_feedforward, d_model)
        self.dropout = dropout
 
        self.layernorm1 = LayerNorm(d_model)
        self.layernorm2 = LayerNorm(d_model)
 
    def forward(self, x):
        # If batch size is 0, don't do anything
        if x.size()[0] == 0:
            return x

        q, k, v = split_heads(x, self.heads) # Split heads from a tensor

        q = self.layernorm1(q)
        k = self.layernorm2(k)

        # Scale the query and key dimensions by sqrt(d_model)
        scale = torch.sqrt(torch.FloatTensor([self.d_model])).view((1, -1))  # [batch size, heads]
        
        attn = (q @ k).div(scale)
        attn = F.softmax(attn, dim=-1) # [batch size, heads]

        x = (attn @ v).transpose(-2, -1)  # Transpose the output to get the shape of [heads, batch size, seq length, d_model]
        x = self.dropout(x)
 
        x = x @ self.fc1  # Concatenate the result with fc1 to obtain the output.
        x = self.layernorm2(x)

        x = self.fc2(x)
        x = self.dropout(x)
        return x


# Initializing the model
model = Model()
x = torch.randn(5, 3, 64, 64)
