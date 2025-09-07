
class Model(torch.nn.Module):
    def __init__(self, **args):
        super().__init__()
        self.query = torch.nn.Linear(*input_dim)  # Define the query layer as input dimension 3
        self.key   = torch.nn.Linear(*key_dim)    # Define the key layer as output dimension 8

    def forward(self, q, k):
        v1 = self.query(q)
        v2 = self.key(k)
        v3 = torch.matmul(v1, v2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = v3 / math.sqrt(self.in_features * self.out_features)  # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return v3 + dropout_qk.matmul(k)

# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(1, 8, *query_dim)
k = torch.randn(1, 8, *key_dim)
