
class Model(torch.nn.Module):
    def __init__(self, query_size, key_size, value_size, num_layers, hidden_size, dropout_p):
        super().__init__()
        self.num_layers = num_layers

        # Initialize multi-head attention layers
        self.query_layer = MultiHeadAttention(key_size=key_size, query_size=query_size, hidden_size=hidden_size)
        
        for i in range(self.num_layers):
            layer_name = f"self_{i}"
            setattr(self, layer_name, MultiHeadAttention(key_size=key_size, query_size=value_size, hidden_size=hidden_size))
 
        # Final fully connected layer
        self.fc = torch.nn.Linear(num_layers*value_size, 2)
 
    def forward(self, x1):
        h_q = self.query_layer(x1)
 
        # Concatenate the heads and feed them through each of the multi-head attention layers
        for i in range(self.num_layers):
            layer_name = f"self_{i}"
            v = getattr(self, layer_name)(h_q)
            h_q = torch.cat([h_q, v], dim=-1)
 
        # Reshape the heads and feed it through a linear transformation
        v_f = h_q.view(-1, h_q.shape[-2]*h_q.shape[-1])
        output = self.fc(v_f)
 
        return output


# Initializing the model
m = Model(query_size=8, key_size=16, value_size=32, num_layers=2, hidden_size=128, dropout_p=0.5)

# Inputs to the model
x1 = torch.randn(1, 8, 32, 64)
