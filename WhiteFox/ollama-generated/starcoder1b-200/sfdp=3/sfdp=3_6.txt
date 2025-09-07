
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size, hidden_size, num_layers=1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(input_dim=input_size,
                                                  num_heads=hidden_size // 2)
        self.fc   = torch.nn.Linear(hidden_size, output_size)
        self.layers = torch.nn.ModuleList([torch.nn.Linear(input_size, hidden_size) for _ in range(num_layers)])
 
    def forward(self, x):
        q = x
        # (batch, len_1, input_dim)
        k_list = []  # A list of the key tensors from each layer of the transformer
        v_list = []  # A list of the value tensors from each layer of the transformer
        for i in range(len(self.layers)):
            # (batch, hidden_size)
            q_i  = torch.nn.functional.dropout(q, p=0.125 * float(i+1)) # Apply dropout to q before projection
            k = self.attn(q_i, query=q_i)[0] #(batch, len_i, hidden_size)
            v = self.layers[i](k).contiguous().view(-1, self.fc.out_features) #(batch, hidden_size)
            # Append the key and value tensors of this layer to their respective lists
            k_list.append(k)
            v_list.append(v)
        # Concatenate all layers together
        k = torch.cat(k_list, dim=1).contiguous().view(-1, self.layers[0].out_features * len(self.layers)) #(batch, hidden_size)
        # Apply layerwise linear transformation and concatenate them along a new axis
        v = torch.cat([v for v in v_list], dim=0) #(batch, output_dim)
        return self.fc(torch.nn.functional.dropout(v, p=dropout_p))

# Initializing the model
model = Model(3, 2, 5, num_layers=3)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
