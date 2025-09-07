
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.fc1 = torch.nn.Linear(7, 64)
        self.fc2 = torch.nn.Linear(64, 10)

    def forward(self, x):
        v = self.conv(x)
        w_query = self.fc1(v).view(1, -1) # Convert to the same shape as w_key/w_value for the Scaled Dot-Product attention mechanism
        w_key = w_query.t()  # Compute a transposed version of w_query, which helps the implementation to avoid the dot product
        w_value = self.fc2(v)
        w_attention = torch.matmul(w_query, w_key.transpose(-2, -1)) / math.sqrt(math.pow(w_key.shape[1], 0.5)) # Compute the attention weights, which are usually called 'softmax' in Transformer models
        output = torch.matmul(w_value, w_attention)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
