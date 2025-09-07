
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled = 1000

    def forward(self, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) / sqrt(self.scaled) # Scale the dot product of query and key by a factor sqrt(self.scaled), before softmaxing. 
        dropout_qk  = torch.nn.functional.dropout(qk.softmax(dim=-1), p=0.5)
        return v6 * value


# Initializing the model with random values for key, value
k, v  = torch.rand((32, 48)), torch.rand((32, 1, 769))
scale_factor = random()

# Inputs to the model: Query and key tensors. The value tensor is not used by the model.
query = torch.randn(1, 30, 7)
m(k, v)

