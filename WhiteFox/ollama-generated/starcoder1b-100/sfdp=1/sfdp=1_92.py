
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model
        self.query_layer = torch.nn.Linear(d_model, d_model)  # Embedding layer of the query and key tensors
        self.key_layer = torch.nn.Linear(d_model, d_model)
        self.value_layer = torch.nn.Linear(d_model, d_model)
        self.linear1 = torch.nn.Linear(d_model * 2, d_model)
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, q, k, v):
        # Embed the query and key tensors
        q = self.query_layer(q).float()
        k = self.key_layer(k).float()
        v = self.value_layer(v).float()
        # Compute the dot product of the query and key tensors
        qkv = torch.matmul(q, k)  # Compute the dot product of the query and key tensors
        # Scale the dot product by an inverse scale factor
        inv_scale_factor = 1 / math.sqrt(self.d_model)  # Compute the inverse scale factor
        qkv *= inv_scale_factor  # Multiply the dot product with the inverse scale factor
        # Apply softmax to the scaled dot product
        softmax_qk = qkv.softmax(-1)  # Apply softmax to the scaled dot product
        # Dropout to avoid model leakage, this is equivalent to adding a random value to every input to the network
        dropout_qk = self.dropout(softmax_qk)
        # Compute the dot product of the dropout output and the value tensor
        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model(d_model=512)
x = torch.randn(1, 64, 64)
y = m(q=x, k=x, v=x)
