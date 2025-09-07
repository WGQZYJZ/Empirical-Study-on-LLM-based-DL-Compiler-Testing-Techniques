
class Model(torch.nn.Module):
    def __init__(self, num_layers=4, num_heads=8, dim_feedforward=2048):
        super().__init__()
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.dim_feedforward = dim_feedforward

        # The input and output vectors will have the same shape as the value tensors
        self.query  = torch.nn.Linear(2048, dim_feedforward)
        self.key    = torch.nn.Linear(2048, dim_feedforward)
        self.value  = torch.nn.Linear(2048, dim_feedforward)

        # The feed forward network of the model (1)
        self.layers = nn.ModuleList()
        for i in range(self.num_layers):
            self.layers.append(nn.Linear(dim_feedforward, dim_feedforward))

    def forward(self, x):
        # The scale factor is chosen carefully to match the dimensions of the query and key tensors
        inv_scale = 1 / torch.sqrt(x.shape[-1])

        # Splitting the input and output vectors
        query   = self.query(x)  # Shape: batch size x number of input features
        key     = self.key(x)    # Shape: batch size x number of attention features
        value   = self.value(x)  # Shape: batch size x number of input features

        # The Scaled Dot-Product Attention mechanism is applied to the three vectors, and then the weighted sum of the values are used as intermediate representations
        query_output = query.matmul(key.transpose(-2, -1)) / inv_scale
        key_value    = key.matmul(value) / inv_scale
        attn         = torch.softmax(query_output, dim=-1)  # Shape: batch size x number of input features

        # The output is multiplied by the value vectors and then scaled to match the dimensions of the values
        outputs      = attn.matmul(value) / inv_scale

        for i in range(self.num_layers - 1):
            y = torch.nn.functional.relu(outputs[:, :, :dim_feedforward * 2])  # Residual connections
            y = self.layers[i](y)

        return outputs

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
