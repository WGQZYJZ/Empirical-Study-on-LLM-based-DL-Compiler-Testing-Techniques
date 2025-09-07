
class Model(torch.nn.Module):
    def __init__(self, dim_query, dim_key, dim_value, dropout_p):
        super().__init__()
        self.dim_query = dim_query
        self.dim_key = dim_key
        self.dim_value = dim_value
        self.dropout_p = dropout_p
        self.query_linear = torch.nn.Linear(dim_query, dim_query)
        self.key_linear = torch.nn.Linear(dim_key, dim_key)
        self.value_linear = torch.nn.Linear(dim_value, dim_value)
 
    def forward(self, query, key):
        qv  = torch.cat([query, value], dim=1)  # Concatenate the query and value tensors into a 2D tensor by concatenating two dimension (batch, sequence, channel).
        query = self.query_linear(qv)  # Use a linear layer to compute the dot product of the input query and value tensor
        key = self.key_linear(qv)  # Use a linear layer to compute the dot product of the input query and key tensor
        scaled_qk  = query.div(self.dim_query ** -0.5)  # Scale the dot product by the inverse scale factor, then calculate the softmax function of the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(scaled_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model(dim_query=300, dim_key=256, dim_value=4, dropout_p=0.1)
x1 = torch.randn(1, 3, 64, 64)
