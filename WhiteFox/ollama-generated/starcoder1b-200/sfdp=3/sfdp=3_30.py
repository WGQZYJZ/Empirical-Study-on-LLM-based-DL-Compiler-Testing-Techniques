
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 128)
        self.key   = torch.nn.Linear(768, 128)
        self.value = torch.nn.Linear(128, 500)
 
    def forward(self, x1, x2):
        query   = F.dropout(self.query(x1), p=dropout_p, training=training) # Compute query as a linear projection
        key     = F.dropout(self.key   (x2), p=dropout_p, training=training)
        value   = self.value (x2)  # Compute the value vector as a linear projection
        scaled_query  = query.mm(key.t()) / np.sqrt(np.maximum(1e-6, key.shape[-1])) # Scale query
        softmax_query = scaled_query.softmax(-1) # Apply softmax to scale query
        dropout_qk    = F.dropout(softmax_query, p=dropout_p, training=training)  # Apply dropout to softmax output
        output       = dropout_qk.mm(value) # Compute the dot product of the dropout output and value tensor
        return output


# Initializing the model
m = Model()

