
class Model(torch.nn.Module):
    def __init__(self, dim=128):
        super().__init__()
 
        self.dim = dim
        self.key_layer_norm = torch.nn.LayerNorm(dim)
        self.query_layer_norm = torch.nn.LayerNorm(dim)

        # We set the weight and bias of the two linear layers to zeros for initializing the parameters in this model.
        self.fc1 = torch.nn.Linear(2 * dim, dim, bias=False)
        self.fc2 = torch.nn.Linear(dim, 1, bias=False)
 
    def forward(self, x1):
        v1 = self.key_layer_norm(x1)
        v2 = torch.tanh(v1)
 
        v3 = self.query_layer_norm(x1)
        v4 = torch.tanh(v3)

        scaled_dot_product  = torch.matmul(v4, v2.transpose(-2, -1)) / (v1.shape[-1] ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
 
        output  = attention_weights.matmul(self.fc2(torch.tanh(self.fc1(v4.reshape(-1, self.dim * 3))))).reshape(*scaled_dot_product.shape[:-1], -1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
