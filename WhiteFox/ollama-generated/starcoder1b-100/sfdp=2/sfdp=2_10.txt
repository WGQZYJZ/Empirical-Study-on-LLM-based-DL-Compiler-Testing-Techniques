
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, hidden_dim=512):
        super().__init__()
        self.query_layer = torch.nn.Linear(query_dim, hidden_dim)  # Create a layer for the query input
        self.key_layer   = torch.nn.Linear(key_dim,     hidden_dim)  # Create a layer for the key input
        self.fc1          = torch.nn.Linear(hidden_dim,    hidden_dim)  # Create a linear transformation to reduce dimensionality of query and value
        self.fc2          = torch.nn.Linear(hidden_dim,    2)         # Create a linear transformation for the attention score
        self.dropout      = torch.nn.Dropout(p=0.5)
        self.scale        = torch.sqrt(torch.FloatTensor([10]))

    def forward(self, x1, x2):
        # Get the hidden representation of query and key inputs
        qk  = torch.matmul(x1, x2.transpose(-2, -1)) / self.scale  # Compute the dot product of the query and the key
        scaled_qk  = qk.div(torch.sqrt(self.scale))         # Scale the dot product by the inverse scale factor
        # Perform a softmax over the scaled dot product for both the query and key inputs
        softmax_qk = scaled_qk.softmax(dim=-1)                   # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output

        # Compute the dot product of the hidden representation of query and value inputs
        output = dropout_qk.matmul(x2)                           # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


