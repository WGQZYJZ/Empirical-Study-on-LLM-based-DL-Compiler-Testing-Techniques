
class Model(torch.nn.Module):
    def __init__(self, hidden_size=1024):
        super().__init__()
        self.hidden_size  = hidden_size

        self.query  = torch.nn.Linear(self.hidden_size, self.hidden_size) 
        self.key   = torch.nn.Linear(self.hidden_size, self.hidden_size)
        self.value = torch.nn.Linear(self.hidden_size, self.hidden_size)
 
    def forward(self, query):
        v1  = self.query(query).transpose(-2, -1) # Apply pointwise linear transformation to the query tensor
        v2  = self.key(query).transpose(-2, -1)  # Apply pointwise linear transformation to the key tensor
        scaled_qk  = torch.bmm(v1, v2) / inv_scale_factor # Compute the dot product of the query and the key using BMM

        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the output of the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v3 = dropout_qk.matmul(self.value(query)) 
        return v3

# Initializing the model
m = Model()


# Inputs to the model:
- The input query tensor is of shape `[2, 1024]` (the batch size is not specified here).
- The key tensor for each sample in the batch is of shape `[1024]`.
- `dropout_p` is a variable specifying dropout probability.
- `inv_scale_factor` is a variable specifying the inverse scale factor applied to the dot product.
- The hidden size of the Transformer model is 1024

