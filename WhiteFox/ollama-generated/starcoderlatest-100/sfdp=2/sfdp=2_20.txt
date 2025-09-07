
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(3, 8) # Embedding of each query token with dimension 8

    def forward(self, x1):
        qk = self.q(x1)  # Compute the dot product of each query and key embedding
        scaled_qk = qk / math.sqrt(qk.size(-1))
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        output = torch.matmul(softmax_qk, self.v) # Compute the dot product of the dropout output and the value embedding
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(500, 3, 64, 64)
