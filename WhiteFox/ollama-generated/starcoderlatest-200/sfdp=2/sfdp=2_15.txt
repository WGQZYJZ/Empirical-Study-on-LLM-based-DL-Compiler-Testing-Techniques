
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_projection = torch.nn.Linear(512, 64)
        self.query_projection = torch.nn.Linear(320, 64)
        self.output_projection = torch.nn.Linear(512, 16)
 
    def forward(self, x):
        key = self.key_projection(x) # Apply linear projection to the query representation
        query = self.query_projection(x)
        output = self.output_projection(x) # Apply linear projection to the hidden state

        qk = torch.matmul(query, key.transpose(-2,-1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output

        return output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = Attention()
 
    def forward(self, x1):
        v1 = self.attention(x1) # Run attention on the query representation
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 512, 64, 64)
