
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(4, 2)
        self.key   = torch.nn.Linear(4, 3)
        self.value = torch.nn.Linear(4, 1)
 
    def forward(self, x):
        query_v = self.query(x) # Get the feature vector from the first layer of the network.
        key_v   = self.key(x)   # Get the feature vector from the second layer of the network.
        value_v  = self.value(x)  # Get the output of the third layer of the network.
        scaled_qk = torch.matmul(query_v, key_v.transpose(-2, -1)) \
                    .div(torch.sqrt(self.attention_head_size ** -0.5) * query_v.shape[-1] ** (-0.5)).softmax(dim=-1)  # Get the softmax attention value for each example.
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)  # Apply dropout to the scaled dot product.
        output     = dropout_qk.matmul(value_v)  # Compute the dot product of the dropout output and the value.
        return output


# Initializing the model
m = Model()


