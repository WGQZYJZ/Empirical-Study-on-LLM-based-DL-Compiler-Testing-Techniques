
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Linear(64, 128)
        self.key_layer = torch.nn.Linear(64, 128)
        self.value_layer = torch.nn.Linear(128, 128)
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, x1, x2):
        # Query Layer: Compute the dot product of the query and key tensors
        query = self.query_layer(x1).view(-1, 64, 1, 1)
        # Key Layer: Compute the dot product of the query and key tensors
        key = self.key_layer(x2).view(64, -1, 1, 1)
        # Value Layer: Compute the dot product of the query and key tensors
        value = self.value_layer(x2).view(64, -1, 1, 1)
        # Apply dropout to the scaled dot product
        scaled_query = torch.matmul(query, key.transpose(-2, -1))
        scaled_key = scaled_query.mul(scale_factor)
        scaled_key = self.dropout(scaled_key)
        # Compute the softmax of the scaled dot product and multiply it with the query and key tensors
        softmax_query = scaled_key.softmax(dim=-1)
        dropout_query = torch.nn.functional.dropout(softmax_query, p=dropout_p)
        # Compute the dot product of the query and key tensor multiplied by the value tensor
        output = dropout_query.matmul(value)
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 20, 20)
x2 = torch.randn(20, 3, 20, 20)
